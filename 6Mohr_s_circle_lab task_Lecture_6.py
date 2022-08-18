#Importing the necessary libraries
import numpy as np
from pylab import *
from numpy.linalg import eig
from numpy.linalg.linalg import eigvals
import matplotlib.pyplot as plt
tensor=np.array([[90,0,0], [0,96,0], [0,0,-50]])
class StressTensorValues:
    def __init__(self,**kywrg):##class for geting the stress values and inert them in the program
        self.tensor=tensor
        self.principleValues=np.sort(np.hstack([eigvals(tensor)]))
class getStressVectors(StressTensorValues):##this class will get each different stress vector alone Sx, Sy,Sz 
    def __init__(self) :
        super().__init__()
        self.tensor=tensor
        self.StressVector1 =np.hstack([tensor[0:,0]])
        self.StressVector2 =np.array(tensor[0:,1])
        self.StressVector3 =np.array(tensor[0:,2])
    def prints(self):###this function will just print the valuse of the stress vectors if the user need them
        print(self.StressVector1,self.StressVector2,self.StressVector3)
class tuplesOfStresses(getStressVectors):###this will return the stress vectors in terms of tuples (x,y)
    def __init__(self):
        super().__init__()
        self.tuple1=(self.StressVector1[0], self.StressVector1[2])#Sx tuples
        self.tuple2=(self.StressVector2[1], self.StressVector2[0])#Sy tuples
        self.tuple3=(self.StressVector3[0], self.StressVector3[2])#Sz tuples
    def printThem(self):
        print(self.tuple1,self.tuple2,self.tuple3)
class getRadiusOfTheCircle(tuplesOfStresses):# this class will calculate raduis of the 3d mohr's circles
    def __init__(self):
        super().__init__()
        self.raduisOfCircle1=(self.principleValues[2]-self.principleValues[0])/2#circel 1
        self.raduisOfCircle2=(self.principleValues[1]-self.principleValues[0])/2#circle2
        self.raduisOfCircle3=(self.principleValues[2]-self.principleValues[1])/2#circecl 3 
    def printing(self):
        print(self.raduisOfCircle1,self.raduisOfCircle2,self.raduisOfCircle3)
class plotingTheCircle(getRadiusOfTheCircle):##in this class we will use plot libarary in pyhton to plot all the three circles we have calculated before
    def __init__(self):
        super().__init__()
    def ploting(self):
        self.circle1=plt.Circle(((self.principleValues[2]+self.principleValues[0])/2,0),self.raduisOfCircle1,color="blue")
        self.circle2=plt.Circle(((self.principleValues[1]+self.principleValues[0])/2,0),self.raduisOfCircle2,color="r")##the format of this function is like this
        self.circle3=plt.Circle(((self.principleValues[2]+self.principleValues[1])/2,0),self.raduisOfCircle3,color="r")#((x,y)center of the circle,raduis of the circle, colors...)
        fig, ax = plt.subplots()
        fig.savefig('plotcircles.png')
        ax.add_patch(self.circle1)
        ax.add_patch(self.circle2)
        ax.add_patch(self.circle3)
        # x axis values
        x = [-150,200]#just to draw an additional axes
        y=[-150,200]
        z=[0,0]
        ax.scatter(x, y)
        plt.plot(x)
        plt.ylabel("Shear stresses",color="black")
        plt.plot(y,z)
        plt.xlabel("Normal stresses",color="black")
        plt.show()
        
        
        

plots=plotingTheCircle()##calling the class which will plot our mohr's circle
plots.ploting()##ploting it
