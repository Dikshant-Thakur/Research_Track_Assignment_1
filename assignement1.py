from __future__ import print_function

import time
from sr.robot import *



a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_token(no_of_markers):
    """
    Function to find the closest token

    Returns:
	dist (float): distance of the closest token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    dist=100
    for token in R.see():
    	if token.dist < dist and token.info.code not in no_of_markers:  
        	dist = token.dist
       	rot_y = token.rot_y
       	code = token.info.code
        		

    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, code
   	
def move(no_of_markers):
    dist = -1
    while (1):
    	dist, rot_y,code = find_token(no_of_markers)  # we look for markers and code
    	if dist==-1:
        	print("Where is the token?")
		turn(80,0.5)  # if no markers are detected
		
    	elif dist < d_th: 
        	 print("Found it!")
        	 R.grab() # if we are close to the token, we grab it.
        	 print("Gotcha!") 
        	 break
    	
    	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
         	 print("Ah, here we are!.")
         	 
         	 if dist  >= d_th + 0.1 :
          	 	drive(100, 0.1)
          	 else:
          	 	drive(10,0.5)
        	
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	 print("Left a bit...")
        	 turn(-5, 0.01)
        	
   	elif rot_y > a_th:    
    	     	print("Right a bit...")
        	turn(+5, 0.01)
         	  
      	elif dist  <= d_th + 0.1 :
        	drive(10,0.1)
        
        elif dist  >= d_th + 0.1:
        	drive(100,1)
        	
    return code
        	
def destination_location(no_of_markers):
	dist = 100
	for token in R.see():
		if token.info.code in no_of_markers:
			dist = token.dist
			rot_y = token.rot_y
			
	if dist == 100:
		return -1, -1
	else:
		return dist, rot_y
			
	
	
def go_to_destination (no_of_markers):
    while (1):
    	dist, rot_y = destination_location(no_of_markers)  # we look for markers and code
    	if dist==-1:
        	print("Where is the centre?? Let me see")
        	turn(100,0.1)
		drive(-50,0.3)  # if no markers are detected)
		
		
    	elif dist <= d_th + 0.3: 
        	 print("Found it!")
		 break
    	
    	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
         	 print("Ah, here we are!.")
          	 if dist  >= d_th + 0.3 :
          	 	drive(100, 0.1)
          	 else:
          	 	drive(10,0.5)         
        	
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	 print("Left a bit...")
        	 turn(-5, 0.1)
        	
   	elif rot_y > a_th:
    		print("Right a bit...")
        	turn(+5, 0.1)

	
	
def main():
	no_of_markers = []
	i = 0
	while 1:
		if len(no_of_markers) == 6:
			print("All done")
			break
		code = move(no_of_markers)
		if i == 0:
			turn(-13,1)
			drive(50,4.0)
			
			i += 1
			
		else:
			go_to_destination(no_of_markers)

		R.release()
		drive(-50,1)
		turn(50,1)
		no_of_markers.append(code)
		print(no_of_markers)
		
		
main()
	
	
				
		
	
	
