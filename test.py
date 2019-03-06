import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as random
from mpl_toolkits.mplot3d import Axes3D
import serial
import time

random.seed(56)

#Cartesian to Polar coordinates
def cartPolar(x, y, z):
    r     = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan(y/x)
    phi   = np.arccos(z/r)
    return(r, theta, phi )
#Polar to Cartisian coordinates
def polarCart(r, theta, phi):
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    return(x,y,z)
#Initialize data
def random_data(i): 
 
    ser = serial.Serial('COM4', baudrate = 9600, timeout = 1)
    #Number of angles measurements are taken
    rowPoints =  5
    #Number of LIDAR rangefinders
    numberRows = 5
    
    totalPoints = rowPoints*numberRows
    
    #Data set length n 
    r = np.ones(totalPoints-rowPoints)
    theta = np.ones(totalPoints-rowPoints)
    phi = np.ones(totalPoints-rowPoints)
    
    #This method should be improved? 
    for i in range(0,totalPoints-rowPoints,rowPoints):
        for j in range(0,rowPoints):
            theta[i+j] = (2*np.pi) * j/rowPoints
            phi[i+j]   = (np.pi/2) * i/totalPoints
                       
            #Lidar entry
                        
            time.sleep(2)
            ser.write('a'.encode())
            time.sleep(0.6)
            dataPoint = ser.readline().decode("utf-8")
            
            dataPoint = dataPoint.strip('\n')
            
            dataPoint = int(dataPoint)
            
            
            r[i+j] += dataPoint
            print(r[i+j])
           
    #Removing duplicate points for last row
    r     = np.delete(r,list(np.arange(0,rowPoints-1)), axis = 0)
    theta = np.delete(theta,list(np.arange(0,rowPoints-1)), axis = 0)
    phi   = np.delete(phi,list(np.arange(0,rowPoints-1)))
  
    #Convert spherical polar coordinates into cartesian
    x, y, z = polarCart(r, theta, phi)
   
    #Draw new plot and set plot paramaters
    ax.clear()
    plt.axis('off')
    plt.xlim((-500,500))
    plt.ylim((-500,500))
    ax.set_zlim(0, 500)
    #ax.view_init(elev=0, azim=0)
    #ax.plot_trisurf(x,y,z, alpha=0.9)
    ax.scatter(x,y,z)
    time.sleep(100000)
    
#Main
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, random_data, interval=1000)
plt.show()