from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
from helipoints import *
from const import *
from PIL.Image import open
from math import *
x = []

name = "Pattys"
center = [0.2,1,3.1]
up = [0,1,0]
look = [0,0,0]

closevieweye = [0,0.07,-0.2]
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
		#glutKeyboardFunc(self.keypressed)
    		self.LoadTextures()
   		glEnable(GL_TEXTURE_2D)
    		glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    		glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
    


	
 	def LoadTextures(self):
    	#global texture
    		image = open("pokeball.jpg")
    
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


	def camera(self,center=[0,0,1],look=[0,0.,-10],up=[0,1,0]):
		glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
		gluPerspective(40.,1.,0.2,40.)
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
		self.camera()
		glutDisplayFunc(self.display)
		glutMainLoop()

	Yrot, Xrot,Scale,erot1,Zrot,srot,drot = [0,0,0.1,0,0,0,0]
	lats = 0
	longs = 0
	d = 1
	def display(self):
		self.draw_scene()
		self.camera()
		glutSwapBuffers()
		glutPostRedisplay()
 
	rv = []
	def random_generator(self):	
		for i in range(100):
			self.rv.append((random.randint(-10,10),random.randint(-100,100),random.randint(-10,10)))


	def draw_scene(self):
				
		glClearColor(0.0, 0.0, 0.0, 0.0 )
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.Yrot += 0.3
		
		self.draw_sphere()
		
	
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

	def draw_triangle(self,v):

                color = (random.random(),random.random(),random.random())
                glBegin(GL_TRIANGLES)
		glColor3f(color[0],color[1],color[2])
                glVertex3f(v[0][0],v[0][1],v[0][2])
                glVertex3f(v[1][0],v[1][1],v[1][2])
                glVertex3f(v[2][0],v[2][1],v[2][2])
                

                glEnd()



	def draw_diamond(self,v):
		s = 1.0
		length = 2.0
		v2 = (v[0]-s,v[1]-length,v[2]-s)
		v3 = (v[0]+s,v[1]-length,v[2]-s)
		v4 = (v[0]-s,v[1]-length,v[2]+s)
		v5 = (v[0]+s,v[1]-length,v[2]+s)
		v1 = (v[0],v[1]-(length*2),v[2])
		glPushMatrix()
#		glRotatef(self.drot,0,1,0)
		glTranslatef(15,5,0)
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
	
	def cube(self):
		glTranslate(0,0,-1)
		glBegin(GL_QUADS)                # Start Drawing The Cube
    
    # Front Face (note that the texture's corners have to match the quad's corners)
   		glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
   		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad
    	  	glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad
    
   
		glEnd()                # Done Drawing The Cube
	x = 0
	def draw_sphere(self):
		global d 	
	
		self.lats = 20
		self.longs = 20
		s= 0;
		t =0;
		self.x += 0.01
		if self.x > 2:
			self.x = 0.01 
		for i  in range(0, self.lats + 1):
            		lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            		z0 = sin(lat0)
            		zr0 = cos(lat0)

            		lat1 = pi * (-0.5 + float(float(i) / float(self.lats)))
            		z1 = sin(lat1)
            		zr1 = cos(lat1)
			glPushMatrix()
			glRotatef(180,0,0,1)
			glRotatef(90,1,0,0)
            # Use Quad strips to draw the sphere
            		glBegin(GL_QUAD_STRIP)
			t0 = (lat0 + (pi/2))/pi 
			t1 = (lat1 + (pi/2))/ pi
			
            		for j in range(0, self.longs + 1):
				
                		lng = 2 * pi * float(float(j - 1) / float(self.longs))+1
                		x = cos(lng)
                		y = sin(lng)
				if d == 1:
			 		s = (((lng +  pi)/pi))
				else:
					s = (((lng / self.x)/pi))
				
				x += 0.01
				
				#glNormal3f(x * zr0, y * zr0, z0)
				glTexCoord2f(s ,t0)
				glVertex3f(x * zr0, y * zr0, z0)
                		glTexCoord2f(s,t1)
                		glVertex3f(x * zr1, y * zr1, z1)

            		glEnd()   
			glPopMatrix()	


d = 1

def Createmenu():
		menu = glutCreateMenu(processMenuEvents)
		glutAddMenuEntry("Disable Texture",1)
		glutAddMenuEntry("Enable Texture",2)
		glutAddMenuEntry("Enable Distortion",3)
		glutAddMenuEntry("Disable Distortion",4)
		glutAttachMenu(GLUT_RIGHT_BUTTON)

def processMenuEvents(option):
		global d 
		if option == 1:
			glDisable(GL_TEXTURE_2D)
		if option == 2:
			glEnable(GL_TEXTURE_2D)
		if option == 3:
			d = 0
		if option == 4:
			d = 1
		
		return 1 
		
c = Cyclone()
c.main()
