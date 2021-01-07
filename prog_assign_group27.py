import numpy as np
import matplotlib.pyplot as plt
from math import *
#190110056 190110098 190110104
A=input("Please Enter Temperature(Standard=298K) Here:-")
T=float(A)
#deltaG0=deltaH0-T*deltaS0
#SO2 + NiO + 0.5O2 = NiSO4        K1
#NiS + 2O2 = NiSO4                K2
#NiS + 1.5O2 = NiO + SO2          K3
#Ni3S2 + 3.5O2 = 3NiO + 2SO2      K4
#Ni3S2 + SO2 = 3NiS + O2          K5
#Ni + 0.5O2 = NiO                 K6
#3Ni + 2SO2 = Ni3S2 + 2O2         K7
#deltaG0= -RTln(K)
R=8.314
#From Literature we get:-
deltaG01=-872907.92-97.07*T-(-239743.2-37.99072*T)-(-296829.696-T*248.1112)-0.5*(-T*205.028552)
deltaG02=-872907.92-97.07*T-(-82006.4-T*52.96944)-2*(-T*205.028552)
deltaG03=-239743.2-37.99072*T-296829.696-T*248.1112-(-82006.4-T*52.96944)-1.5*(-T*205.028552)
deltaG04=3*(-239743.2-37.99072*T)+2*(-296829.696-T*248.1112)-(-202924-T*133.888)-3.5*(-T*205.028552)
deltaG05=3*(-82006.4-T*52.96944)+(-T*205.028552)-(-202924-T*133.888)-(-296829.696-T*248.1112)
deltaG06=(-239743.2-37.99072*T)-0.5*(-T*205.028552)-(-T*29.87376)
deltaG07=-202924-T*133.888+2*(-T*205.028552)-3*(-T*29.87376)-2*(-296829.696-T*248.1112)
K1=exp(-deltaG01/(R*T))
K2=exp(-deltaG02/(R*T))
K3=exp(-deltaG03/(R*T))
K4=exp(-deltaG04/(R*T))
K5=exp(-deltaG05/(R*T))
K6=exp(-deltaG06/(R*T))
K7=exp(-deltaG07/(R*T))
logpo21=np.linspace(-0.5*log10(K1)-0.5*log10(K3),100,100)
logpso21=-0.5*logpo21-log10(K1)
plt.plot(logpo21,logpso21)
logpo23=np.linspace(-((4/3)*log10(K5)+0.5*(4/3)*log10(K4)),-0.5*log10(K1)-0.5*log10(K3),100)
logpso23=1.5*logpo23+log10(K3)
plt.plot(logpo23,logpso23)
logpo24=np.linspace(-2*log10(K6),-((4/3)*log10(K5)+0.5*(4/3)*log10(K4)),100)
logpso24=1.75*logpo24+0.5*log10(K4)
plt.plot(logpo24,logpso24)
logpo25=np.linspace(-150,-((4/3)*log10(K5)+0.5*(4/3)*log10(K4)),100)
logpso25=logpo25-log10(K5)
plt.plot(logpo25,logpso25)
logpo27=np.linspace(-150,-2*log10(K6),100)
logpso27=logpo27-0.5*log10(K7)
plt.plot(logpo27,logpso27)
plt.vlines(x=-0.5*log10(K2), ymin=-0.75*log10(K1)+0.25*log10(K3), ymax=200)
plt.vlines(x=-2*log10(K6),ymin=-150,ymax=-2*log10(K6)-0.5*log10(K7))
plt.xlabel("log pO2")
plt.ylabel("log pSO2")
plt.ylim((-150,100))
plt.title("Predominance Diagram of Ni-S-O system")
plt.legend(["NiO-NiSO4","NiS-NiO","Ni3S2-NiO","Ni3S2-NiS","Ni-Ni3S2","Ni-NiO","NiS-NiSO4"],loc='upper right')
plt.annotate("A",(-2*log10(K6),-150),textcoords="offset points",xytext=(1,1))
plt.annotate("B",(-2*log10(K6),-2*log10(K6)-0.5*log10(K7)),textcoords="offset points",xytext=(3,-2))
plt.annotate("C",(-((4/3)*log10(K5)+0.5*(4/3)*log10(K4)),-((4/3)*log10(K5)+0.5*(4/3)*log10(K4))-log10(K5)),textcoords="offset points",xytext=(-3,-12))
plt.annotate("D",(-0.5*log10(K2),-0.75*log10(K1)+0.25*log10(K3)),textcoords="offset points",xytext=(2,1))
plt.annotate("E",(-150,-150-0.5*log10(K7)),textcoords="offset points",xytext=(0,-9))
plt.annotate("F",(-150,-150-log10(K5)),textcoords="offset points",xytext=(-1,6))
plt.annotate("G",(-0.5*log10(K2),100),textcoords="offset points",xytext=(2,-9))
plt.annotate("H",(100,-0.5*100-log10(K1)),textcoords="offset points",xytext=(-2,3))
plt.text((-0.5*log10(K2)+100)/2,-(-0.5*100-log10(K1)+-0.75*log10(K1)+0.25*log10(K3))/2,'NiSO4')
plt.text((-2*log10(K6)-150)/2,-(-0.5*100-log10(K1)+-0.75*log10(K1)+0.25*log10(K3))/2,'NiS')
plt.text(-0.5*log10(K2),(-2*150-2*log10(K6)-0.5*log10(K7))/3,'NiO')
plt.text((-2*log10(K6)-150)/2,(-2*150-2*log10(K6)-0.5*log10(K7))/3,'Ni')
plt.text(-160,-150-0.5*log10(K7)-1.5,'Ni3S2',rotation=35)
plt.show()

