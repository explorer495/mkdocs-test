# Virtual Bitmap device pins (VPINs)

A VPIN is an Arduino pin number that has been extended to include pins on external devices or expanders.

By giving external device pins unique VPIN numbers, the vast majority of the pin manipulation required by the user is controlled the same way regardless of whether the pin is an actual Arduino pin on the main CPU, an expander pin over i2c perhaps behind a multiplexer, a virtual pin or even a software-only pin simulation.

The vast majority of VPINs are either output (e.g. LEDs and servos) or input (e.g. buttons and sensors) but rarely both.  

## Creating virtual pins

Virtual pins are normally defined by specifying the Hardware Driver that is used to connect to an external device. There is no way for the command station to know for sure what devices are connected so it must be told. This is done by including HAL commands in myAutomation.h

For Example

```cpp
    HAL(PCA9685,100,16,0x20) 
    HAL(MCP23017,200,16,0x40) 
```


This would create VPINs 100 to 115 to represent the 16 servo outputs of a [PCA9685](?PCA9685) servo control board at I2C address 0x20 and VPINS 200 to 215 in an [MCP23017](?MCP23017) i/o expander.  
Refer to wiring details and fuller list of [supported I2C devices](#) elsewhere.

## Using OUTPUT VPINS

Pin values can be changed with basic digital pin commands common to all VPINs.  In EXRAIL

`SET(113)` `RESET(113)`  sets value HIGH or LOW.

`SET(100,5)` or `RESET(100,5)`  sets/resets a range of pins (100..104 in this case).

`BLINK(201,250,750)` sets pin 201 blinking for 250mS on and 750mS off. Blinking is stopped by a SET or RESET of the pin.

Serial commands can set HIGH/LOW values to VPINs using <z 201> <z -201> as for any digital output.

## Using INPUT VPINs

`IF(200)` tests if pin value is HIGH.

`ONBUTTON(200)` triggers when a pin goes HIGH. This is most useful for push buttons connected between the pin and ground. This causes a new EXRAIL task to start and switch bounce will be ignored until the task completes.

For example:

```cpp
ONBUTTON(202) 
   RED(11) 
   THROW(2)
   CLOSE(1)
   GREEN(12)
   DONE
```

`ONSENSOR(200)` triggers when a sensor changes state. This is less useful.

Other more advanced commands are available, see cookbooks.

