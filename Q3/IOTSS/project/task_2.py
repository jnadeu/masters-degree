import serial

# File 'rep_0.txt' does NOT contain valid data
# Move 1 -> Wave hello
# Move 2 -> Cercle to the left
# Move 3 -> Other
arduino = serial.Serial(port='/dev/ttyACM0',   baudrate=115200, timeout=.1)
x = 0
rep = 30 # number of repetitions 

while x <= rep:
    data = arduino.readline().decode().strip()
    if data.rfind("giro:") >= 0:
        data = data.strip("giro:")
        f = open("rep_"+str(x)+".txt", "a")
        f.write(data+"\n")
        f.close()
        print(data)

    elif data.isnumeric():
        if data == "1":
            f = open("rep_"+str(x)+".txt", "a")
            f.write("\n")
            f.close()
            x+=1
        print(data)
    
