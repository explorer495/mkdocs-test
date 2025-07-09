# Connecting a servo turnout

The details below assume you are using an EX-CSB1 command station or a DIY station with an EX8874 motor shield and Wifi connection. Otherwise the steps are the same but the wiring is trickier without the Qwiic sockets and testing requires command input.

You will need the following for up to 16 servos.

- Your Command Station with power supply and USB connection to your PC.
- A Qwiic cable
- A PCA9685 (preferably with Qwiic sockets)
- Up to 16 SG90 servos.
- The EX-Installer downloaded and installed on your PC.
- (Optionally) and Android phone with EX-Toolbox installed
- A servo power supply 5 or 6V DC not taken from the command station.

## Follow the steps below

1. Turn off power to your Command station and unplug the USB cable.
2. Connect the Qwiic cable between the CSB1 ![CSB1](/_static/images/ex-csb1/csb1qwiic.jpg) (or EX8874 on a mega) ![mega](/_static/images/mega/mega-EX8874.jpg)) and the PCA9685. 
3. Run the EX-Installer on your PC and select the cpu type, then the Serial Monitor. You should see output similar to the following where the Command Station enumerates all the I2C devices it can find.
4. Examine the log to check that your PCA9685 has been detected and note the I2C address it was discovered at. This will typically be 0x40. If this address is 0x40 or 0x41 then the CS has defaulted this to be a PCA9685 and automatically assigned a range of 16 [VPINs](?VPIN) to represent the 16 servo outputs.
5. Examine the log further down and you should see. TODO CLIP where the VPINs are assigned. The following advice assumes that the address was 0x40 and the first VPIN will be 100.
6. Plug a servo into the first output socket. DO NOT mechanically connect the servo arm to any turnout or animation as the servo may move unexpectedly and cause physical damage.
7. Connect the additional servo power supply to the long-edge turrets on the PCA9685, observing the correct polarity. ![PCA9685](/_static/images/i2c-devices/PCA9685.jpg)
8. On the installers serial monitor, enter the command ```<D SERVO 100 2000>``` which should move the servo. Experiment with other positions than 2000. The usable range is approximately 100 to 4000 but varies.  
9. (Optionally) Use the EX-Toolbox Andoid app to experiment with servo angles and servo arm lengths until you have the required throw distance and angles to suit your servo mounting preferences.

## Define your Turnouts

1. In EX-Installer, edit myAutomation.h and define each turnout to give an id of your choice, the VPIN of the servo, the closed and open servo values you have discovered by experimentation and a suitable decription to show on your throttle. 

 For example 

 ```cpp
 SERVO_TURNOUT(1,100,350,720,"Coal yard exit")
 SERVO_TURNOUT(2,101,400,800,"Branch line siding")
 ```

 2. Reload the command station from the installer.

## Test your turnout definitions

1. Using the serial monitor as before, enter the commands ```<T 1 T>``` to throw turnout 1, ```<T 2 C>``` to close turnout 2 and so on. 
2. With your Wifi throttle (Typically Engine Driver) navigate to the turnouts page where you will see the two turnouts listed. From there you can throw or close them as required.

## Connect your servos to turnouts

There are many ways of mounting servos both above and below the baseboard using 3D printed mounts or a strip of plastic L shape. You will probably want to use microswitches to switch frog polarity or use more expensive frog juicers or EXRAIL driven relays. 

We recommend that whatever mechanical connection you make allows for protection of you turnout from excess servo movement.
