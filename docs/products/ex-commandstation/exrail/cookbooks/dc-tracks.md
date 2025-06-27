# Set a track to DC

The command

- ``SET_TRACK(t,mode)`` is used to change the way a track is used.

Using a ROUTE or other sequence, you can set a track to the correct DC polarity and specify the loco address that the throttle will use to drive the loco on that track.

(The throttle doesn't need to know that you are using DC.)

```cpp
 ROUTE(77,"Set track A to DC for loco 123")
   SETLOCO(123)
   SET_TRACK(A,DC)
   DONE
```

Modes DC or DCX are only different in that the polarity is reversed. This will be important if you have, for example, a double track mainline which is normally wired in opposite polarity so that 'forward' is clockwise on one track and anticlockwise on the other.
To drive over a junction between the two, the 'to' track must be switched in polarity to match the 'from' track.

For example:

```cpp
ROUTE(78,"Cross from outer to inner")
  SETLOCO(123)
  SET_TRACK(A,DC)
  SET_TRACK(B,DCX)
  THROW(6) // throw the crossover turnout(s)
  DONE
```

See also the [facing turnouts](/products/ex-commandstation/exrail/cookbooks/turnouts/11-facing-turnouts.md) cookbook.
