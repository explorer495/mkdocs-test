# Buying I2C devices

There are many I2C devices available and the price/availability can vary widely depending on your location and delivery options. Where devices are very cheap, you may find quality issues and so expect a few duds. 

Some devices come with [Qwiic](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs) connectors which makes them easier to plug-and-play with the Qwiic connector on your EX-CSB! or EX8874 motor shield. 

In general the Adafruit devices below are high quality and well documented but that is usually reflected in the price.

- MCP23017 provides 16 pins for mixed input or output.
[(see details)](https://www.adafruit.com/product/5346#technical-details) This is good for
    - Up to 14 inputs from push-buttons, switches, sensors.
    - Up to 16 outputs to LEDs and signals (which require current limiting resistors) and relays.

- PCA9685 provides up to 16 outputs for servos and LEDs (PWM pins used for V+ include resistors) [(See details)](https://www.adafruit.com/product/815)

- LTC4311 resolves electronic issues when the total of I2C wiring is greater than approximately 2m or 6ft. [(See details)](https://www.adafruit.com/product/4756)

- Qwiic wires make it easy to plug these devices together.
[(See details)](https://www.adafruit.com/product/4210)

TODO

- mux
- neopixel
