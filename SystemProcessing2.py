import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import serial


def polarCart(r, theta, phi):
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    return(x,y,z)
    

def lidarData(i):
    #Initialize serial connection
    ser = serial.Serial('COM4', baudrate = 9600, timeout=3)
    
    #Set the number of data points
    rowPoints =  5
    numberRows = 6
    totalPoints = rowPoints*numberRows
    
    #Data arrays
    r = np.ones(totalPoints)
    phi = np.ones(totalPoints)
    theta = np.ones(totalPoints)
    
    #Get lidar data
    data = []
    while 1:
        varRead = ser.readline().decode('utf-8').replace('\r','').replace('\n','').replace('\x00','')
        if varRead == "b":
            break
        data.append(varRead)
    data = [ x for x in data if x is not "" ]
    data = list(map(int,data))

    
    #Get positional data
    r = data
    for i in range(0,totalPoints,rowPoints):
        for j in range(0,rowPoints):
            phi[i+j]   = (np.pi/2) * i/totalPoints
            theta[i+j] = (2*np.pi) * j/rowPoints
    
    #Convcert to Cartisian
    x, y, z = polarCart(r, theta, phi)
    
    #Draw new plot and set plot paramaters
    ax.clear()
    plt.axis('off')
    plt.xlim((-500,500))
    plt.ylim((-500,500))
    ax.set_zlim(0, 500)
    ax.scatter(x,y,z)
    
    
#Main
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, lidarData, interval=1000)
plt.show()