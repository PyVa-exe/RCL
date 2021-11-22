import sys
#bad code, i know, and i don't know



def Assemble(xRaw):
    xOutputBuffer = []
    
    xIndex = 0
    for xLine in xRaw.split("\n"):
        xLineTerminals = xLine.split(" ")
        xCommand = xLineTerminals[0]
        if len(xLineTerminals) > 1: xArgs = xLineTerminals[1:] 

        
        xTempBuffer = []
        if xCommand == "forward":
            xTempBuffer.append(0.0) #command
            xTempBuffer.append(float(xArgs[0]) / 100 * 255) #arg (value needs to be converted to 8-bit spectrum)
                        
        elif xCommand == "backward":
            xTempBuffer.append(1.0)
            xTempBuffer.append(float(xArgs[0]) / 100 * 255)


        elif xCommand == "left":
            xTempBuffer.append(2.0)
            xTempBuffer.append(float(xArgs[0]) / 100 * 255)


        elif xCommand == "right":
            xTempBuffer.append(3.0)
            xTempBuffer.append(float(xArgs[0]) / 100 * 255)


        elif xCommand == "stop":
            xTempBuffer.append(4.0)

        elif xCommand == "wait":
            xTempBuffer.append(5.0)
            xTempBuffer.append(float(xArgs[0]))

        elif xCommand == "exit":
            xTempBuffer.append(6.0)



        #handle commands with complex syntax structure
        #var set
        if len(xLineTerminals) > 2 and xLineTerminals[1] == "=":
            xTempBuffer.append(7.0)
            xTempBuffer.append(xLineTerminals[0])
            xTempBuffer.append(xLineTerminals[2])
            



        xOutputBuffer += [str(x) for x in xTempBuffer]

        #check for the difference of the array length, to adjust index
        xIndex += len(xTempBuffer)
            
            
        
    return xOutputBuffer


if __name__ == '__main__':
    xPath = sys.argv[1]
    xFile = open(xPath, "r").read()
    
    print("{ " + ", ".join(Assemble(xFile)) + " }")
    

