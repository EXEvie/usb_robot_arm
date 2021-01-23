#import the USB and Time librarys into Python
import usb.core, usb.util, time
 
#Shoulder/elbow start angle = 40
#0.5 seconds of shoulder/elbow movement is 10 degrees
#Base/shoulder start angle = 90
#0.5 seconds of base/shoulder movement is 10 degrees

def ConnectArm():
    #Allocate the name 'RoboArm' to the USB device
    RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0001)
    #RoboArm.set_configuration()
    
    #Check if the arm is detected and warn if not
    if RoboArm is None:
        raise ValueError("Arm not found")
    return RoboArm
 
#Create a variable for duration
#Duration=1
 
#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd,RoboArm):
    #Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    
def MoveJoints(Duration,commands,ini,RoboArm): #pass commands as list
    ArmCmd = [0,0,0]
    base_shoulder_angle = ini[2]
    shoulder_elbow_angle = ini[3]
    for command in commands:
        if command == shoulder_in:
            base_shoulder_angle = ini[2] - Duration #creating new location values to be written to ini file
        if command == shoulder_out:
            base_shoulder_angle = ini[2] + Duration
        if command == elbow_up:
            shoulder_elbow_angle = ini[3] + Duration
        if command == elbow_down:
            shoulder_elbow_angle = ini[3] - Duration
        for instruction in xrange(0,len(command)):
            ArmCmd[instruction] += command[instruction]
        #direction = 1-direction #Changes from inward to outward, and vice-versa
    MoveArm(Duration,ArmCmd,RoboArm)
    if base_shoulder_angle == shoulder_elbow_angle == 0:
        ini = [1,1,base_shoulder_angle,shoulder_elbow_angle,ini[4]]
    else:
        ini = [0,1,base_shoulder_angle,shoulder_elbow_angle,ini[4]]
    return [ini[0],ini[1],ini[2],ini[3],ini[4]]
    
#Note that the below can be summed to move multiple motors at once
light_on = [0,0,1]
light_off = [0,0,0]
grip_close = [1,0,0]
grip_open = [2,0,0]
shoulder_in = [64,0,0]
shoulder_out = [128,0,0]  
elbow_down = [16,0,0]
elbow_up = [32,0,0]
wrist_up = [4,0,0]
wrist_down = [8,0,0]  
base_clock = [0,1,0]
base_anti = [0,2,0]
stop = [0,0,0]

if __name__ == "__Main__":
    RoboArm = ConnectArm()
    MoveArm(0.5, grip_close, RoboArm)
