
#Overview


##What is EX-FastClock?

EX-FastClock is a standalone microprocessor based fast adjustable speed clock, using an additional Arduino Uno in conjunction with a shield based TFT touchscreen. Features have been added to EX-CommandStation to allow the clock to integrate to the EX-CommandStation and control EXRAIL based on time events.

Each time the time changes the EX-CommandStation looks for a time change event and if it finds a match it executes the commands recorded for that event as defined in the EXRAIL myAutomation.h file.  Additionally the EX-CommandStation will issue a time broadcast so that other devices such as clock repeaters can capture the time.  Also where WiThrottle devices are connected a WiThrottle broadcast is made which means that connected devices such as Engine Driver can display the time.

EX-FastClock allows the FastClock device to connect to the EX-CommandStation via either Serial Communications or I2C.  Even though EX-FastClock provides the code for an Uno based Clock it should be possible for tinkerer level users to add the relevant code if they already have a working clock that they wish to integrate to EX-CommandStation.

To make full use of EX-FastClock**, you will need a basic understanding of EX-RAIL automation, but we'll share the details and some examples to help with this.

**NOTE**

  EX-FastClock is in public Beta testing, and as such, we encourage regular feedback on the success or otherwise of both the software and documentation. Please reach out via any of our support methods and help us get EX-FastClock as easy to use and reliable as possible.



The EX-FastClock integration includes:

* A ready made Arduino program for an Arduino Uno based Fast Clock
* Support for Serial connection
* |I2C| device driver
* EX-RAIL automation support
* Time Broadcast for time display on WiThrottle controllers such as |Engine Driver|
* Debug output to Serial Monitor


##Credit where credit is due!

*The EX-FastClock is based on a project originally written by Jim Gifford (Hallet Cove Southern) in June 2017. That project used a 32 x 8 LED matrix to display the time and was controlled by a number of pushbuttons. You can see Jim's Original Project `here <https://www.hallettcovesouthern.com/track-plan-design-info/arduino-projects/fast-clock/>`.

*MCUFRIEND.kbv credit: This library was written by David Prentice and has become the De-Facto standard for the shield based TFT screens used in this project. This library inherits from the Adafruit GFX library.

*Adafruit for the Adafruit GFX Library.


##Next Steps


Now that you have a general overview of EX-FastClock's features and capabilities, click the "next" button see what is needed to create an EX-FastClock**.
