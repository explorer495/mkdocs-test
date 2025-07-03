# Route button control

Route buttons appear on the throttle and can be controlled from EXRAIL to hide, disable or recaption the button. Everything here applies equally to AUTOMATIONs.

If a route button can be in one of 4 states:
  
- Inactive (waiting to be pressed)
- Active (highlighted as if selected)
- Disabled (you can't press this)
- Hidden (the entire route is not visible on the throttle)

This allows EXRAIL to prevent multiple conflicting routes to be set, or to replace the default "Set" button with open/close, start/stop, yes/no, on/off or whatever makes most sense in context.

Here are examples of solving the same problem but with different user experiences.
In this case we want a way of setting a light on or off.

## Simple light switch route

 This example just has the logic to switch a light on/off with the "Set" button.
 It uses a [Bitmap flag](/products/ex-commandstation/exrail/cookbooks/flags-and-latches/flags.md) to remember whether the light is on or off. Note that the light and flag will default to off.

 A flag or range of flags in created like this:

```cpp
HAL(Bitmap,800,16)
```

That creates flags 800..815, we only need one here but if you need more, its better to crete a bank of flags in one go rather than lots of individual flags.

```cpp
ROUTE(600,"Shed lights")
  IF(800)  // is the light on? 
     RESET(120)  // lights off
     RESET(800)
  ELSE  // light is off 
     SET(120)  // lights on
     SET(800)
  ENDIF
  DONE
```

## Changing button captions

The same logic includes changing the button caption from "Set" to "Turn On" or "Turn Off".

```cpp
ROUTE(600,"Shed lights")
  IF(800)  // is the light on? 
     RESET(120)  // lights off
     RESET(800)
     ROUTE_CAPTION(600,"Turn on") // change button caption
  ELSE  // light is off 
     SET(120)  // lights on
     SET(800)
     ROUTE_CAPTION(600,"Turn off") // change button caption
  ENDIF
  DONE

AUTOSTART
  ROUTE_CAPTION(600,"Turn On") // start with lights off (pin and flag will default off)
  DONE

```

## Changed button active/inactive appearance

This example make the "set" button appear active (highlighted) or inactive

```cpp
ROUTE(600,"Shed lights")
  IF(800)  // is the light on? 
     RESET(120)  // lights off
     RESET(800)
     ROUTE_INACTIVE(600) // change button state to inactive
  ELSE  // light is off 
     SET(120)  // lights on
     SET(800)
     ROUTE_ACTIVE(600) // button appears highlighted as active
  ENDIF
  DONE
```

## Two separate routes example

This example has two "routes" to control lights, but only one of them will be visible at a time so we dont need a flag.
Each route will have the default "Set" button.

```cpp
ROUTE(600,"Shed lights on")
  SET(120)
  ROUTE_HIDDEN(600) // hide self
  ROUTE_INACTIVE(601) // reveal off 
  DONE

ROUTE(601,"Shed lights off")
  RESET(120)
  ROUTE_HIDDEN(601)
  ROUTE_INACTIVE(600)
  DONE
  
AUTOSTART
    ROUTE_HIDDEN(601)  // shed lights are off already
  DONE
```
