# STEALTH control of displays (Advanced)

The following example creates a C++ function to display loco details on an OLED screen. By using a generic HAL driver, the function can be invoked repeatedly according to a time delay.

BEWARE that code like this is sensitive to many restrictions such as time taken and memory use. It is also subject to version changes in some of the internal dcc-ex routines so is only given here as an example.

EXRAIL macros cannot be used inside STEALTH sections. Users using STEALTH and STEALTH_GLOBAL are expected to understand the implications and the C++ language features used.

The STEALTH_GLOBAL macro allows the creation of C++ functions within the command station environment.
This function displays the first 8 locos in the DCC speed reminders table on LCD/OLED screen 2.

```cpp
STEALTH_GLOBAL(
  void updateLocoScreen() {
    for (int i=0; i<8; i++) {
      if (DCC::speedTable[i].loco > 0) {
        int speed = DCC::speedTable[i].speedCode;
        char direction = (speed & 0x80) ? 'F' : 'R';
        speed = speed & 0x7f;
        if (speed > 0) speed = speed - 1;
        StringFormatter::lcd2(2, i+2, F("Loco:%4d %3d %c"), 
            DCC::speedTable[i].loco,speed, direction);
            }
        }
    }
)
```

To ensure the function is called once per second we use the UserAddin HAL feature.
The LCD/OLED number 2 used by the function is connected by I2C. 

```cpp
HAL(UserAddin,updateLocoScreen,1000) 
HAL(HALDisplay<OLED>, 2, 0x3d, 128, 64)  
```
