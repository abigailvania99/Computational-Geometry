from CGAL.CGAL_Kernel import Point_2
from CGAL import CGAL_Convex_hull_2
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

Titik = []
Titik.append(Point_2(0,0))
Titik.append(Point_2(0,1))
Titik.append(Point_2(1,0))
Titik.append(Point_2(1,1))
Titik.append(Point_2(1,2))
Titik.append(Point_2(2,0))
Titik.append(Point_2(2,1))
Titik.append(Point_2(2,2))
Titik.append(Point_2(3,0))
Titik.append(Point_2(3,1))
Titik.append(Point_2(4,0))


hasil = []
CGAL_Convex_hull_2.ch_graham_andrew(Titik,hasil)

print('Titik yang convexhull :')
for i in hasil:
   print ('(',i.x(),',',i.y(),')')

def display():
   glClear (GL_COLOR_BUFFER_BIT)#utk clear semua pixel

   glBegin(GL_LINES) #untuk membuat garis sumbu x dan y dari x=-1 sampai x=5 dan y=-1 sampai y=5
   glColor3f (0.0, 0.0, 0.0)#warna garis sumbu x dan y berwarna hitam
   glVertex3f (-1.0, 0.0, 0.0)
   glVertex3f (5.0, 0.0, 0.0)
   glVertex3f (0.0, -1.0, 0.0)
   glVertex3f (0.0, 5.0, 0.0)
   glEnd()
   
   glPointSize(6.0) #untuk ukuran titik yang telah diinput
   glBegin(GL_POINTS)
   glColor3f (0.4, 0.2, 0.3)#warna point
   for p in Titik :
       glVertex3f (p.x(), p.y(), 0.0)
   glEnd()


   glBegin(GL_LINE_LOOP)#menghubungkan garis tertutup dari titik yang diperoleh dari convex hull
   glColor3f (0.0, 1.0, 0.0)#warna garis hijau
   for p in hasil:
       glVertex3f (p.x(), p.y(), 0.0)
   glEnd()
   
   glFlush ();

def init():
	
   glClearColor (1.0, 1.0, 1.0, 0.0)#untuk clearing color

   glMatrixMode(GL_PROJECTION)#untuk initialize viewing values
   glLoadIdentity()
   glOrtho(-1.0, 5.0, -1.0, 5.0, -1.0, 1.0)



glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)#untuk ukuran window
glutInitWindowPosition(500, 150)#untuk position window
glutCreateWindow("Convex-Hull nomor 1 (Abigail Vania-2101637005)")
init()
glutDisplayFunc(display)
glutMainLoop()
