
#EX-FastClock

Welcome to the home of EX-FastClock, a fully integrated Fast Clock for **EX-CommandStation**. 

EX-FastClock is a standalone adjustable speed clock built using an additional Arduino Uno microcontroller and a plug-in shield type TFT touch screen.  The commands built into the DCC_EX Command Station make it possible to also integrate an existing microcontroller based fast clock.

## Background

This project is based on a project originally written by Jim Gifford (Hallet Cove Southern) in June 2017.  This project used a 32 x 8 LED matrix to display the time and was controlled by a number of pushbuttons.

[See Jim's Original Project here.](https://www.hallettcovesouthern.com/track-plan-design-info/arduino-projects/fast-clock/)

I felt that this project was ripe for an update and decided to convert Jim's code to operate using a cheap TFT/LCD touch screen to run on my own layout. This project is the result.  Much of the code has been rewritten into smaller functions with additional features added, but the time clock calculations are the originals.

This project has now been extended to add the capability of integrating the clock to the DCC-EX 
Command Station and more specifically the EXRAIL automation feature which now allows time based 
control. This feature is optional and can be controlled by the config.h file.

