from CGAL.CGAL_Kernel import Point_2
from CGAL.CGAL_Kernel import Segment_2
from CGAL.CGAL_Kernel import intersection
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

segments=[]
segments.append(Segment_2(Point_2(0,1), Point_2(1,0)))
segments.append(Segment_2(Point_2(1,1), Point_2(2,2)))
segments.append(Segment_2(Point_2(0,0), Point_2(1,2)))
segments.append(Segment_2(Point_2(0,0), Point_2(2,1)))
segments.append(Segment_2(Point_2(-1,0), Point_2(-1,2)))
segments.append(Segment_2(Point_2(0,-1), Point_2(2,-1)))

head = [Point_2(0,1), Point_2(1,1), Point_2(0,0), Point_2(0,0), Point_2(-1,0), Point_2(0,-1)]
tail = [Point_2(1,0), Point_2(2,2), Point_2(1,2), Point_2(2,1), Point_2(-1,2), Point_2(2,-1)]

#point_2 untuk 2 dimensi dan segment_2 untuk 2 dimensi juga

intersectionPoint=[]

for i in range (len(segments)):
    for j in range (i+1,len(segments)):
        inter = intersection(segments[i], segments[j]) #untuk cek ada intersection atau engga
        if inter.is_Point_2()==True:
            k=Point_2(inter.get_Point_2().x(),inter.get_Point_2().y())
            #karena kalau bertemu sama-sama diujung bukan intersection
            if k in head:
                if head[i]==head[j] or tail[i]==head[j] or head[i]==tail[j]:
                    continue
            elif k in tail:
                if tail[i]==tail[j]or tail[i]==head[j] or head[i]==tail[j]:
                    continue    
            else:
                print ('Titik potong segment ',i+1,'dengan ',j+1,': ','(',inter.get_Point_2().x(),',',inter.get_Point_2().y(),')')
                intersectionPoint.append(Point_2(inter.get_Point_2().x(),inter.get_Point_2().y()))

def display():
   glClear (GL_COLOR_BUFFER_BIT)#utk clear semua pixel
   glBegin(GL_LINES) #untuk membuat garis sumbu x dan y dari x=-2 sampai x=5 dan y=-2 sampai y=5
   glColor3f (0.0, 0.0, 0.0)#warna garis sumbu x dan y berwarna hitam
   glVertex3f (-2.0, 0.0, 0.0)
   glVertex3f (5.0, 0.0, 0.0)
   glVertex3f (0.0, -2.0, 0.0)
   glVertex3f (0.0, 5.0, 0.0)
   glEnd()
   
   glColor3f (0.4, 0.3, 0.7)#warna garis
   for i in range(len(head)):
       glBegin(GL_LINES)#untuk membuat garis
       glVertex3f (head[i].x(), head[i].y(), 0.0)
       glVertex3f (tail[i].x(), tail[i].y(), 0.0)
       glEnd()

   glColor3f(0.5, 0.3, 0.2)#warna titik pada intersection
   glPointSize(7.0)#ukuran titik
   for i in range(len(intersectionPoint)):
       glBegin(GL_POINTS)
       glVertex3f(intersectionPoint[i].x(), intersectionPoint[i].y(), 0.0)
       glEnd()
   glFlush ();

def init():
   glClearColor (1.0, 1.0, 1.0, 0.0)#untuk clearing color
   glMatrixMode(GL_PROJECTION)#untuk initialize viewing values
   glLoadIdentity()
   glOrtho(-2.0,5.0, -2.0, 3.0, -1.0, 1.0)       

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)#untuk ukuran window
glutInitWindowPosition(500, 150)#untuk position window
glutCreateWindow(" Brute Force algorithm Intersection Nomor 2 (Abigail Vania 2101637005)")
init()
glutDisplayFunc(display)
glutMainLoop()

