Installing and running
----------------------
This portable robot simulator was developed by [Student Robotics](https://studentrobotics.org).

The simulator requires a Python 2.7 installation along with pygame, PyPyBox2D, PyYAML libraries. 

Once you have the aforementioned requirements, run this using the below-given line of code. 
```bash
 $ python2 run.py assignment.py
```

**Pseudo Code**
-------------


Import necessary libraries

**#Define the threshold values**



a_th = 2.0
d_th = 0.4

**#Define Functions**

=> def drive(speed, seconds):

Functions for setting the linear velocity



=> def turn(speed, seconds):

Function for setting an angular velocity


=> def find_token(no_of_markers):

 Search for the closest tokens and those tokens who are not yet been picked up
 
 Return the distance, angle and the token code


 

=>def move(no_of_markers):

 Move the robot to the closest token
 
 If no token is not detected, the Robot will look for the token
 
 Adjust the robot's position and orientation according to the token
 
 If the token is found, then the robot will grab it.

 

=>def destination_location(no_of_markers):

 Find the location to gather them.
 
 Return the distance and angle between the robot's and the destination.

 

=>def def go_to_destination (no_of_markers):

 Move the robot to the destination
 
 If no location is detected, will search for the location
 
 Adjust the robot's position and orientation according to the destination.

 

**#Define the main function**

Initialize a list to store markers' codes

Initialize the variable to count the box

If the robot collected the box and put it in a place, then end the program

If it's the first time then define the location!

If it's not the first iteration, move the robot to the destination token

Release the token, move back, and update the list of markers' codes

Print list of markers' codes

Call the main function to execute the program


Robot API
---------

The API for controlling a simulated robot is designed to be as similar as possible to the [SR API][sr-api].

### Motors ###

The simulated robot has two motors configured for skid steering, connected to a two-output [Motor Board](https://studentrobotics.org/docs/kit/motor_board). The left motor is connected to output `0` and the right motor to output `1`.

The Motor Board API is identical to [that of the SR API](https://studentrobotics.org/docs/programming/sr/motors/), except that motor boards cannot be addressed by serial number. So, to turn on the spot at one quarter of full power, one might write the following:

```python
R.motors[0].m0.power = 25
R.motors[0].m1.power = -25
```

### The Grabber ###

The robot is equipped with a grabber, capable of picking up a token which is in front of the robot and within 0.4 metres of the robot's centre. To pick up a token, call the `R.grab` method:

```python
success = R.grab()
```

The `R.grab` function returns `True` if a token was successfully picked up, or `False` otherwise. If the robot is already holding a token, it will throw an `AlreadyHoldingSomethingException`.

To drop the token, call the `R.release` method.

Cable-tie flails are not implemented.

### Vision ###

To help the robot find tokens and navigate, each token has markers stuck to it, as does each wall. The `R.see` method returns a list of all the markers the robot can see, as `Marker` objects. The robot can only see markers which it is facing towards.

Each `Marker` object has the following attributes:

* `info`: a `MarkerInfo` object describing the marker itself. Has the following attributes:
  * `code`: the numeric code of the marker.
  * `marker_type`: the type of object the marker is attached to (either `MARKER_TOKEN_GOLD`, `MARKER_TOKEN_SILVER` or `MARKER_ARENA`).
  * `offset`: offset of the numeric code of the marker from the lowest numbered marker of its type. For example, token number 3 has the code 43, but offset 3.
  * `size`: the size that the marker would be in the real game, for compatibility with the SR API.
* `centre`: the location of the marker in polar coordinates, as a `PolarCoord` object. Has the following attributes:
  * `length`: the distance from the centre of the robot to the object (in metres).
  * `rot_y`: rotation about the Y axis in degrees.
* `dist`: an alias for `centre.length`
* `res`: the value of the `res` parameter of `R.see`, for compatibility with the SR API.
* `rot_y`: an alias for `centre.rot_y`
* `timestamp`: the time at which the marker was seen (when `R.see` was called).

For example, the following code lists all of the markers the robot can see:

```python
markers = R.see()
print "I can see", len(markers), "markers:"

for m in markers:
    if m.info.marker_type in (MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER):
        print " - Token {0} is {1} metres away".format( m.info.offset, m.dist )
    elif m.info.marker_type == MARKER_ARENA:
        print " - Arena marker {0} is {1} metres away".format( m.info.offset, m.dist )
```

[sr-api]: https://studentrobotics.org/docs/programming/sr/
