import numpy as np
from math import exp
import matplotlib.pyplot as plt

N=int(input("saisir le nombre de pas: "))

T=int(input("saisir le temps final: "))

h=T/N

r=0.05

t=np.zeros(N+1)
y=np.zeros(N+1)
A=np.zeros(N+1)


y0=int(input("saisir la condition initiale y0: "))


#initialisation
y[0]=y0
t[0]=0
A[0]=y0


for n in range(N) :
  t[n+1]=t[n] + h
  
#differences finies
for n in range(1,N+1) :
    y[n]=(1+h*r)**n *y[0]
    
# affichage
plt.title("differences finies")
plt.plot(t, y, label="Intérêts composé")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()

#Méthode de Cranck-Nicholson
for n in range(1,N+1) :
    A[n]=((1+h*r/2)/(1-h*r/2))**n *A[0]



# affichage
plt.title("Méthode de Cranck-Nicholson")
plt.plot(t, y, label="Intérêts composé")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.show()
