.. _procoda:

*******
ProCoDA
*******

Important Parts of ProCoDA (Imagine it as a washing machine)
------------------------------------------------------------

* Setpoints: There are two types of setpoints in ProCoDA, constants and variables. These are the numbers thatProCoDA uses to run any of its functions (These are things like warm or cold water)
* States: States are the different ways ProCoDA can run (These are the parts of a laundry cycle like wash, rinse, spin)
* Rules: These control when ProCoDA changes between states (These are like going from rinse to spin)

General Notes
-------------
* When you input a value that it a decimal it will convert it into a form without the decimal (i.e. 0.3 will become 300m)
* The required set points give the order of the set points and the set points must be in the same order when you input them
* All added set points should be added after ON and OFF, always add setpoint after because it will mess with the selected set points

Connect a turbidimeter
----------------------
* Edit Rules
* Add a set point for the unitID
* Set the value to usually 1
* Add a second setpoint the turbidity
* Change the turbidity from a constant to a variable
* Now more options will appear click on the folder which will open a window
* Click on HF Turbidimeter
* Then choose the com that the turbidimeter is connected to the computer with
* Select the required set points(If you don’t know you can always try all of them and see which one has the correct value displayed, if it is not the right one the value will be -999)

Connect a sensor
----------------
* Go to Configuration → Click on the volts symbol
* Make sure your sensor is plugged into the procoda box
* Click insert sensor and change the channel to the correct port
* Then open the folder button and click the type of sensor you have and what you want it to record (i.e. cm of water for headloss)
* Name it sensor
* To zero the sensor, click the zero button

Connecting a pump
-----------------
There are many ways to connect a pump, but I am going to stick to one pump head, since adding more is fairly straight-forward. I will also be doing it with the code that uses mL/s and tubing ID, but you can use the other codes as well, as long as you have the required set points.

* Add a constant set point with the mL/s that you want the pump to run at
* Add a constant set point with the tubing size that you will be using
* Add a variable set point
* Click on the folder and open the peristaltic folder and choose the right code you want to use for this tutorial it is single head pump control (mL per second, Tubing Size)
* Select the set points
* It should display the rpm of the pump as a decimal in the value
* You can calculate the rpm of the pump using the auto tutorial for peristaltic pumps on the wiki

How to save data from a test
----------------------------
Under Datalog directory path, click on the folder, and choose where you want data to be stored. Procoda will store information from all variables and sensors there.

How to set up a pump for a test
-------------------------------
#. Edit Rules
#. Click Rules and Outputs
#. Add a new state
#. Click on Outputs
#. Look at which pump port it is connected to
#. Turn pump on/off to on
#. Turn pump cw/ccw on or off depending on which way you want it to turn
#. For pump speed choose the variable set point you created when you connected the pump
#. To test it go to process operation and change the state to the state you added
#. If your pump is not running at the speed ProCoDA displays you can calibrate it using the pump calibration button

How to set up a timed test
--------------------------
#. Edit Rules
#. Create a constant set point with the value as the number of SECONDS you want to test to go on for
#. Go to Rules & Outputs
#. Click on the state that runs the test then click on rules
#. Then it is basically like a computer program
#. If elapsed time in current state> run time of test
#. Then go to next state usually it is OFF
#. You can also do many other conditional statements with this function like have pumps turn off based on pressure and such
