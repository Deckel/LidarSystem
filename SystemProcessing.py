import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import serial
import time


def polarCart(r, theta, phi):
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos((np.pi/2) - phi)
    return(x,y,z)
    

def lidarData(i):
    #Globals
    global rowPoints
    global numberRows
    global totalPoints
    
    #Data arrays
    global r
    phi = np.ones(totalPoints)
    theta = np.ones(totalPoints)
    global data
    
    #Get lidar data
    timeout = time.time() + 1
    while time.time() < timeout:
        if ser.inWaiting() > 0:
            varRead = ser.readline().decode('utf-8').replace('\r','').replace('\n','').replace('\x00','')
            if varRead == "b":
                break
            data.append(varRead)
        data = [ x for x in data if x is not "" ]
    try:
        data = list(map(int,data))
        if(len(data)==len(r)):
            r = data
    except:
        print("Data has been currupted returning to last data set")
    
    #Get positional data
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
    #ax.autoscale_view()
    
    
#Main
rowPoints =  20
numberRows = 8
totalPoints = rowPoints*numberRows
data = []
r = np.ones(totalPoints)*1000
#Initialize serial connection
ser = serial.Serial('COM4', baudrate = 9600, timeout=3)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig, lidarData, interval=10000)
plt.show()