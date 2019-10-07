import pygame
from pygame.locals import *
import math
import sys
import time
import random

class gun():
	def m_gun(self,gx,gy):
		screen=pygame.display.get_surface()
		gx=gx-3
		gun_1=pygame.draw.rect(screen,(200,0,0),Rect(gx,gy,6,8))
	def pos_gun(self,x,y,t):
		x1=x
		y1=y
		t1=t
		jud=1
		return jud,x1,y1,t1
	def e_gun(self,e_gx,e_gy):
		screen=pygame.display.get_surface()
		e_gx=e_gx-3
		gun_1=pygame.draw.rect(screen,(200,0,0),Rect(e_gx,e_gy,6,8))
	def p_beam(self,bx,by):
		screen=pygame.display.get_surface()
		bx=bx-5
		beam=pygame.draw.rect(screen,(200,40,100),Rect(bx,by,10,-400))
		return bx,by
	def e_beam(self,bx,by):
		screen=pygame.display.get_surface()
		bx=bx-5
		beam=pygame.draw.rect(screen,(200,40,100),Rect(bx,by,10,400))
		return bx,by
	def p_bom(self,bom_x,bom_y):
		screen=pygame.display.get_surface()
		pygame.draw.rect(screen,(200,200,200),Rect(bom_x-4,bom_y-4,8,8))
		return bom_x,bom_y
	def do_bom(self,bom_x,bom_y,ex,ey,e_hp):
		screen=pygame.display.get_surface()
		pygame.draw.line(screen,(200,0,0),(0,bom_y),(400,bom_y),14)
		pygame.draw.line(screen,(200,0,0),(bom_x,0),(bom_x,400),14)
		if ex-bom_x<17 and bom_x-ex<17 or ey-bom_y<7 and bom_y-ey<22:
			e_hp-=2
		return e_hp
class Player():
	def player(self,px,py):
		screen=pygame.display.get_surface()
		pygame.draw.rect(screen,(200,200,200),Rect(px-10,py,20,10))
		pygame.draw.line(screen,(200,200,200),(px-1,py-4),(px-1,py),6)
	def hit_p(self,x,y,e_gx,e_gy,e_gt,p_hp):
		screen=pygame.display.get_surface()
		if x-e_gx<13 and e_gx-x<13 and e_gy-y<15 and y-e_gy<8:
			p_hp-=5
			e_gx=-10
			e_gy=-10
			e_gt=0
			pygame.draw.rect(screen,(200,0,0),Rect(x-5,y-5,10,10))
		return e_gx,e_gy,e_gt,p_hp
	def hit_p_beam(self,x,y,bx,by,p_hp):
		screen=pygame.display.get_surface()
		if x-bx<16 and bx-x<16:
			p_hp-=1
			pygame.draw.rect(screen,(200,0,0),Rect(x-5,y-5,10,10))
		return p_hp
class Enemy():
	def enemy(self,ex,ey):
		screen=pygame.display.get_surface()
		pygame.draw.rect(screen,(200,100,0),Rect(ex-10,ey,20,10))
		pygame.draw.line(screen,(200,100,0),(ex-1,ey+14),(ex-1,ey),6)
	def hit_e(self,ex,ey,gx,gy,gt,e_hp):
		screen=pygame.display.get_surface()
		if ex-gx<13 and gx-ex<13 and gy-ey<15 and ey-gy<8:
			e_hp-=5
			gx=-10
			gy=-10
			gt=0
			pygame.draw.rect(screen,(200,0,0),Rect(ex-5,ey+5,10,10))
		return gx,gy,gt,e_hp
	def hit_e_beam(self,ex,ey,bx,by,e_hp):
		screen=pygame.display.get_surface()
		if ex-bx<16 and bx-ex<16:
			e_hp-=1
			pygame.draw.rect(screen,(200,0,0),Rect(ex-5,ey+5,10,10))
		return e_hp
class Item():
	def i_hp(self,tate_pos,yoko_pos,i_hp_jud,x,y,ex,ey,p_hp,e_hp):
		screen=pygame.display.get_surface()
		font=pygame.font.Font(None,20)
		pygame.draw.rect(screen,(100,200,100),Rect(yoko_pos-7,tate_pos,15,15))
		text=font.render("H",True,(255,255,255))
		screen.blit(text,[yoko_pos-5,tate_pos])
		if x-yoko_pos<18 and yoko_pos-x<17 and y-tate_pos<10 and tate_pos-y<15:
			p_hp+=10
			i_hp_jud=1
			p_hp_text=font.render("HP+10",True,(255,255,255))
			screen.blit(p_hp_text,[yoko_pos-5,tate_pos])
		if ex-yoko_pos<18 and yoko_pos-ex<17 and ey-tate_pos<10 and tate_pos-ey<15:
			e_hp+=10
			i_hp_jud=1
			e_hp_text=font.render("HP+10",True,(255,255,255))
			screen.blit(e_hp_text,[yoko_pos-5,tate_pos])
		return p_hp,e_hp,i_hp_jud
	def i_bom(self,tate_pos2,yoko_pos2,i_bom_jud,x,y,bom):
		screen=pygame.display.get_surface()
		font=pygame.font.Font(None,20)
		pygame.draw.rect(screen,(200,100,100),Rect(yoko_pos2-7,tate_pos2,15,15))
		text=font.render("B",True,(255,255,255))
		screen.blit(text,[yoko_pos2-5,tate_pos2])
		if x-yoko_pos2<18 and yoko_pos2-x<17 and y-tate_pos2<10 and tate_pos2-y<15:
			bom+=1
			i_bom_jud=1
			p_hp_text=font.render("bom+1",True,(255,255,255))
			screen.blit(p_hp_text,[yoko_pos2-5,tate_pos2])
		return bom,i_bom_jud
def main():
	jud=[]
	g=[]
	g_x=[]
	g_y=[]
	g_t=[]
	e_g_x=[]
	e_g_y=[]
	e_g_t=[]
	e_jud=[]
	p=Player()
	e=Enemy()
	item=Item()
	t_jud=0
	title_jud=0
	e_hp=100
	p_hp=100
	p_cha=0
	p_b_jud=0
	p_b_x=-20
	p_b_y=-20
	e_cha=0
	e_b_x=-20
	e_b_y=-20
	i_t_jud=0
	i_hp_jud=0
	i_t2_jud=0
	i_bom_jud=0
	bom_jud=0
	bom=0
	bom_t=0
	do_bom_jud=0
	for i in range(0,3):
		jud.append(0)
		e_jud.append(0)
		g.append(gun())
		g_x.append(-10)
		g_y.append(-10)
		g_t.append(0)
		e_g_x.append(-10)
		e_g_y.append(-10)
		e_g_t.append(0)
	(w,h)=(400,400)
	(x,y)=(w//2,h)
	(ex,ey)=(w//2,0)
	pygame.init()
	pygame.display.set_mode((w,h))
	pygame.display.set_caption("shooter")
	screen=pygame.display.get_surface()
	t_font=pygame.font.Font("HGRME.TTC",40)
	s_font=pygame.font.Font("HGRME.TTC",20)
	font=pygame.font.Font(None,20)
	font2=pygame.font.Font(None,40)
	t=0
	while(1):
		while title_jud==0:
			pygame.display.update()
			pygame.time.wait(30)
			title_text=t_font.render("シューティングゲーム",True,(255,255,255))
			screen.blit(title_text,[0,180])
			sub_text=s_font.render("w:発射,矢印:操作,enter:スタート",True,(255,255,255))
			sub_text2=s_font.render("s:チャージ・ビーム",True,(255,255,255))
			screen.blit(sub_text,[50,250])
			screen.blit(sub_text2,[50,320])
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					if event.key == 13:
						title_jud=1
		if t-i_t_jud>=100 and t-i_t_jud<=400 and i_hp_jud==0:
			if t-i_t_jud==100:
				tate_pos=random.randint(10,390)
				yoko_pos=random.randint(10,390)
			p_hp,e_hp,i_hp_jud=item.i_hp(tate_pos,yoko_pos,i_hp_jud,x,y,ex,ey,p_hp,e_hp)
		if t-i_t_jud>400:
			i_t_jud=t
			i_hp_jud=0
		if t-i_t2_jud>=100 and t-i_t2_jud<=400 and i_bom_jud==0:
			if t-i_t2_jud==100:
				tate_pos2=random.randint(200,390)
				yoko_pos2=random.randint(10,390)
			bom,i_bom_jud=item.i_bom(tate_pos2,yoko_pos2,i_bom_jud,x,y,bom)
		if t-i_t2_jud>400:
			i_t2_jud=t
			i_bom_jud=0
		if p_hp>0:
			font_p_hp="HP:"+str(p_hp)
		if e_hp>0:
			font_e_hp="HP:"+str(e_hp)
		if p_hp<=0:
			font_p_hp="You Lose"
			font_e_hp="You Lose"
		if e_hp<=0:
			font_e_hp="You Win"
			font_p_hp="You Win"
		if p_hp<=0 or e_hp<=0:
			exit_text=font2.render("press enter",True,(255,255,255))
			screen.blit(exit_text,[120,180])
		font_p_cha="charge"+str(p_cha)
		font_e_cha="charge"+str(e_cha)
		font_bom="bom"+str(bom)
		bom_text=font.render(font_bom,True,(255,255,255))
		e_cha_text=font.render(font_e_cha,True,(255,255,255))
		p_cha_text=font.render(font_p_cha,True,(255,255,255))
		p_hp_text=font.render(font_p_hp,True,(255,255,255))
		e_hp_text=font.render(font_e_hp,True,(255,255,255))
		screen.blit(bom_text,[330,320])
		screen.blit(p_hp_text,[330,380])
		screen.blit(e_hp_text,[330,20])
		screen.blit(p_cha_text,[330,350])
		screen.blit(e_cha_text,[330,50])
		t=t+1
		pressed_key = pygame.key.get_pressed()
		if pressed_key[K_LEFT]:
			x-=4
		if pressed_key[K_RIGHT]:
			x+=4
		if pressed_key[K_UP]:
			y-=4 
		if pressed_key[K_DOWN]:
			y+=4
		if pressed_key[115]:
			p_cha+=1
		if p_cha>100:
			p_cha=100
		if p_b_jud==1 and t-p_t_beam<20:
			p_b_x,p_b_y=g[0].p_beam(x,y)
		if p_b_jud==1 and t-p_t_beam>20:
			p_b_jud=0
			p_t_beam=0
			p_b_x=-20
			p_b_y=-20
			p_cha=0
		if pressed_key[100]:
			if bom>=1:
				bom_y-=6
				bom_x,bom_y=g[0].p_bom(bom_x,bom_y)
		if t-bom_t<20 and do_bom_jud==1:
			e_hp=g[0].do_bom(bom_x,bom_y,ex,ey,e_hp)
		if t-bom_t>20:
			bom_t=0
			do_bom_jud=0
		if jud[0]>0 and t-g_t[0]<50:
			g_y[0]=g_y[0]-10
			g[0].m_gun(g_x[0],g_y[0])
		if jud[0]>0 and t-g_t[0]>50:
			jud[0]=0
		if jud[1]>0 and t-g_t[1]<50:
			g_y[1]=g_y[1]-10
			g[1].m_gun(g_x[1],g_y[1])
		if jud[1]>0 and t-g_t[1]>50:
			jud[1]=0
		if jud[2]>0 and t-g_t[2]<50:
			g_y[2]=g_y[2]-10
			g[2].m_gun(g_x[2],g_y[2])
		if jud[2]>0 and t-g_t[2]>50:
			jud[2]=0
		if e_jud[0]>0 and t-e_g_t[0]<50:#
			e_g_y[0]=e_g_y[0]+10
			g[0].e_gun(e_g_x[0],e_g_y[0])
		if e_jud[0]>0 and t-e_g_t[0]>50:
			e_jud[0]=0
		if e_jud[1]>0 and t-e_g_t[1]<50:
			e_g_y[1]=e_g_y[1]+10
			g[1].e_gun(e_g_x[1],e_g_y[1])
		if e_jud[1]>0 and t-e_g_t[1]>50:
			e_jud[1]=0
		if e_jud[2]>0 and t-e_g_t[2]<50:
			e_g_y[2]=e_g_y[2]+10
			g[2].e_gun(e_g_x[2],e_g_y[2])
		if e_jud[2]>0 and t-e_g_t[2]>50:
			e_jud[2]=0#
		for i in range(3):
			if e_g_y[i]>h:
				e_jud[i]=0
				e_g_x[i]=-10
				e_g_y[i]=-10
				e_g_t[i]=0
			if g_y[i]<0:
				jud[i]=0
				g_x[i]=-10
				g_y[i]=-10
				g_t[i]=0
		pygame.display.update()
		pygame.time.wait(30)
		screen.fill((0, 20, 0, 0))
		if x<0:
			x=0
		if x>w:
			x=w
		if y>h-10:
			y=h-10
		if y<h/2:
			y=h/2
		p.player(x,y)
		if t_jud==0:
			rand=random.randint(0,100)
			t1=t
			t_jud=1
		if t_jud==1 and t-t1>10:
			t_jud=0
		if rand<30:
			ex+=4
		if rand>70:
			ex-=4
		if rand<100 and rand>60:
			ey+=4
		if rand>10 and rand<40:
			ey-=4
		if rand<30:
			e_cha+=1
		if e_cha>=100:
			e_b_x,e_b_y=g[0].e_beam(ex,ey)
		if e_cha==100:
			t2=t
		if e_cha>=100 and t-t2>20:
			e_cha=0
			e_b_x=-20
			e_b_y=-20
		g_rand=random.randint(0,100)
		if g_rand<3:
			if e_jud[0]==0:
				e_jud[0],e_g_x[0],e_g_y[0],e_g_t[0]=g[0].pos_gun(ex,ey,t)
			if e_jud[1]==0 and e_jud[0]==2:
				e_jud[1],e_g_x[1],e_g_y[1],e_g_t[1]=g[1].pos_gun(ex,ey,t)
			if e_jud[2]==0 and e_jud[1]==2:
				e_jud[2],e_g_x[2],e_g_y[2],e_g_t[2]=g[2].pos_gun(ex,ey,t)
			if e_jud[0]==1:
				e_jud[0]=2
			if e_jud[1]==1:
				e_jud[1]=2
		if ex<0:
			ex=0
		if ex>w:
			ex=w
		if ey<0:
			ey=0
		if ey>h//2-15:
			ey=h//2-15
		e.enemy(ex,ey)
		e_hp=e.hit_e_beam(ex,ey,p_b_x,p_b_y,e_hp)
		p_hp=p.hit_p_beam(x,y,e_b_x,e_b_y,p_hp)
		for i in range(3):
			g_x[i],g_y[i],g_t[i],e_hp=e.hit_e(ex,ey,g_x[i],g_y[i],g_t[i],e_hp)
			e_g_x[i],e_g_y[i],e_g_t[i],p_hp=p.hit_p(x,y,e_g_x[i],e_g_y[i],e_g_t[i],p_hp)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				if event.key == 119:#w
					if jud[0]==0:
						jud[0],g_x[0],g_y[0],g_t[0]=g[0].pos_gun(x,y,t)
					if jud[1]==0 and jud[0]==2:
						jud[1],g_x[1],g_y[1],g_t[1]=g[1].pos_gun(x,y,t)
					if jud[2]==0 and jud[1]==2:
						jud[2],g_x[2],g_y[2],g_t[2]=g[2].pos_gun(x,y,t)
				if event.key == 13:
					if p_hp<=0 or e_hp<=0:
						pygame.quit()
						sys.exit()
				if event.key == 100:
					if bom>=1:
						bom_x=x
						bom_y=y
						bom_x,bom_y=g[0].p_bom(bom_x,bom_y)
			if event.type == KEYUP:
				if event.key == 119:#w
					if jud[0]==1:
						jud[0]=2
					if jud[1]==1:
						jud[1]=2
				if event.key == 115:#s
					if p_cha==100:
						p_t_beam=t
						p_b_jud=1
				if event.key == 100:#d
					if bom>=1:
						bom-=1
						bom_t=t
						do_bom_jud=1
if __name__ == "__main__":
	main()