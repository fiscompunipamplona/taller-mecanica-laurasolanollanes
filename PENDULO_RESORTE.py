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

R = 0.03

def funcion (cond, t, g ): # funcion definida para los valores de theta y omega
    dthe = cond[1]
    dl=cond[3]
    dome=(-1/cond[2])*(2*cond[3]*cond[1])-g*sin(cond[0])
    dr=(cond[2])*((cond[1])**2)-((k/m)*(cond[2])-b)+g*cos(cond[0])
    return array([dthe, dome, dl, dr], float)


g = 9.81
b=0.5
k=5
m=1

thes=90*pi/180 #valores iniciales para theta y omega
l=0.1
omes= 0.
r=0.2

initcond = array([thes,omes,l,r], float)#arreglos de las condiciones iniciales

pasos = 1000 #numero de pasos
tin = 0. #tiempo inicial
tfin = 15.#tiempo final
tdif=(tfin-tin)/pasos #diferencial de tiempo
t=linspace(tin, tfin, pasos)#arreglo de diferencial de tiempo

soluc, outodeint = odeint( funcion, initcond, t, args = (g,), full_output=True) #solucion de la ecuacion diferencial (parametros acordes a los definidos en la funcion)

theta, omega, ll, rr = soluc.T # solucion para cada paso de theta y omega

scene.range = 0.2 # tamaño de la ventana de fondo

xp = l*sin(thes) #pasa de coordenadas polares a cartesinas
yp = -l*cos(thes)
zp = 0.

actime = 0.0001 # tiempon con el que se utiliza la posicion de la particula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.red) #define objeto con que se va a trabajar

contime = 0 #es un contador que se mueve ene el espacio temporal en donde se resolvio la ecuacion deferencial
runtime= 0 #tiempo en el q se ejecuta la animacion

while runtime < tfin: #animacion 
    sleep(actime) 
    prtcl.pos = vector( l*sin(theta[contime]), -l*cos(theta[contime]), zp )
    runtime += tdif
    contime += 1
