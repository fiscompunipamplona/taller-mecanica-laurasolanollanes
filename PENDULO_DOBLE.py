#Laura Solano y Diego Palacios 

from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint
from vpython import sphere, scene, vector, color, arrow, text, sleep

arrow_size = 0.1

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.03 #Radio de la esfera

def funcion (cond, t, g, l): #Función que devuelve valores de theta y omega(arreglo)
    a1=cond[4]
    b1=cond[5]
    dphi1=cond[1]
    da=(1/2)*(-(cond[5])*cos(cond[0]-cond[2])-((cond[2])**2)*sin(cond[0]-cond[2]))-(g/l)*sin(cond[0])
    dphi2=cond[3]
    db=-(cond[4])*cos(cond[0]-cond[2])+((cond[1])**2)*sin(cond[0]-cond[2])-(g/l)*sin(cond[2])
    return array([dphi1,da,dphi2,db,a1,b1], float)

g = 9.8
l = 0.2

phi1=1.3*pi/2.
a=0.
phi2=0
b=0.
da=0.
db=0.

cont1 = array([phi1,a,phi2,b,da,db])

pasos=5000 #numero de pasos
tin=0.   #tiempo inicial
tfin=12.  #tiempo final
tdif=(tfin-tin)/pasos #un diferencial de tiempo
t=linspace(tin, tfin, pasos) #arreglo de diferencial de tiempo

soluc, outodeint = odeint( funcion, cont1, t, args=(g,l),full_output=True) #Solución de la ecuación diferencial(Parámetros acordes a los definidos en la función) 
#soluc (arreglo de n filas y 2 columnas) es la solución diferencial para cada paso(columnas) de theta y omega


phi_1,aa,phi_2,bb,aaa,bbb = soluc.T #Devuelve la matriz transpuesta (a cada una de las variables de la izquierda, theta y omega, le define el respectivo vector)

scene.range = 0.5 #Tamaño de la ventana de fondo

xp = l*sin(phi1) #Pasa de coordenadas polares a cartesianas
yp = -l*cos(phi1)
zp = 0.

xs=l*(sin(phi1)+sin(phi2))
ys=-l*(cos(phi1)+cos(phi2))
zs=0.

actime= 0.0001 #Tiempo con que se actualiza la posición de la partícula

prtcl=sphere(pos=vector(xp,yp,zp), radius=R, color=color.green) #Define objeto con que se va a trabajar
prtcls=sphere(pos=vector(xs,ys,zs), radius=R, color=color.blue)

contime=0 #Contador que se mueve en el espacio temporal en el que se resolvió la ecuación diferencial
runtime=0  #Tiempo en el que se ejecuta la animación

while runtime < tfin: #ANIMACIÓN
    prtcl.pos = vector( l*sin(phi_1[contime]), -l*cos(phi_1[contime]), zp )
    prtcls.pos= vector( l*(sin(phi_1[contime])+sin(phi_2[contime])), -l*(cos(phi_1[contime])+cos(phi_2[contime])), zs )
    runtime += tdif
    sleep(actime)
    runtime += 1