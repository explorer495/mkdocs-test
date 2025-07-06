# AUTOMATIONS

An AUTOMATION is a sequence of EXRAIL commands used to drive a loco.

By creating an AUTOMATION in EXRAIL, your throttle will show the automation on its Routes display. To send a loco along an AUTOMATION, you must first drive the loco to a point where the automation can start and then select the automation from the routes screen.

The automation will take over driving the loco but you will still see the throttle moving if the loco changes speed. If you manually alter the speed with the throttle that will take effect normally as the automation spends most of its time in an AT command waiting for the train to reach a sensor, and will not wake up again until the sensor is detected. You may, for example, stop the train manually to fix a derailment, dropped rolling stock or cat sitting on the track. When you restart the loco and drive it to the sensor, the automation will carry on.

Imahine we have a track like this with sensors..

```
Dogbath                                                  Catflap
||============================================================||
  |          |                                  |            |
 180        181                                182          183
```

Create an automation like this. The automation id needs to be unique amongst all AUTOMATION, ROUTE or SEQUENCE definitions.  

```cpp
AUTOMATION(123,"Dogbath to Catflap and back")
  FWD(20) // Set off
  AT(181) SPEED(40) // once round bend, increase speed
  AT(182) SPEED(20) // approaching Catflap
  AT(183) STOP // at Catflap stopping point
  DELAYRANDOM(5000,10000) // wait for tea trolley to be refreshed
  REV(20) // reverse away 
  AT(183) SPEED(50) // out of station
  AT(181) SPEED(20) // approaching Dogbath
  AT(180) STOP // stopping point
  DONE // task is complete 
```

First drive your loco to Digbath with the forward facing Catflap. Select the automation from your throttle and the train should make the journey.

It should be pretty obvious what this does and where the sensors need to be to give a reasonable slow down point. The AT command stops the task until the sensor is activated. EXRAIL commands can be on the same line or separate lines, it makes no difference but sometimes its easier to read if you put things like AT something DO something on one line.

If you wished this to shuttle back and forth, just replace the `DONE` with `DELAYRANDOM(5000,10000) FOLLOW(123)` and the automation will delay at Catford and loop back to the start.

Of particular interest, compared with a PC (JMRI, iTrain, RocRail etc) running the loco, EXRAIL is only interested in the sensor your task us trying to reach. This makes it vastly more efficient than even the fastest PC system.
