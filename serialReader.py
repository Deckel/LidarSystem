import serial
import time

ser = serial.Serial('COM4', baudrate = 9600, timeout=3)
a = []
data = []


'''
for i in range(1,10):
    a.append(ser.readline().decode('utf-8').replace('\r','').replace('\n','').replace('\x00',''))
    
print(a)
    

while True:
    b = str(ser.readline())
    if b == "b's\\r\\n'":
        break
'''
time.sleep(1)

while 1:
    data = []
    #ser.write('a\n'.encode('utf-8'))
    while 1:
        varRead = ser.readline().decode('utf-8').replace('\r','').replace('\n','').replace('\x00','')
       
        if varRead == "b":
            break
        data.append(varRead)
    
    data = [ x for x in data if x is not "" ]
    print(data)
    print(len(data))