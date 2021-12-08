#program to take assembled rcl code and simulate it
#program receives pipe from rcl assembler like this
#    python "rcl assembler.py" <input path> --py | python "rcl simulator.py"


import sys
import time
import keyboard



def Error(xMsg):
    print(xMsg)
    sys.exit(1)


def Simulate(xRaw):
    xProg = eval(xRaw)
    xExecPtr = 0
    
    
    #maps command to how much the execPtr need the incremented after said command
    xIncMapper = {
            0 : 2,
            1 : 2,
            2 : 2,
            3 : 2,  
            4 : 1,
            5 : 2,
            6 : 0,
            7 : 0,
            8 : 5,
        
        }
    
    xLineFinderValue  = 0
    xUltraSensorValue = 0
    
    sys.stdin.flush()
    
    while True:        
        xDoAttrOverride = False
        
        xCommand = int(xProg[xExecPtr])
        try: xAttr = xProg[xExecPtr + 1]
        except IndexError: pass

        print(f"ptr: {xExecPtr} \t command: {xCommand}".format())

        if xCommand == 0: print(f"forward  {xAttr}".format())
        elif xCommand == 1: print(f"backward {xAttr}".format())
        elif xCommand == 2: print(f"left     {xAttr}".format())
        elif xCommand == 3: print(f"right    {xAttr}".format())
        elif xCommand == 4: print("stop")
        
        elif xCommand == 5: time.sleep(xAttr)
        elif xCommand == 6: sys.exit(0)
        
        elif xCommand == 7: xDoAttrOverride = True
        elif xCommand == 8:
            xSensorCode = xProg[xExecPtr + 2]
            xCompType   = xProg[xExecPtr + 3]
            xConstValue = xProg[xExecPtr + 4]
            
            xSensorValue = None
            
            if   xSensorCode == 0: xSensorValue = xLineFinderValue
            elif xSensorCode == 1: xSensorValue = xUltraSensorValue
            
            if xCompType == 0 and xSensorValue == xConstValue: xDoAttrOverride = True
            elif xCompType == 1 and xSensorValue > xConstValue: xDoAttrOverride = True
            elif xCompType == 2 and xSensorValue < xConstValue: xDoAttrOverride = True
        
        
        try:    
            if xDoAttrOverride:  xExecPtr = int(xAttr)
            else:                xExecPtr += xIncMapper[xCommand]
            
        except  KeyError: Error(f"Invalid Command with number: {xCommand}".format())
    

try:                        Simulate(sys.stdin.read())
except KeyboardInterrupt:   pass