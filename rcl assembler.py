import sys
#bad code, i know, and i don't know



def Assemble(xRaw):
    xOutputBuffer = []
    
    xIndex = 0
    for xLine in xRaw.split("\n"):
        xCommand = xLine.split(" ")[0]
        xArgs    = xLine.split(" ")[1:]

        if xCommand == "forward":
            xOutputBuffer.append(0) #command
            xOutputBuffer.append(float(xArgs[0]) / 100 * 255) #arg (value needs to be converted to 8-bit spectrum)
                        
            xIndex += 2

            
        elif xCommand == "backward":
            xOutputBuffer.append(1)
            xOutputBuffer.append(float(xArgs[0]) / 100 * 255)

            xIndex += 2


        elif xCommand == "left":
            xOutputBuffer.append(2)
            xOutputBuffer.append(float(xArgs[0]) / 100 * 255)
            
            xIndex += 2


        elif xCommand == "right":
            xOutputBuffer.append(3)
            xOutputBuffer.append(float(xArgs[0]) / 100 * 255)
                        
            xIndex += 2
            
            
        
    return xOutputBuffer


if __name__ == '__main__':
    xPath = sys.argv[1]
    xFile = open(xPath, "r").read()
    
    print(Assemble(xFile))
    

