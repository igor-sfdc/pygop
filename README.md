pygop
=====

A python module to interface with the GOP service from Greenwave Reality.

## Instructions

1. Press the sync button on the gateway. It will begin to flash.
2. Run 'gopcli.py -p' to generate token and to do an initial scan of your bulb network
3. If this succeeds, script away! 

### Current Features

- Blink mode to identify bulbs and rooms
- Added support for custom domains and .local prefix
- Get information about your rooms and bulbs
  (Room Name, Rid, Bulb Name, Did, On/Off Status, Dim Level, Offline Status)
- Set bulb/fixture on/off and dim level by did or bulb/fixture name
- Set room on/off and dim level by rid or room name
- Robust error checking and easy to read error messages
- Command line utility to access all API features

### Future Features and Work

- Interactive identification mode
- Add/remove bulb to room
- Toggle/dim everything at once
- Room/bulb renaming
- Improve performance
- Robustify
- Add tests
- Scenes

## Changelog

### 0.0.2 on Jan 26, 2015 by bdunlay

Greenwave/TCP updated firmware and removed HTTP service. This is a minor change to re-integrate pygop with greenwave's update.

- Added basic support for firmware version 3.0.74 (HTTPS-only), requires manual identification of gateway IP (GWR disabled domain service)
- Added settings page to hold custom configuration details such as gateway IPs; it should not be committed to the repo

## Fork notes

### Cron entries (setup using WD My Cloud DL2000)
`0 20 * * * python /home/root/pygop-tcp-light-control/turnRoomsOn.py & # Turn lights on every day at 8 PM`
`0 8 * * * python /home/root/pygop-tcp-light-control/turnRoomsOff.py & # Turn lights off every day at 8 AM`

### Commands:

#### Runs room report
`python test.py`

#### Sets all lights to DIM=65
`python setRoomsDim.py`

#### Turns all lights ON
`python turnRoomsOn.py`

#### Turns all lights OFF
`python turnRoomsOff.py`
