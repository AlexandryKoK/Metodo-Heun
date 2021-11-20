import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt

#mu = 0.2
#m=0.5
#k=4


g = 9.8

# Definindo as funcoes 
def dx(t,x_0,z_0):
    return z_0

def dz(t,x_0,z_0, mu,m,k):
    return -np.sign(z_0)*mu*9.8 - x_0*k/(m)


#Definindo os valores iniciais
x_0 = 5
z_0 = 0


#Os passos
h = 0.1

# O algoritmo de Heun
def heun(x_0,z_0,h,mu,m,k):
    #print(mu*m*g/(k*5))
    #Fazendo que os valores iniciais sejam substituidos pelos novos calculados do passo i-1 a partir de 2.
    t_0 = 0 # t começa de 0 
    x = x_0
    z = z_0
    #Criando o loop que vai calcular a quantidade de iteracoes;
    for i in range(1,121):
        k_11 = dx(t_0,x,z)
        k_12 = dz(t_0,x,z, mu,m,k)
        k_21 = dx(t_0 + h,x+h*k_11,z+h*k_12)
        k_22 = dz(t_0 + h,x + h*k_11,z + h*k_12, mu,m,k)
        #x = x + h/2*(k_11 + k_21) 
        x = x + h/2*(k_11 + k_21) + mu*m*g/(k)
        z = z + h/2*(k_12 + k_22)
        t_0 = t_0 + h # alterando o valor de t
        plt.grid()
        plt.scatter(t_0, x)
        plt.title("Titulo")
        plt.xlabel("t (s)")
        plt.ylabel("x (m)")
        #Imprimindo os resultados.
        print('(t = %g, x = %g, v = %g)' % (t_0,x,z))
        #plt.scatter(x, z, linestyle='--', marker='o')
    #print('(t = %g, x = %g, v = %g)' % (t_0,x,z))
        #print(z)

#heun(5,0,0.1,0.2,0.5,4)
#heun(5,0,0.1,0.1,0.5,4)
#heun(5,0,0.1,0.2,0.75,4)
#heun(5,0,0.1,0.2,0.5,6)
#heun(5,0,0.1,0.4,0.5,4)
#heun(5,0,0.1,0.2,2,4)
heun(5,0,0.1,0.4,2,2)
plt.show()
