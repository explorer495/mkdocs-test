# Easy build - Arduino Mega

TODO This page needs pictures inserting.

The instructions below detail the steps required to use an EX8874 motor shield.

DO NOT USE ANY OTHER SHIELD TYPE WITHOUT FIRST CHECKING OUR DETAILED INSTRUCTIONS FOR THAT SHIELD.

## What you need

To build a basic DIY Command Station in easy steps you will need:

- A PC or laptop (Not A Raspberry Pi) running a reasonably recent versions of Windows, Linux or MacOS
- an Arduino Mega microprocessor
- USB cable to your PC for the processor.
- an EX-MotorShield8874 to power the track.
- A double-insulated DC power supply with a voltage suitable for your layout/locos.  
- Optionally.. an EX-WiFiSheild8266 to use Wifi throttles.

## Step By Step Build

### Prepare your Mega

1. Use sticky tape or similar to cover up the barrel connector on the Mega. (Power to the processor will be provided by the EX8874 shield and you don't want accidents.)

2. Use sticky tape or similar to cover the top of the USB connector on the mega. This prevents any accidental contact with the underside of the motor shield.  

### Prepare your EX8874 shield

Sight down both rows of pins on the EX8874 board and make sure they are all straight. They should all line up in a row and not be bent in any plane, just like the teeth on a comb. If any look like the photo below, bend them with your fingers and/or needle nose pliers.

### Mount the EX8874 shield

DO NOT USE ANY OTHER SHIELD TYPE WITHOUT FIRST CHECKING OUR DETAILED INSTRUCTIONS FOR THAT SHIELD.

1. Line up the pins on the side of the board closest to the USB with the header connector on the Mega first.
    See the picture below and notice the small gap between the two sets of pins to match the two pin header sockets.
2. Just align them and start to push them in but don’t push them all the way.
    Use your fingers to try to push the pins to get them to all go into the holes.
3. Do the same on the other side.
    Get all the pins aligned and start to press gently to get them into the holes. Notice on this side, you have more holes than you do pins. This is normal.
4. Being careful to not bend any pins gently press, using a rocking motion if you need to, in order to get the motor board to seat firmly onto the Mega. Press gently until you feel you can’t put the pins in any further. Don’t force anything, there will be a visible gap.

The board should be seated. Note the pins are longer than the headers. It is normal for you to see a few millimetres of the pins between the bottom of the motor board and the top of the headers.

Check your work. Look under and through where the boards connect, make sure no pins missed the holes and got bent so that they run along the outside of the headers.

### Connect your track

The EX8874 track connectors unplug for easy access.
    If you only have one piece of track for testing, wire it to the PROG track plug.

 1. Your PROG track is wired to the green socket closest to the power barrel connector.
 2. The MAIN track is wired to the far connector.

### Optionally install WiFiShield

1. Prepare your EX-WiFiShield8266 by removing the two jumpers, see picture.
2. Mount the WiFi shield on the EX8874 noting the correct orientation in the pictures and there will be 2 pins on either side which are deliberately missing.
3. Use a male-female Dupont wire (normally supplied with the shield) to connect to any one of the Tx pins on the WiFi Board, and connect the other end to the Rx1 pin on the mega (pin 19). See photo below.

4. Take a second jumper wire and connect it to any one of the Rx pins on the WiFi Board and connect the other end to Tx1 on the mega (pin 18).

TODO Photo.

### Connect your power supply

Plug in to the barrel connector on the EX8874 shield (NOT the mega).

### Connect to your PC

Using a suitable USB cable (must carry Data and Power, not all cables do this!) connect the Mega USB to your PC.

### Load the software

Congratulations, you have built a DIY command station the easy way. But you still have to load the software.

For simplicity, software loading is best done with the [EX-Installer](80-installer.md)
