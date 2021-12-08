import sys
#bad code, i know, and i don't care





def Assemble(xRaw):
		xOutputBuffer = []
		xLines = xRaw.split("\n")
		xPointMapper = {}
		xCommands = ["forward", "backward", "left", "right", "stop", "wait", "exit", "jump", "if"]

		xSensorDec = {
				"lineSensor" : 0.0,
				"ultraSensor" : 1.0,
				
			
			
			}


		xSpaceMapper = {
				"forward" : 2,
				"backward" : 2,
				"left" : 2,
				"right" : 2,  
				"stop" : 1,
				"wait" : 2,
				"exit" : 1,
				"jump" : 2,
				"if" : 5,
			
			}


		xIndex = 0
		for xLine in xLines:
			xLineTerminals = xLine.split(" ")
			
			if len(xLineTerminals) > 0 and xLineTerminals[0] == "point":
				xPointMapper[xLineTerminals[1]] = xIndex

			elif xLineTerminals[0] in xSpaceMapper.keys(): xIndex += xSpaceMapper[xLineTerminals[0]]



		xIndex = 0
		# iterate over lines
		for xLine in xLines:
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

				elif xCommand == "jump":
						xTempBuffer.append(7.0)
						xPointName = xLineTerminals[1]
						xPointIndex = xPointMapper[xPointName]
						xTempBuffer.append(float(xPointIndex))

				elif xCommand == "if":
					xSensorCode = xSensorDec[xArgs[0]]
					xCompType = {"=" : 0.0, ">" : 1.0, "<" : 2.0}[xArgs[1]]
					xConstValue = float(xArgs[2])

					xPointName = xArgs[4]
					xPointIndex = xPointMapper[xPointName]

					
					xTempBuffer.append(8.0)					
					xTempBuffer.append(float(xPointIndex))
					xTempBuffer.append(xSensorCode)
					xTempBuffer.append(xCompType)
					xTempBuffer.append(xConstValue)

				xOutputBuffer += [str(x) for x in xTempBuffer]

				#check for the difference of the array length, to adjust index
				xIndex += len(xTempBuffer)
						
						
		return xOutputBuffer


if __name__ == '__main__':
    xPath = sys.argv[1]
    xFile = open(xPath, "r").read()
    
    xPythonOutputFormat = "--py" in sys.argv
    
    if not xPythonOutputFormat: print("{ " + ", ".join(Assemble(xFile)) + " }")
    else:						print("[ " + ", ".join(Assemble(xFile)) + " ]")

