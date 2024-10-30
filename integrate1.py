'''
Created on Jun 2, 2021

@author: abc
'''
from sympy import *
from sympy.integrals.integrals import integrate
from sympy.core.numbers import pi
from sympy.codegen.ast import integer

x,y,z = symbols('x y z')
a,b = symbols('a b')
r = symbols('r')
alpha, beta, gamma, delta = symbols('alpha, beta, gamma, delta')
epsilon, zeta, eta, theta = symbols('epsilon, zeta, eta, theta')
iota, kappa, lamda, mu = symbols('iota, kappa, lamda, mu')
nu, xi, omicron = symbols('nu, xi, omicron')
rho, sigma, tau, upsilon = symbols('rho, sigma, tau, upsilon')
phi, chi, psi, omega = symbols('phi, chi, psi, omega')

print(integrate((x-x**2),(x,0,1))) #1/6


print(integrate(-sin(x)**2 , (x, 0,2*pi ))) #20240407

print(integrate((x*y),(y,1,x),(x,1,2)))#20240408  9/8
print(integrate((x*y),(x,y,2),(y,1,2)))#20240408  9/8
#print(integrate((x*y),(y,1,x)))
print(integrate(integrate((x*y),(y,1,x)),(x,1,2)))#20240408 #二重积分 #9/8

print(integrate(integrate((y*sqrt(1+x**2-y**2)),(y,x,1)),(x,-1,1))) #1/2
print(integrate((r),(theta,0,2*pi))) #圆的周长
print(integrate((r),(r,0,a),(phi,0,2*pi))) #20240409 园的面积
#print(integrate(integrate((y*sqrt(1+x**2-y**2)),(x,-1,y)),(y,-1,1)))
print(integrate(x,(z,0,1-x-2*y),(y,0,(1-x)/2),(x,0,1))) #三重积分
print(integrate((r**2*sin(phi)),(r,0,a),(phi,0,pi),(theta,0,2*pi))) #20240409 球的体积
print(integrate(integrate(integrate((r**2*sin(phi)),(r,0,a)),(phi,0,pi)),(theta,0,2*pi)))

tiji= integrate((r**2*sin(phi)),(r,0,a),(phi,0,pi),(theta,0,2*pi))
print(latex(tiji))
'''
print(integrate(sqrt(1-cos(x))))
print (integrate(pi*(b**2/a**2)*(a**2-x**2),(x,-a,a)))
print (integrate(pi*(r**2-x**2),(x,-r,r)))

#print (integrate((sqrt(r**2-x**2)),(x,0,r)))

print (integrate((sqrt(5**2-x**2)),(x,0,5)))
print (integrate((sin(x)**2),(x,0,pi/2)))
print (integrate(a,(x)))
print (integrate((sqrt(100**2-x**2)),(x,0,100)))
print(integrate(sin(x)/x,(x,-oo,+oo)))

'''