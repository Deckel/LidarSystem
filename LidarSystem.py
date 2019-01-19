import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as random

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
    #Define number of points and points in a row
    #totalPoints needs to be a factor of rowPoints!!!!
    totalPoints = 200
    rowPoints = 20
    #Data set length n 
    r = np.ones(totalPoints)
    theta = np.ones(totalPoints)
    phi = np.ones(totalPoints)
    #This method should be improved? 
    for i in range(0,totalPoints,rowPoints):
        for j in range(0,rowPoints):
            theta[i+j] = 2*np.pi/rowPoints * j
            phi[i+j]   = ((np.pi/2)/(totalPoints/rowPoints)) *i/rowPoints
            r[i+j] += random.random()*0.1      
    #Convert spherical polar coordinates into cartesian
    x, y, z = polarCart(r, theta, phi)
    #Draw new plot
    ax.clear()
    plt.axis('off')
    ax.plot_trisurf(x,y,z)
    #ax.scatter(x,y,z)
    
#main
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, random_data, interval=1000)
plt.show()


