from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
from helipoints import *
from const import *
x = []

name = "Pattys Heli"
center = [0.4,1,2.7]
up = [0,1,0]
look = [0,0,0]

closevieweye = [0,0.07,-0.2]
class Cyclone():

	def __init__(self):
		pass	
		
	def init(self,name="Pattys",size=(700,700)):
	
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH )
		glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH)-size[0])/2,(glutGet(GLUT_SCREEN_HEIGHT)-size[1])/2)
		glutInitWindowSize(size[0],size[1])
		glutCreateWindow(name)
                glEnable(GL_DEPTH_TEST)
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		#glutKeyboardFunc(self.keypressed)

	def camera(self,center=[-0.2,0,0],look=[0,0.07,-0.2],up=[0,1,0]):
		glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
		gluPerspective(40.,1.,0.1,40.)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
		gluLookAt(center[0],center[1],center[2],
                              look[0],look[1],look[2],
                              up[0],up[1],up[2])
                glRotatef( self.Yrot, 0., 1., 0.)
                glRotatef( self.Xrot, 1., 0., 0.)
		glRotatef( self.Zrot, 0., 0., 1.)
		if self.Scale < 0.1:
			self.Scale = 0.1

		glScalef(self.Scale,self.Scale,self.Scale)

	def main(self):
		
		self.init()
		self.random_generator()
		Createmenu()
		#self.camera()
		glutDisplayFunc(self.display)
		glutMainLoop()

	Yrot, Xrot,Scale,erot1,Zrot,srot,drot = [0,0,0.1,0,0,0,0]
#srot is rotation for big blade and erot1 is rotation for small blade
	def display(self):
		
		self.camera(center,look,up)
		self.draw_scene()
		glutSwapBuffers()
		glutPostRedisplay()
 
	rv = []
	def random_generator(self):	
		for i in range(100):
			self.rv.append((random.randint(-10,10),random.randint(-100,100),random.randint(-10,10)))


	def draw_scene(self):
				
		glClearColor(0.0, 0.0, 0.0, 0.0 )
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.drot += 2.0
		self.srot += 2.0
		self.erot1 += 3*self.srot
		glPushMatrix()
                glTranslatef( 0., 0., 0. )
                glRotatef(  80.,   0., 1., 0. )
                glRotatef( -15.,   0., 0., 1. )	
                
		glBegin(GL_LINES)
		
		glColor3f(0,0,1)
	        
		for i in range(len(heliedges)):
			p0 = helipoints[heliedges[i][0]]
			p1 = helipoints[heliedges[i][1]]
			glVertex3f( p0[0], p0[1], p0[2] )
			glVertex3f( p1[0], p1[1], p1[2] )
#                	if i == len(heliedges)-1:
		glEnd()
		

		glPopMatrix()

		glPushMatrix()
		glTranslatef(-1.8,2.5,7.8)		
#		glRotatef(70,0,0,0)
		glRotatef(102,0,-1,0)

		glRotatef(self.erot1,0,0,1) 
		glBegin( GL_TRIANGLES )
		
		glColor3f(0.5,1,0)		
	        glVertex2f(  SMALL_BLADE_RADIUS,  SMALL_BLADE_WIDTH/2. )
	        glVertex2f(  0., 0. )
	        glVertex2f(  SMALL_BLADE_RADIUS, -SMALL_BLADE_WIDTH/2. )

	        glVertex2f( -SMALL_BLADE_RADIUS, -SMALL_BLADE_WIDTH/2. )
	        glVertex2f(  0., 0. )
	        glVertex2f( -SMALL_BLADE_RADIUS,  SMALL_BLADE_WIDTH/2. )
                glEnd()
		glPopMatrix()
	
		glPushMatrix()
		glTranslatef(0.9,3.8,-0.2)		
		glRotatef(self.srot,0,1,0) 
		glRotatef(90,1,0,0)
		glBegin( GL_TRIANGLES )
		
	        glVertex2f(  BLADE_RADIUS,  BLADE_WIDTH/2. )
	        glVertex2f(  0., 0. )
	        glVertex2f(  BLADE_RADIUS, -BLADE_WIDTH/2. )

	        glVertex2f( -BLADE_RADIUS, -BLADE_WIDTH/2. )
	        glVertex2f(  0., 0. )
	        glVertex2f( -BLADE_RADIUS,  BLADE_WIDTH/2. )
                glEnd()
		glPopMatrix()

		self.draw_diamond((0,1,0))
		#for i in range(100):
		#	self.draw_diamond(self.rv[i])
		text = "Hit C for Close view And H for far view "
#		self.draw_text(text,50,200)
		
	def draw_square(self,v):
		color = (random.random(),random.random(),random.random())
                glBegin(GL_QUADS)

                glColor3f(color[0],color[1],color[2])
                glVertex3f(v[0][0],v[0][1],v[0][2])
                glVertex3f(v[1][0],v[1][1],v[1][2])
                glVertex3f(v[2][0],v[2][1],v[2][2])
		glVertex3f(v[3][0],v[3][1],v[3][2])

                glEnd()

	def keypressed(self,key,x,y):
		global center
		global look
		global eye
		
		if(key == 'h'):
			center= [0,10,0]
			look = [0,0,0]
			eye = [0,0,-1]
		if(key == 'c'):
			center = [0,0,0]
			look = [-10,0,0]
			eye = [0,1,0]

#	def draw_text(self,text,x,y):

	#	glMatrixMode(GL_PROJECTION)
	#	glLoadIdentity()
	#	glOrtho(0,800,0,600,-5,5)
	#	glMatrixMode(GL_MODELVIEW)
	#	glLoadIdentity()
	#	glPushMatrix()
	#	glLoadIdentity()
	#	glRasterPos2f(x,y)
	#	for i in range(len(text)):
	#		glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(text[i]))
		#glPopMatrix()
	
	def draw_triangle(self,v):

                color = (random.random(),random.random(),random.random())
                glBegin(GL_TRIANGLES)
		glColor3f(color[0],color[1],color[2])
                glVertex3f(v[0][0],v[0][1],v[0][2])
                glVertex3f(v[1][0],v[1][1],v[1][2])
                glVertex3f(v[2][0],v[2][1],v[2][2])
                

                glEnd()

		

	def draw_diamond(self,v):
		glPushMatrix()
		s = 1.0
		length = 2.0
		v2 = (v[0]-s,v[1]-length,v[2]-s)
		v3 = (v[0]+s,v[1]-length,v[2]-s)
		v4 = (v[0]-s,v[1]-length,v[2]+s)
		v5 = (v[0]+s,v[1]-length,v[2]+s)
		v1 = (v[0],v[1]-(length*2),v[2])

#		glRotatef(self.drot,0,1,0)
		glTranslatef(1.5,2.5,-20)
		glRotatef(self.drot,0,1,0)
		self.draw_triangle((v2,v4,v))
		self.draw_triangle((v3,v2,v))
		self.draw_triangle((v5,v3,v))
		self.draw_triangle((v4,v5,v))
		self.draw_triangle((v2,v4,v1))
		self.draw_triangle((v3,v2,v1))
		self.draw_triangle((v5,v3,v1))
		self.draw_triangle((v4,v5,v1))
		glPopMatrix()
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
			print "close view"
			center = [0.12,0.28,-0.399]
			look = [0.4,0,-4.9]
			up = [0,1,0]
	
		return 1 
		
c = Cyclone()
c.main()
