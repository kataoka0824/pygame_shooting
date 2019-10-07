import pygame
from pygame.locals import *
import math
import sys,os
import time
import random
class Scope():
	def scope(self,s_x,s_y,w,h):
		screen=pygame.display.get_surface()
		pygame.draw.circle(screen,(200,200,200),(s_x,s_y),2)
		pygame.draw.line(screen,(200,200,200),(s_x-1,s_y-5),(s_x-1,s_y-20),2)
		pygame.draw.line(screen,(200,200,200),(s_x-1,s_y+5),(s_x-1,s_y+20),2)
		pygame.draw.line(screen,(200,200,200),(s_x-5,s_y-1),(s_x-20,s_y-1),2)
		pygame.draw.line(screen,(200,200,200),(s_x+5,s_y-1),(s_x+20,s_y-1),2)
		pressed_key = pygame.key.get_pressed()
		if pressed_key[K_LEFT]:
			s_x-=4
		if pressed_key[K_RIGHT]:
			s_x+=4
		if pressed_key[K_UP]:
			s_y-=4 
		if pressed_key[K_DOWN]:
			s_y+=4
		if s_x<0:
			s_x=0
		if s_x>w:
			s_x=w
		if s_y<0:
			s_y=0
		if s_y>h:
			s_y=h
		return s_x,s_y
	def shot(self,s_x,s_y,s_jud,t_jud,ft,mt,hit_jud):
		screen=pygame.display.get_surface()
		tim=Time()
		mt,t_jud=tim.ftime_made(ft,mt,3,t_jud)
		if s_jud==1:
			pygame.draw.circle(screen,(200,30,30),(s_x,s_y-70*((ft-mt)-3)),6*(4-ft+mt))
		if t_jud==0 and s_jud==0:
			hit_jud=0
		if t_jud==0 and s_jud==1:
			hit_jud=1
			s_jud=0
		return s_jud,mt,t_jud,hit_jud
class Time():
	def ftime_made(self,ft,mt,m_t,t_jud):
		if t_jud==1:
			t_jud=2
			mt=ft
		if t_jud==2 and ft-mt>m_t:
			t_jud=0
		return mt,t_jud
class Enemy():
	def enemy(self,ex,ey,ft,mt,t_jud,w,h,move,Lv_k,Lv):
		screen=pygame.display.get_surface()
		tim=Time()
		mt,t_jud=tim.ftime_made(ft,mt,5,t_jud)
		pygame.draw.rect(screen,(50,200,50),Rect(ex-20,ey-2,40,4))
		pygame.draw.rect(screen,(50,200,50),Rect(ex-2,ey-20,4,40))
		pygame.draw.circle(screen,(200,100,0),(ex,ey),12)
		pygame.draw.circle(screen,(0,0,200),(ex,ey),10)
		pygame.draw.circle(screen,(200,200,200),(ex,ey),6)
		pygame.draw.circle(screen,(0,0,0),(ex,ey),2)
		if t_jud==0:
			t_jud=1
			move=random.randint(0,100)
		if t_jud==2 and Lv<=5:
			if move>=0 and move<24:
				ex+=2
			if move>=36 and move<72:
				ex-=2
			if move>=12 and move<48:
				ey+=2
			if move>=48 and move<94:
				ey-=2
		if t_jud==2 and Lv>5 and Lv<=10:
			if move>=0 and move<24:
				ex+=4
			if move>=36 and move<72:
				ex-=4
			if move>=12 and move<48:
				ey+=4
			if move>=48 and move<94:
				ey-=4
		if t_jud==2 and Lv>10 and Lv<=15:
			if move>=0 and move<24:
				ex+=6
			if move>=36 and move<72:
				ex-=6
			if move>=12 and move<48:
				ey+=6
			if move>=48 and move<94:
				ey-=6
		if ex<0:
			ex=0
			move=0
		if ex>w:
			ex=w
			move=49
		if ey<0:
			ey=0
			move=25
		if ey>h:
			ey=h
			move=90
		return ex,ey,mt,t_jud,move,Lv_k
	def e_hit(self,ex,ey,hit_jud,s_x,s_y,ft,e_mt,e_t_jud,enemy_jud,point,hit_ex,hit_ey,Lv):
		screen=pygame.display.get_surface()
		tim=Time()
		if hit_jud==1 and s_x-ex<13 and ex-s_x<13 and s_y-ey<13 and ey-s_y<13:
			enemy_jud=0
			e_t_jud=1
			e_mt=0
			point+=10
			hit_ex=ex
			hit_ey=ey
			if Lv>5 and Lv<=10:
				point+=20
			if Lv>10 and Lv<=15:
				point+=40
		e_mt,e_t_jud=tim.ftime_made(ft,e_mt,3,e_t_jud)
		if e_t_jud==2 and enemy_jud==0:
			pygame.draw.circle(screen,(200,0,0),(hit_ex,hit_ey),20)
			ex=-30
			ey=-30
		return e_mt,e_t_jud,enemy_jud,point,ex,ey,hit_ex,hit_ey
	def e_shot(self,ex,ey,ft,t,e_mt_shot,e_t_shot,p_hp,Lv):
		screen=pygame.display.get_surface()
		tim=Time()
		if t%8>=5:
			pygame.draw.circle(screen,(200,200,40),(ex,ey),6)
		if t%8==7:
			e_t_shot=1
		e_mt_shot,e_t_shot=tim.ftime_made(ft,e_mt_shot,3,e_t_shot)
		if e_t_shot==2:
			pygame.draw.circle(screen,(200,30,30),(ex,ey+70*((ft-e_mt_shot))),50*(ft-e_mt_shot))
			if ft-e_mt_shot==2:
				p_hp-=10
				if Lv>5 and Lv<=10:
					p_hp-=5
				if Lv>10 and Lv<=15:
					p_hp-=10
				screen.fill((200,20,0,0))
		return e_mt_shot,e_t_shot,p_hp
def hp_ber(p_hp,w,h,font,max_p_hp):
	screen=pygame.display.get_surface()
	if p_hp<0:
		p_hp=0
	if p_hp>50:
		pygame.draw.rect(screen,(20,200,20),Rect(w-100,10,p_hp//2,10))
	if p_hp<=50 and p_hp>10:
		pygame.draw.rect(screen,(200,200,20),Rect(w-100,10,p_hp//2,10))
	if p_hp<=10 and p_hp>=0:
		pygame.draw.rect(screen,(200,20,20),Rect(w-100,10,p_hp//2,10))
	pygame.draw.rect(screen,(200,200,200),Rect(w-100,10,max_p_hp//2,10),2)
	text=font.render("HP:",True,(200,200,200))
	screen.blit(text,[470,10])
def time(t,ft):
	ft+=1
	if ft>=30*(t+1):
		t+=1
	return t,ft
def mode_title(title_jud,font1,Lv,Lv_k):
	screen=pygame.display.get_surface()
	pygame.display.update()
	pygame.time.wait(30)
	text1=font1.render("Press_Enter",True,(200,200,200))
	screen.blit(text1,[200,200])
	text2=font1.render("w:発射,矢印キー:移動",True,(200,200,200))
	screen.blit(text2,[150,300])
	for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == 13:
						title_jud=1
						Lv+=1
						Lv_k+=1
	return title_jud,Lv,Lv_k
def mode_Lv_point(Lv,font1,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,w,h,e,hit_ex,hit_ey,Lv_k):
	screen=pygame.display.get_surface()
	pygame.display.update()
	pygame.time.wait(30)
	text1=font1.render("Press_Enter",True,(200,200,200))
	screen.blit(text1,[200,200])
	Lv_moji="Lv"+str(Lv)+"クリア"
	text2=font1.render(Lv_moji,True,(200,200,200))
	screen.blit(text2,[210,300])
	ft=0
	t=0
	p_hp=100
	s_jud=0
	t_jud=[0]
	mt=[0]
	lv_jud=0
	ex=[]
	ey=[]
	e_t_jud=[]
	e_mt=[]
	e_t_shot=[]
	e_mt_shot=[]
	enemy_jud=[]
	e_move=[]
	e=[]
	hit_ex=[]
	hit_ey=[]
	for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == 13:
						Lv+=1
						lv_jud=1
						Lv_k+=1
	if Lv%5==1:
		Lv_k=1
	if lv_jud==1:
		for i in range(Lv_k):
			ex.append(w//2)
			ey.append(h//2)
			e_t_jud.append(0)
			e_mt.append(0)
			e_t_shot.append(0)
			e_mt_shot.append(0)
			enemy_jud.append(1)
			e_move.append(0)
			e.append(Enemy())
			hit_ex.append(0)
			hit_ey.append(0)
	return Lv,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,e,hit_ex,hit_ey,Lv_k
def mode_gameover(Lv,font1,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,w,h,e,s_x,s_y,point,Lv_k):
	screen=pygame.display.get_surface()
	pygame.display.update()
	pygame.time.wait(30)
	game_jud=0
	text=font1.render("GAMEOVER",True,(200,200,200))
	screen.blit(text,[250,220])
	text1=font1.render("Enter:Lv1から",True,(200,200,200))
	screen.blit(text1,[230,270])
	text2=font1.render("q:やめる",True,(200,200,200))
	screen.blit(text2,[250,320])
	for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == 13:
						Lv=1
						Lv_k=1
						game_jud=1
					if event.key == 113:#q
						pygame.quit()
						sys.exit()
	if game_jud==1:
		(s_x,s_y)=(w//2,h//2)
		ex=[w//2]
		ey=[h//2]
		ft=0
		t=0
		p_hp=100
		s_jud=0
		t_jud=[0]
		mt=[0]
		e_t_jud=[0]
		e_mt=[0]
		e_t_shot=[0]
		e_mt_shot=[0]
		enemy_jud=[1]
		e=[Enemy()]
		e_move=[0]
		point=0
	return Lv,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,e,s_x,s_y,point,Lv_k
def mode_gameclear(font1):
	screen=pygame.display.get_surface()
	screen.fill((0,20,0,0))
	text=font1.render("ゲームクリア！",True,(200,200,200))
	screen.blit(text,[220,220])
	text1=font1.render("Enter:終了",True,(200,200,200))
	screen.blit(text1,[230,270])
	for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == 13:
						pygame.quit()
						sys.exit()
	pygame.display.update()
	pygame.time.wait(30)
def main():
	fp="hiscore.txt"
	pygame.init()
	(w,h)=(600,600)
	(s_x,s_y)=(w//2,h//2)
	ex=[w//2]
	ey=[h//2]
	ft=0
	t=0
	p_hp=100
	max_p_hp=p_hp
	s_jud=0
	t_jud=[0]
	mt=[0]
	e_t_jud=[0]
	e_mt=[0]
	e_t_shot=[0]
	e_mt_shot=[0]
	enemy_jud=[1]
	s=Scope()
	e=[Enemy()]
	tim=Time()
	hit_jud=0
	e_move=[0]
	point=0
	title_jud=0
	Lv=0
	hit_ex=[0]
	hit_ey=[0]
	Lv_k=0
	pygame.display.set_mode((w,h))
	pygame.display.set_caption("的あて")
	screen=pygame.display.get_surface()
	font=pygame.font.Font(None,20)
	font1=pygame.font.Font("HGRME.TTC",20)
	with open(fp,mode="r") as f:
			hiscore=f.read()
			hiscore_moji="hiscore:"+hiscore
			print(int(hiscore))
	while (1):
		while title_jud==0:
			title_jud,Lv,Lv_k=mode_title(title_jud,font1,Lv,Lv_k)
		while sum(enemy_jud)==0:
			Lv,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,e,hit_ex,hit_ey,Lv_k=mode_Lv_point(Lv,font1,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,w,h,e,hit_ex,hit_ey,Lv_k)
		while p_hp<=0:
			Lv,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,e,s_x,s_y,point,Lv_k=mode_gameover(Lv,font1,ft,t,p_hp,s_jud,t_jud,mt,ex,ey,e_t_jud,e_mt,e_t_shot,e_mt_shot,enemy_jud,e_move,w,h,e,s_x,s_y,point,Lv_k)
		while Lv==16:
			mode_gameclear(font1)
		t,ft=time(t,ft)
		hiscore_text=font.render(hiscore_moji,True,(200,200,200))
		screen.blit(hiscore_text,[500,60])
		time_moji="time:"+str(t)
		point_moji="得点:"+str(point)
		point_text=font1.render(point_moji,True,(200,200,200))
		screen.blit(point_text,[500,120])
		time_text=font.render(time_moji,True,(200,200,200))
		screen.blit(time_text,[500,100])
		ftime_moji="ftime:"+str(ft)
		ftime_text=font.render(ftime_moji,True,(200,200,200))
		screen.blit(ftime_text,[500,80])
		lv_moji="Lv"+str(Lv)
		lv_text=font.render(lv_moji,True,(200,200,200))
		screen.blit(lv_text,[10,10])
		for i in range(Lv_k):
			if enemy_jud[i]==1:
				ex[i],ey[i],e_mt[i],e_t_jud[i],e_move[i],Lv_k=e[i].enemy(ex[i],ey[i],ft,e_mt[i],e_t_jud[i],w,h,e_move[i],Lv_k,Lv)
				e_mt_shot[i],e_t_shot[i],p_hp=e[i].e_shot(ex[i],ey[i],ft,t,e_mt_shot[i],e_t_shot[i],p_hp,Lv)
			e_mt[i],e_t_jud[i],enemy_jud[i],point,ex[i],ey[i],hit_ex[i],hit_ey[i]=e[i].e_hit(ex[i],ey[i],hit_jud,s_x,s_y,ft,e_mt[i],e_t_jud[i],enemy_jud[i],point,hit_ex[i],hit_ey[i],Lv)
		s_x,s_y=s.scope(s_x,s_y,w,h)
		s_jud,mt[0],t_jud[0],hit_jud=s.shot(s_x,s_y,s_jud,t_jud[0],ft,mt[0],hit_jud)
		hp_ber(p_hp,w,h,font,max_p_hp)
		pygame.display.update()
		pygame.time.wait(30)
		screen.fill((0,20,0,0))
		fp="hiscore.txt"
		with open(fp,mode="w") as f:
			if point>=int(hiscore):
				f.write(str(point))
			if point<int(hiscore):
				f.write(hiscore)
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == 119:#w
					s_jud=1
					t_jud[0]=1
				if event.key == 115:#s
					for i in range(Lv_k):
						enemy_jud[i]=0

if __name__ == "__main__":
	main()