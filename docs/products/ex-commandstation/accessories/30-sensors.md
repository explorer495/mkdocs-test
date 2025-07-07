# Sensors

Sensors become necessary when you wish to add automated control of accessories or trains, or you wish to add a control panel separate from the functions of your throttle. Each sensor device can trigger actions or be read in [EXRAIL](?EXRAIL) or be passed up to a PC controller such as JMRI, RocRail or iTrain.

Sensor devices include

- Switches and buttons on a control panel
- InfraRed or ultrasonic detectors when a train crosses a point on the track
- Video camera using AI to detect train position or children's hands reaching over the layout
- Block Occupancy (or Train-on-track, TOTI) detectors that detect the current consumed by a loco decoder or resistor-fitted rolling stock when present in an isolated track block.

EXRAIL is used to handle sensors

- Describe how the sensor devices are wired to the command station (usually via I2C) and what [VPIN](?VPIN) is to be assigned to each sensor

- Control what happens when a sensor VPIN changes state

The most common method of connecting sensor devices to your command station is through an [MCP23017](?MCP23017) device which offers up to 14 input pins (or 16 output pins, or a mix of both) through a single I2C connection. For more inputs you can add more MCP23017 devices to the I2C chain.

The [EX-IOExpander](?IOExpander) can be used to connect multiple sensors over a single I2C connection depending on the microprocessor used to build it.

The [EX-SensorCam](?SensorCam) can be used to offer up to 80 sensor points on a single I2C connection.  
