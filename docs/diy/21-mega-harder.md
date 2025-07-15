# Alternative build - Arduino Mega

TODO This page needs pictures inserting.


These instructions assume a slightly more competent user who has made the decision to trade simplicity for price. It is assumed that you are comfortable modifying devices, soldering etc. and are not going to make costly mistakes such as mixing up the power supplies.

There are a limited number of suitable motor or WiFi shields available and each has its own quirks.

## What you need

To build a basic DIY Command Station you will need:

- A PC or laptop (Not A Raspberry Pi) running a reasonably recent versions of Windows, Linux or MacOS
- an Arduino Mega microprocessor running our free Open Source software
- USB cable to your PC for the processor.
- an Arduino standard (or others as noted in details) motor-shield to power the track.
- A double-insulated DC power supply with a voltage suitable for your layout/locos.
- An additional double-insulated DC Power supply of 5 to 8 volts suitable to drive the Arduino logic. (This may also be fed through the USB cable, and old phone charger is suitable or if you intend to use JMRI your computer will supply this power.)
- Optionally
    - a female barrel connector to match the plug on your chosen track power supply
    - a suitable WiFi shield to use WiFi throttles (Recommended) with 2 suitable M-F Dupont wires.
    - OR an Ethernet Shield

## Step By Step Build

### Prepare your Mega

1. Use sticky tape or similar to cover the top of the USB connector on the mega. This prevents any accidental contact with the underside of the motor shield.  

### Optionally mount your Ethernet Shield

Note, you can't have Ethernet and WiFi running on the same command station, but you can install both shields and choose one or the other when installing the software.

The standard Ethernet shields must be first in the stack as they use pins that are not passed through the headers of the motor shield. Look underneath the shield and this will become obvious. The shields also cause issues with their height, shields above may not sit level (but will still work) unless you introduce an extra row of header extenders.

Non-shield Ethernet adapters have other wiring requirements. Search our help for [details](?Ethernet).

### Prepare your motor shield

FAILURE TO DO THIS CAN DESTROY YOUR MEGA.

1. Unless you are using an EX8874 shield, you MUST prevent the shield from feeding track voltage into your Mega. This is done by cutting the VIN trace and/or removing the pin that feeds the Mega.
TODO See pictures applicable to the various supported shields.

2. Ensure shield pins are straight and correctly aligned.

### Mount the motor shield

1. Align the motor shield so that the power connectors are at the same end as the Mega power/usb connectors.
2. Being careful to not bend any pins gently press, using a rocking motion if you need to, in order to get the motor board to seat firmly onto the Mega. Press gently until you feel you can’t put the pins in any further. Don’t force anything, there will be a visible gap.

The board should be seated. Note the pins are longer than the headers. It is normal for you to see a few millimetres of the pins between the bottom of the motor board and the top of the headers.

Check your work. Look under and through where the boards connect, make sure no pins missed the holes and got bent so that they run along the outside of the headers.

### Connect your track

Don't skip this step if you don't yet have any track because the WiFi shield will cover the connectors.

It's best to create fly leads with a suitable pluggable connectors for later. It makes it much easier to detach your command station from your layout when you need to fiddle with it or throw it against the wall out of sheer frustration.

If you only have one piece of track for testing, wire it to the PROG track plug.

 1. Your PROG track is wired to the B channel output.
 2. The MAIN track is wired to the A channel output.

### Connect your track power supply

1. Wire your track power supply to the input turrets of the motor shield, observing polarity. It is best to create short wire with a female barrel connector.

### Optionally install a Wifi Shield

1. Make sure your Wifi shield is loaded with a suitable version of the Espressif AT command firmware. See [firmware loading instructions](?Espresif firmware)

2. Prepare your WiFi shield (see supported types and notes below) by removing the pins that connect to the Mega Serial port.
3. Mount the WiFi shield on the motor shield.
4. Use two male-female Dupont wires to connect the shields TX pin to the Mega RX1 pin, and the shield RX pin to the Mega TX1 pin.  

TODO Photo.

### Load the software

Software loading is best done with the [EX-Installer](80-installer.md)
