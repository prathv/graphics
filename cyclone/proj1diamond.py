
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random

name = "Pattys"

class Cyclone():

	def __init__(self):
		pass	
		
	def init(self,name="Pattys",size=(700,700)):
	
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
		glutInitWindowPosition((glutGet(GLUT_SCREEN_WIDTH)-size[0])/2,(glutGet(GLUT_SCREEN_HEIGHT)-size[1])/2)
		glutInitWindowSize(size[0],size[1])
		glutCreateWindow(name)
                glEnable(GL_DEPTH_TEST)
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


	def camera(self,center=[0,0,10],look=[0,0,0],up=[0,1,0]):
	
		glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
		gluPerspective(40.,1.,1.,40.)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
		gluLookAt(center[0],center[1],center[2],
                              look[0],look[1],look[2],
                              up[0],up[1],up[2])
		
                glRotatef( self.Yrot, 0., 1., 0. )
                glRotatef( self.Xrot, 1., 0., 0. )
		
		if self.Scale < 0.1:
			self.Scale = 0.1

		glScalef(self.Scale,self.Scale,self.Scale)

	def main(self):
		self.init()
		self.camera()
		self.random_generator()
		glutDisplayFunc(self.display)
		glutMainLoop()

	Yrot, Xrot,Scale = [0,0,0.1]
	
	def display(self):
		
		self.draw_scene()
		self.camera()
		glutSwapBuffers()
		glutPostRedisplay()
 	
	def draw_triangle(self,v):

               
                color = (random.random(),random.random(),random.random())
                glBegin(GL_TRIANGLES)

		glColor3f(color[0],color[1],color[2])
                glVertex3f(v[0][0],v[0][1],v[0][2])
                glVertex3f(v[1][0],v[1][1],v[1][2])
                glVertex3f(v[2][0],v[2][1],v[2][2])
                

                glEnd()

	def draw_square(self,v):


                color = (random.random(),random.random(),random.random())
                glBegin(GL_QUADS)

                glColor3f(color[0],color[1],color[2])
                glVertex3f(v[0][0],v[0][1],v[0][2])
                glVertex3f(v[1][0],v[1][1],v[1][2])
                glVertex3f(v[2][0],v[2][1],v[2][2])
		glVertex3f(v[3][0],v[3][1],v[3][2])

                glEnd()

	

	def draw_diamond(self,v):
		s = 1.0
		length = 2.0
		v2 = (v[0]-s,v[1]-length,v[2]-s)
		v3 = (v[0]+s,v[1]-length,v[2]-s)
		v4 = (v[0]-s,v[1]-length,v[2]+s)
		v5 = (v[0]+s,v[1]-length,v[2]+s)
		v1 = (v[0],v[1]-(length*2),v[2])
		self.draw_triangle((v2,v4,v))
		self.draw_triangle((v3,v2,v))
		self.draw_triangle((v5,v3,v))
		self.draw_triangle((v4,v5,v))
		self.draw_triangle((v2,v4,v1))
		self.draw_triangle((v3,v2,v1))
		self.draw_triangle((v5,v3,v1))
		self.draw_triangle((v4,v5,v1))
	#	self.draw_square((v2,v3,v5,v4))

	rv = []
	def random_generator(self):	
		for i in range(100):
			self.rv.append((random.randint(-10,10),random.randint(-100,100),random.randint(-10,10)))

	def draw_scene(self):
		
		glClearColor(0.0, 0.0, 0.0, 0.0 )
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.Yrot += 10
		self.draw_diamond((0,1,0))
		for i in range(100):
			self.draw_diamond(self.rv[i])

	
c = Cyclone()
c.main()
