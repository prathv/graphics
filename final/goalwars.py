from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import math
from math import *
from PIL.Image import *
from collections import *
from time import *
name = "Pattys Heli"
x = 0
y = -1.5
z = 2.0
ballx = 0
bally = -1.7
xspeed = 0.008
yspeed = 0.007
quadric = gluNewQuadric()
gravity = 0.0009
animate = 1
up = 1
down = 0
sizecube = 0.2
cube1x = -0.6
cube1y = -1.9
cube2x = 0.
cube2y = -1.9
forcey = 0.001 * yspeed
forcex = 0.004 * xspeed
radius = 0.04
left = 0
right = 0
stop = 0
lasttime = 0
forcethresh = [0.,0.,0.2,0.3,0.4,0.5,0.6,0.7]
forcethresh = [0.,-0.1,0.2,-0.3,-0.4,-0.5,-0.6,-0.7]
bound = glGenLists(1)
cube1 = glGenLists(1)
cube2 = glGenLists(1)
keys =  defaultdict((bool))
class Cyclone():

	def __init__(self):
		pass	
		
	def init(self,name="Pattys Goal Wars",size=(700,700)):
		global quadric
		
		gluQuadricNormals(quadric,GL_SMOOTH);
		gluQuadricTexture(quadric,GL_TRUE);
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
		glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH)-size[0])/2,(glutGet(GLUT_SCREEN_HEIGHT)-size[1])/2)
		glutInitWindowSize(size[0],size[1])
		glutCreateWindow(name)
                glEnable(GL_DEPTH_TEST)
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		
    # Create Texture    
    
    		glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    		glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
		
		global bound,cube1,cube2,sizecube 		
		
		glNewList(bound,GL_COMPILE) 	

	    
  		self.boundary() 
		
		self.post([-1.7,-1.8,0.],1) #-1.9,-1.8,0.1,
		self.post([1.7,-1.8,0.],2)	

		
		glEndList()

#		glNewList(cube1,GL_COMPILE) 	

#	    	self.cubecreate(sizecube/2,1)
  	
#		glEndList()
		
#		glNewList(cube2,GL_COMPILE) 	

#	    	self.cubecreate(sizecube/2,2)
  	
#		glEndList()
	

	

	    	

	    
		
    # Create Texture   
		glutKeyboardUpFunc(self.keypressed) 
 		#glutKeyboardFunc(self.keypressed)
	global x,y,z
	def camera(self,center=[x,y,z],look=[0,-1.9,0],up=[0,1,0]):
#		print "camera center is",(center[0],center[1],center[2])
		glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
		gluPerspective(50.,1.,0.1,100.0)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
		gluLookAt(center[0],center[1],center[2],
                              look[0],look[1],look[2],
                              up[0],up[1],up[2])
                glRotatef( self.Yrot, 0., 1., 0.)
                glRotatef( self.Xrot, 1., 0., 0.)
		glRotatef( self.Zrot, 0., 0., 1.)
#		if self.Scale < 0.1:
#			self.Scale = 0.1

#		glScalef(self.Scale,self.Scale,self.Scale)

	def LoadTextures(self,image):
    	#global texture
    		image = open(image)
    
   		ix = image.size[0]
    		iy = image.size[1]
   		image = image.tostring("raw", "RGBX", 0, -1)
    
    # Create Texture   
   		glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   # 2d texture (x and y size)
    
    		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    		glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)

    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
		



	def main(self):
		
		self.init()
		Createmenu()
		glutDisplayFunc(self.display)
		glutMainLoop()

	Yrot, Xrot,Scale,erot1,Zrot,srot,brot = [0,0,1.0,0,0,0,0]
	def display(self):
		global x,y,z,bound	
		self.camera(center=[x,y,z], look = [ballx,bally,0])
		self.draw_scene()
	#	self.checkkey()
		glutSwapBuffers()
		glutPostRedisplay()
 
	rhead = 0
	lhead = 0
	def draw_scene(self):
		global rotatey,animate,gravity,up,down,cube1x,cube1y,sizecube,radius,x,y
		global rotatez,quadric,ballx,bally,xspeed,yspeed,forcex,forcey,left,right,bound,cube1,cube2
		if rotatey == 0:
			self.Yrot += 1
		if rotatez == 0:
			self.Zrot += 0.1
		glClearColor(0.0, 0.0, 0.0, 0.0 )
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
			
		
		glCallList(bound)
		glPushMatrix()
		#glColor3f(1.0,0,0)
		
		glEnable(GL_TEXTURE_2D)
		self.LoadTextures("soccer.jpg")
		glTranslate(ballx,bally,0.)
		if left == 1:
			self.brot += 2
			glRotate(self.brot,0,0,1)
		if right == 1:
			self.brot += 2
			glRotate(self.brot,0,0,-1)
		glRotate(90,0,1,0)
		gluSphere(quadric,radius,32,32)
		
   		glDisable(GL_TEXTURE_2D)
		glPopMatrix()	
		
			
		glPushMatrix()
		glTranslate(cube1x,cube1y,0)
		self.rhead += 0.7
		#glutSolidCube(sizecube)
		glRotate(self.rhead,0,1,0)
		#glCallList(cube1)
		self.cubecreate(sizecube/2,1)
		glPopMatrix()

	
		glPushMatrix()
		glColor3f(0.5,0.5,0)
		self.lhead -= 0.7
		glTranslate(cube2x,cube2y,0)
	#	glutSolidCube(sizecube)
		glRotate(self.lhead,0,1,0)
		#glCallList(cube2)
		self.cubecreate(sizecube/2,2)
		glPopMatrix()



			#	glPushMatrix()
	#	glColor3f(1,0,0)
	#	glTranslate(cube1x,cube1y+(sizecube/2),0)
	#	gluSphere(quadric,0.0005,32,32)
	#	glPopMatrix()

	#	glPushMatrix()
	#	glColor3f(1,0,0)
	#	glTranslate(ballx,bally-radius,0)
	#	gluSphere(quadric,0.002,32,32)
	#	glPopMatrix()
	
		point = self.checkcol(radius,ballx,bally,cube1x,cube1y,sizecube)
		point2 = self.checkcol(radius,ballx,bally,cube2x,cube2y,sizecube)
#		print "Animate value" , animate
#		print "DOwn value and UP value",down,up	
		if animate == 0:
				
			self.cubecol(cube1x,cube1y,point)
			self.cubecol(cube2x,cube2y,point2)
			#print yspeed,up,down
#		print bally	
		
		self.goaldet()		
	
	def cubecreate(self, sizecube,cubeid):
		
		glPushMatrix()
		glEnable(GL_TEXTURE_2D)
		self.LoadTextures("sky.jpg")	
		
      		#glColor3f(1.0, 0.0, 0.0)
		glBegin(GL_QUADS)
		
				#top face
		glTexCoord2f(1.0,1.0)
      		glVertex3f( sizecube, 0.1, -sizecube)
		glTexCoord2f(1.0,0.0)
      		glVertex3f(-sizecube, 0.1, -sizecube)
		glTexCoord2f(0.0,0.0)
      		glVertex3f(-sizecube, 0.1,  sizecube)
		glTexCoord2f(0.0,1.0)
      		glVertex3f( sizecube, 0.1,  sizecube)
 	
		glEnd()
		glDisable(GL_TEXTURE_2D)
		glPopMatrix()

		glPushMatrix()
		#glEnable(GL_TEXTURE_2D)
		#self.LoadTextures("grass.jpg")	
		glRotate(90,0,1,0)
		glBegin(GL_QUADS) 
		

		#Bottom face
#		glColor3f(0.2, 0.5,0.0)
		#s,t (1,1)
   	      	glTexCoord2f(0.0,1.0)
		glVertex3f( sizecube, -sizecube,  sizecube)
      		#(0,0)
		glTexCoord2f(0.0,0.0)
		glVertex3f(-sizecube, -sizecube,  sizecube)
      		#(1,0)
		glTexCoord2f(1.15,0.0)
		glVertex3f(-sizecube, -sizecube, -sizecube)
      		#(0,1)
		glTexCoord2f(1.15,1.0)
		glVertex3f( sizecube, -sizecube, -sizecube)
 
	

   		glEnd()
		
		#need to change texture back to 2 maybe
		#glDisable(GL_TEXTURE_2D)
		glPopMatrix()
		if cubeid == 1:		
			self.LoadTextures("header.jpg")
		else:
			self.LoadTextures("header2.jpg")
   		glEnable(GL_TEXTURE_2D)
		glPushMatrix()
		
		#backFace
 #     		glColor3f(1, 1, 0.0)  
		#(0,1)
		glRotate(-90,0,0,1)
		glBegin(GL_QUADS)
		glTexCoord2f(1.0,0,0);
      		glVertex3f( sizecube, -sizecube, -sizecube)
		#(0,i0)
		glTexCoord2f(1.0,1.0);
   	        glVertex3f(-sizecube, -sizecube, -sizecube)
      		#(sizecube)
		glTexCoord2f(0.0,1.0);
		glVertex3f(-sizecube,  sizecube, -sizecube)
      		#(2,2)
		glTexCoord2f(0.0,0.0);
		glVertex3f( sizecube,  sizecube, -sizecube)
		glEnd()
 		glPopMatrix()



		
		glPushMatrix()
		#(0,1)
		#glRotate(,0,0,1)
		glBegin(GL_QUADS)
		#front face
      		#glColor3f(0.0, sizecube, 0.0)
		#(1,1)
      		glTexCoord2f(1.0,1.0);
		glVertex3f( sizecube,  sizecube, sizecube)
      		#(sizecube)
		glTexCoord2f(0.0,1.0);
		glVertex3f(-sizecube,  sizecube, sizecube)
      		#(0,0)
		glTexCoord2f(0.0,0.0);
		glVertex3f(-sizecube, -sizecube, sizecube)
		#(0,2)
		glTexCoord2f(1.0,0.0);
	        glVertex3f( sizecube, -sizecube, sizecube)
 		glEnd()
 		glPopMatrix()
	

		
		glPushMatrix()
		
	#	glRotate(90,si,0)
		glBegin(GL_QUADS)
		#left face
      		#glColor3f(sizecube, 0.0, 0.0)
		#(sizecube)
		glTexCoord2f(1.0,1.0);
      		glVertex3f(-sizecube,  sizecube,  sizecube)
      		#(2,2)
		glTexCoord2f(0.0,1.0);
		glVertex3f(-sizecube,  sizecube, -sizecube)
      		#(0,2)
		glTexCoord2f(0.0,0.0);
		glVertex3f(-sizecube, -sizecube, -sizecube)
		#(0,0)
		glTexCoord2f(1.0,0.0);
      		glVertex3f(-sizecube, -sizecube,  sizecube)
 
		glEnd()
 		glPopMatrix()


		
		glPushMatrix()
		#(0,2)
	#	glRotate(90,sizecube,0)
		glBegin(GL_QUADS)
		
		#right face
      		#glColor3f(sizecube, 0.0, sizecube)
		#(2,2)   
		glTexCoord2f(1.0,1.0); 
      		glVertex3f(sizecube,  sizecube, -sizecube)
      		#(sizecube)
		glTexCoord2f(0.0,1.0);
		glVertex3f(sizecube,  sizecube,  sizecube)
      		#(0,2)
		glTexCoord2f(0.0,0.0);
		glVertex3f(sizecube, -sizecube,  sizecube)
      		#(0,0)
		glTexCoord2f(1.0,0.0);
		glVertex3f(sizecube, -sizecube, -sizecube)		
		glEnd()
		
 		glPopMatrix()	
		
		glDisable(GL_TEXTURE_2D)

	def boundary(self):
	
		glPushMatrix()
		glEnable(GL_TEXTURE_2D)
		self.LoadTextures("sky.jpg")	
		glBegin(GL_QUADS)
		
				#top face
#      		glColor3f(0.0, 0.0, 1.0)
		glTexCoord2f(1.0,1.0)
      		glVertex3f( 2.0, 0.0, -2.0)
		glTexCoord2f(1.0,0.0)
      		glVertex3f(-2.0, 0.0, -2.0)
		glTexCoord2f(0.0,0.0)
      		glVertex3f(-2.0, 0.0,  2.0)
		glTexCoord2f(0.0,1.0)
      		glVertex3f( 2.0, 0.0,  2.0)
 	
		glEnd()
		glDisable(GL_TEXTURE_2D)
		glPopMatrix()

		glPushMatrix()
		glEnable(GL_TEXTURE_2D)
		self.LoadTextures("grass.jpg")	
		glRotate(90,0,1,0)
		glBegin(GL_QUADS) 
		

		#Bottom face
		#glColor3f(2.0, 0.5,0.0)
		#s,t (1,1)
   	      	glTexCoord2f(0.0,1.0)
		glVertex3f( 2.0, -2.0,  2.0)
      		#(0,0)
		glTexCoord2f(0.0,0.0)
		glVertex3f(-2.0, -2.0,  2.0)
      		#(1,0)
		glTexCoord2f(1.15,0.0)
		glVertex3f(-2.0, -2.0, -2.0)
      		#(0,1)
		glTexCoord2f(1.15,1.0)
		glVertex3f( 2.0, -2.0, -2.0)
 
	

   		glEnd()
	
		glDisable(GL_TEXTURE_2D)
		glPopMatrix()
		
		self.LoadTextures("crowd.jpg")
   		glEnable(GL_TEXTURE_2D)
		glPushMatrix()
		#backFace
      		#glColor3f(2.0, 2.0, 0.0)  
		#(0,1)
		glRotate(-90,0,0,1)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0,0,0);
      		glVertex3f( 2.0, -2.0, -2.0)
		#(0,0)
		glTexCoord2f(0.0,2.0);
   	        glVertex3f(-2.0, -2.0, -2.0)
      		#(2,0)
		glTexCoord2f(1.0,2.0);
		glVertex3f(-2.0,  2.0, -2.0)
      		#(2,2)
		glTexCoord2f(1.0,0.0);
		glVertex3f( 2.0,  2.0, -2.0)
		glEnd()
 		glPopMatrix()



		
		glPushMatrix()
		#(0,1)
		glRotate(90,0,0,1)
		glBegin(GL_QUADS)
		#front face
      		#glColor3f(0.0, 2.0, 0.0)
		#(1,1)
      		glTexCoord2f(1.0,2.0);
		glVertex3f( 2.0,  2.0, 2.0)
      		#(2,0)
		glTexCoord2f(1.0,0.0);
		glVertex3f(-2.0,  2.0, 2.0)
      		#(0,0)
		glTexCoord2f(0.0,0.0);
		glVertex3f(-2.0, -2.0, 2.0)
		#(0,2)
		glTexCoord2f(0.0,2.0);
	        glVertex3f( 2.0, -2.0, 2.0)
 		glEnd()
 		glPopMatrix()
	

		
		glPushMatrix()
		
		glRotate(90,2,0,0)
		glBegin(GL_QUADS)
		#left face
      		#glColor3f(2.0, 0.0, 0.0)
		#(2,0)
		glTexCoord2f(1.0,0.0);
      		glVertex3f(-2.0,  2.0,  2.0)
      		#(2,2)
		glTexCoord2f(1.0,2.0);
		glVertex3f(-2.0,  2.0, -2.0)
      		#(0,2)
		glTexCoord2f(0.0,2.0);
		glVertex3f(-2.0, -2.0, -2.0)
		#(0,0)
		glTexCoord2f(0.0,0.0);
      		glVertex3f(-2.0, -2.0,  2.0)
 
		glEnd()
 		glPopMatrix()


		
		glPushMatrix()
		#(0,2)
		glRotate(90,2,0,0)
		glBegin(GL_QUADS)
		
		#right face
      		#glColor3f(2.0, 0.0, 2.0)
		#(2,2)   
		glTexCoord2f(0.5,2.0); 
      		glVertex3f(2.0,  2.0, -2.0)
      		#(2,0)
		glTexCoord2f(0.5,0.0);
		glVertex3f(2.0,  2.0,  2.0)
      		#(0,2)
		glTexCoord2f(0.0,0.0);
		glVertex3f(2.0, -2.0,  2.0)
      		#(0,0)
		glTexCoord2f(0.0,2.0);
		glVertex3f(2.0, -2.0, -2.0)		
		glEnd()
		
		glDisable(GL_TEXTURE_2D)
 		glPopMatrix()	
		

	def post(self, coord , id = 1):
		

		glPushMatrix()
		
		glEnable(GL_TEXTURE_2D)
			
		glTranslate(coord[0],coord[1],coord[2]) 
		if id == 2:
			glRotate(180,0,1,0)
		glRotate(180,0,0,1)
		glRotate(90,0,1,0)
		
		self.LoadTextures("net.jpg")
		glBegin(GL_QUADS)
				#top face
      		#glColor3f(1.0, 0.0, 1.0)
		glTexCoord2f(0.8,0.77)
      		glVertex3f( 0.3, -0.2, -0.1)
		glTexCoord2f(0.5,0.77)
      		glVertex3f(-0.3, -0.2, -0.1)
		glTexCoord2f(0.5,0.3)
      		glVertex3f(-0.3, 0.2,  0.1)
		glTexCoord2f(0.8,0.3)
      		glVertex3f( 0.3, 0.2,  0.1)
		glEnd()
		
		glDisable(GL_TEXTURE_2D)
 		glPopMatrix()	
		#backFace
      		#glColor3f(0, 0.3, 1.0)  
		glPushMatrix()
		
		glEnable(GL_TEXTURE_2D)
		
		self.LoadTextures("post.jpg")
		glTranslate(coord[0],coord[1],coord[2])
		
		if id == 2:
			glRotate(180,0,1,0)
		glRotate(90,0,1,0)
		
		glBegin(GL_TRIANGLES)
	#	glTexCoord2f(0.0,0,0);
  #    		glVertex3f( 0.3, -0.3, -0.3)
		#(0,0)
		#glTexCoord2f(0.0,0.3);
 #  	        glVertex3f(-0.3, -0.3, -0.3)
      		#(0.3)
#		#glTexCoord2f(1.0,0.3);
#		glVertex3f(-0.3 , 0.3, -0.3)
      		#(0.3.3)
		#glTexCoord2f(1.0,0.0);
#		glVertex3f( 0.3,  0.3, -0.3)
		
		#left face
      		#glColor3f(0.3, 0.0, 0.0)
		#(0.3)
		glTexCoord2f(0.9,0.9);
	
      		glVertex3f(-0.3,  0.2,  0.1)
      		#(0.3.3)
		#glTexCoord2f(1.0,0.3);
		glTexCoord2f(1.,0.3);
		glVertex3f(-0.3,  -0.2, 0.1)
      		#(0,0.3)
		glTexCoord2f(0.3,0.3);
		glVertex3f(-0.3, -0.2, -0.1)
		#(0,0)
		#glTexCoord2f(0.0,0.0);
 


		
		#(0,0.3)
		
		#right face
      		#glColor3f(0.3, 0.0, 0.3.0)
		#(0.3.3)   
		glTexCoord2f(0.3,0.3); 
      		glVertex3f(0.3,  -0.2, -0.1)
      		#(0.3)
		glTexCoord2f(1.0,0.3);
		glVertex3f(0.3,  0.2,  0.1)
      		#(0,0.3)
		glTexCoord2f(1.0,1.0);
		glVertex3f(0.3, -0.2,  0.1)
      		#(0,0)
	#	glTexCoord2f(0.0,0.3);
		
		glEnd()
		glDisable(GL_TEXTURE_2D)
 		glPopMatrix()
		
	def keypressed(self,key,g,b):
		global rotatey,animate,ballx,bally,yspeed,xspeed
		global rotatez,cube1x,cube1y,left,right,cube2x,cube2y
		global x,y,z,keys
		if(key == 'f'):
			if animate == 0:
				animate = 1
			else:
				animate = 0	
		if(key == 'r'):
			if rotatey == 0:
				rotatey = 1
			else:
				rotatey = 0	
		if key == 'h':	
			if rotatez == 0:
				rotatez = 1
			else:
				rotatez = 0
		if key == 'w':	
			z -= 0.1
			
		if key == 'a':
			keys['a'] = True
		#	print "a is pressed"	
			cube1x -= 0.01
			if cube1x < -1.7:
					cube1x = -1.7
	
		else:
			keys['a'] = False
		#	print "a is released"
		
		if key == 's':	
			z += 0.1
		if key == 'd':	
			cube1x += 0.01
			if cube1x > 1.7:
				cube1x = 1.7
						
			
		if key == 'j':	
		#	print "j is pressed"
			keys['j'] = True
			if keys['j'] == True:
				cube2x -= 0.01
				if cube2x < -1.7:
					cube2x = -1.7

		if key == 'l':	
			cube2x += 0.01
			if cube2x > 1.7:
				cube2x = 1.7
					
		if key == "x":
			ballx = 0
			bally = -1.5
			yspeed = 0.008
			xspeed = 0.005
			left = 1
			right = 1
	
	def checkcol(self,rad,sphx,sphy,cubex,cubey,sizecube):
			diffx,diffy = sphx - cubex, sphy - cubey
#			print (sphx,sphy),(cubex,cubey),sizecube/2
#			print diffx - (sizecube/2) , diffy - sizecube/2	

			if abs(diffx) - (sizecube/2) > 0:
				a = (diffx - sizecube/2)/(abs(diffx-sizecube/2))
				pointx = a*sizecube/2
			else:
				pointx = diffx
	
			if abs(diffy) - (sizecube/2) > 0:
				b = (diffy - sizecube/2)/(abs(diffy-sizecube/2))
				pointy = b*sizecube/2
			else:
				pointy = diffy			
		#	print pointx  ,pointy ,sphx,cubex
			return (pointx + cubex,pointy + cubey,pointx,pointy)	

	def cubecol(self,cube1x,cube1y,point):
			global yspeed, xspeed, forcex,forcey, radius,ballx,bally,up,down,right,left,forcethresh
			
			
			if down == 0:
				
				distance = sqrt(pow(float(ballx - point[0]),2) +pow(float(bally - point[1]),2))
				print "Down",ballx,bally
				yspeed += gravity
				bally += -yspeed
				if left == 1:
					ballx -= xspeed
				if right == 1:
					ballx += xspeed
				if bally <= -1.9:
					bally = -1.9
					down = 1
					up = 0
		
				if ballx <= -1.7 :
					ballx = -1.7
					if bally <= -1.56:
						if bally != -1.8:
							bally -= 0.01
					else:
						ballx += -xspeed
				if ballx >= 1.7 and bally <= -1.56:
					ballx = 1.7
					if bally != -1.8:
						bally -= 0.01
					
	
				
				print "cube coordinates are",cube1x,cube1y
				print "ball coordinates",ballx,bally
				print "left right coordinates for",cube1x,point[2],point[3]

				print "distance between ball and point is ",distance,"radius is",radius
				
				kx = ((point[0] - cube1x)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
				ky = ((point[1] - cube1y)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
				print(kx,ky)
				kx = kx * (radius +  sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
				ky = ky * (radius + sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
				
				if  distance <= radius :
					print "collision",point[0],point[1]
					
					kx = ((point[0] - cube1x)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
					ky = ((point[1] - cube1y)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
					kx = kx * ( radius + sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
					ky = ky * ( radius + sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
					
					if point[2] <= 0:
						
				#		print "bally and x pre collision is",bally,ballx
						ballx = kx + cube1x	
						bally = ky + cube1y
						
				#		print "ballx and y after reset ",ballx,bally
						if point[3] >= 0.1:
				#			print "no x collison , entered"		

				#			print "kx and ky are",(kx,ky)
							if point[2] > -0.025:		
									ballx -= forcex
									bally += forcey 
							
							else:
									ballx -= 0.015+ forcex 
									bally += forcey
									xspeed = 0.015 + forcex		
		
				#			print "final position",ballx,bally,forcex,forcey
							up = 0
							down = 1
							left = 1
							right = 0	
							
					else: 	
						if point[2] > 0:
							ballx = kx + cube1x
							bally = ky + cube1y
								
							if point[3] >= 0.1:
								print "right x collision, entered"
								if point[2] < 0.025:		
									ballx += forcex
									bally += forcey 
								else:
									ballx += 0.015 + forcex 
									bally += forcey
									xspeed = 0.015 + forcex
							up = 0
							down = 1
							right = 1
							left = 0
								
					#	else:
					#		print "left x collision"
					#		ballx = kx + cube1x
					#		bally = ky + cube1y
					#		up = 0 
					#		down = 1
									
				else:
					print "No collision sucka"	
			if up == 0:
				
				distance = sqrt(pow(float(ballx - point[0]),2) +pow(float(bally - point[1]),2))
				print "up",ballx,bally
				if bally >= 2.0:
					bally = 1.9
						
				#	up = 1
				#	down = 0
			
					
				if ballx <= -1.7 :
					ballx = -1.7
					if bally <= -1.56:
						if bally != -1.9:
							print bally
							bally -= 0.01
					else:
						bally += yspeed
						ballx += -xspeed
						
				
				if ballx >= 1.7 and bally <= -1.5:
					ballx = 1.7
					if bally != -1.9:
						print bally
						bally -= 0.01
					
					
				bally += yspeed
								
				yspeed -= gravity


				if left == 1:
					ballx -= xspeed
				if right == 1:
					ballx += xspeed
				if  distance <= radius :
					print "collision"
						
					kx = ((point[0] - cube1x)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
					ky = ((point[1] - cube1y)/sqrt(pow(point[0]-cube1x,2)+pow(point[1]-cube1y,2)))
					kx = kx * (radius +  sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
					ky = ky * (radius + sqrt(pow(float(point[0] - cube1x),2) +pow(float(point[1] - cube1y),2)))
					if abs(point[0]) < 0.1 :
						print "no x collison"
						ballx = kx + cube1x	
						bally = ky + cube1y
						print "kx and ky are",(kx,ky)
							
						#up = 1
						#down = 0 	
					else: 	
						if point[0] < 0:
							print "right x collision"
							ballx = kx + cube1x
							bally = ky + cube1y
						else:
							print "left x collision"
							ballx = kx + cube1x
							bally = ky + cube1y
									
				else:
					print "No collision sucka"
				
				if yspeed < 0:
						up = 1
						down = 0		
	
	def goaldet(self):
			global ballx, bally ,left ,right,xspeed,yspeed,animate, lasttime, stop
			currtime = time()
			if ballx < -1.65 or ballx > 1.65 :
				if bally < -1.52 :
		#			print "player  scored"
					if stop == 0:
						animate = 1
						lasttime = currtime 
						stop = 1
					
				else:	
					if ballx < -1.65:
						ballx += xspeed + forcex
						left = 0
						right = 1
					else:
						ballx -= xspeed - forcex		
						left = 1
						right = 0
					
		
		#	print "bally, is ",bally
			if stop == 1 and (currtime - lasttime)%60 > 3 and lasttime != 0:
				stop = 0
				lasttime = 0
				animate = 0
				ballx = 0
				bally = -1.5
				yspeed = 0.003
				xspeed = 0.008
				left = 1
				right = 1
				down = 0
				up = 1	
		
				
				


	#def checkkey(self):
	#	global keys,cube1x,cube1y
	#	for x in keys:
	#		if keys['a'] == True:
	#			cube1x -= 0.01
		
		
				
									
rotatey = 1
rotatez = 1      	
cubemv = 0
def Createmenu():
		menu = glutCreateMenu(processMenuEvents)
		glutAddMenuEntry("Far View",1)
		glutAddMenuEntry("Close View",2)
		glutAttachMenu(GLUT_RIGHT_BUTTON)

def processMenuEvents(option):
             	global center
		global look
		global up
		if option == 1:
			print "far view"
			center = [0.4,1,2.7]
			look = [0,0,0]
			up = [0,1,0]
		else:
			pass	
	
		return 1 
		
c = Cyclone()
c.main()
