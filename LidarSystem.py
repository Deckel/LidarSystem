import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as random
from mpl_toolkits.mplot3d import Axes3D

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
    #Number of angles measurements are taken
    rowPoints = 10
    #Number of LIDAR rangefinders
    numberRows = 5
    totalPoints = rowPoints*numberRows
    #Data set length n 
    r = np.ones(totalPoints)
    theta = np.ones(totalPoints)
    phi = np.ones(totalPoints)
    #This method should be improved? 
    for i in range(0,totalPoints,rowPoints):
        for j in range(0,rowPoints):
            theta[i+j] = 2*np.pi/rowPoints * j
            phi[i+j]   = ((np.pi/2)/(totalPoints/rowPoints)) * i/rowPoints
           
            #Lidar entry (random data set for now)
            r[i+j] += random.random()*0.1 

    #Removing duplicate points for last row
    r[totalPoints-rowPoints:totalPoints] = r[totalPoints-1]
    #Convert spherical polar coordinates into cartesian
    x, y, z = polarCart(r, theta, phi)
    #Draw new plot and set plot paramaters
    ax.clear()
    plt.axis('off')
    plt.xlim((-1.5,1.5))
    plt.ylim((-1.5,1.5))
    ax.set_zlim(0, 1.5)
    ax.plot_trisurf(x,y,z)
    #ax.scatter(x,y,z)
    
#Main
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, random_data, interval=100)
plt.show()


