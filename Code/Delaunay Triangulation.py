from __future__ import print_function
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import random
from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Triangulation_2 import Delaunay_triangulation_2


points=[]
points.append( Point_2(1,0) ) #0
points.append( Point_2(2,3) ) #1
points.append( Point_2(-2,2) ) #2
points.append( Point_2(0,-1) ) #3
points.append( Point_2(-2,-2) ) #4


T=Delaunay_triangulation_2()
T.insert(points)

map={}
p=0

#untuk melakukan maping titik dengan urutan titik
#finite vertices itu titik yang ada
for i in T.finite_vertices():
   map[i]=p
   p=p+1

#finite faces itu suatu bidang
for i in T.finite_faces():
   print ("urutan titik : ", map[i.vertex(0)], map[i.vertex(1)], map[i.vertex(2)])
   print ("titik ke ", map[i.vertex(0)],": (",i.vertex(0).point(),")")
   print ("titik ke ", map[i.vertex(1)],": (",i.vertex(1).point(),")")
   print ("titik ke ", map[i.vertex(2)],": (",i.vertex(2).point(),")")
   print ("============================")

def display(): 
   glClear (GL_COLOR_BUFFER_BIT)#utk clear semua pixel

   glBegin(GL_TRIANGLES)#untuk membuat segitiga
   for c in T.finite_faces():
        glColor3f (random(), random(), random())#warna segitiga random
        glVertex3f(c.vertex(0).point().x() ,c.vertex(0).point().y(), 0.0 )
        glVertex3f(c.vertex(1).point().x() ,c.vertex(1).point().y(), 0.0 )
        glVertex3f(c.vertex(2).point().x() ,c.vertex(2).point().y(), 0.0 )

   glEnd()

   glFlush ();

def init():
   glClearColor (1.0, 1.0, 1.0, 0.0)#untuk clearing color
   glMatrixMode(GL_PROJECTION)#untuk initialize viewing values
   glLoadIdentity()
   glOrtho(-8.0, 8.0, -8.0, 8.0, -1.0, 1.0)



glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)#untuk ukuran window
glutInitWindowPosition(500, 150)#untuk position window
glutCreateWindow("Delaunay triangulation Nomor 3 (Abigail Vania 2101637005)")
init()
glutDisplayFunc(display)
glutMainLoop()


