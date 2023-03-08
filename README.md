# smartled_hack
A reverse-engineering effort for Smart LED products.
This project provides tools to control off-the-shelf smart LED products.


## Hardware
- Raspberry Pi 3B+ (or any Linux/Bluetooth-capable devices)
- AKEPO Small Size 16W RGBW APP Twinkle Fiber Optic Lights (Amazon [link](https://www.amazon.com/dp/B0B67YTSYZ?ref=ppx_pop_mob_ap_share))

## Requirements
- Python libraries
  ```
  pip install asyncio bleak
  ```

## Preliminary Finding
- It is a Bluetooth GATT device
- Destination Address: `21:0a:00:06:5a:b2`
- Handle: `0x000d`
- UUID: `0000ffb1-0000-1000-8000-00805f9b34fb`
- Configs:
  * `power`: `00` or `ff` (off and on)
  * `color`: `ff0000` (red, in hex)
  * `twinkle`: `ff04` (on, speed 4)

## Demo
This device is the work by Wan-Chien Lin, featuring in LEDucation 2023.

![](pics/demo_green_red.gif)

## Packet Structure
total = 20 bytes
```
00: header 'a5'
01: power 'ff'/'00' (on/off)
02: ? manual or preset switch? 01 for manual 00 for preset
03: preset 0x00 - 0x13 (0 - 19, 20 presets). 0xff if manual?
04: speed 0x01 - 0x0a (1 - 10, 10 speeds) (seems not revelent in manual mode)
05: R 0x00 - 0xff (seems all 0x00 in preset mode)
06: G 0x00 - 0xff
07: B 0x00 - 0xff
08: ? 00 or ff
09: brightness 0x01 - 0x64 (1 - 100, 100 levels)
10: 0x00 (magic?)
11: 0xff (magic?)
12: 0x05 (magic?)
13: twinkle 0x00 or 0xff (off/on)
14: twinkle speed 0x01 - 0x04 (1 - 4, 4 speeds)
15: 0x00 or 0xff (meteor?)
16: 0x01 (meteor?)
17: 0x05 (meteor?)
18: 0x00 (meteor?)
19: 0xaa (meteor?)
```

## Command Template (WIP)
```
f'a5{power}{mode}{preset}{speed}{color}00{brightness}00ff05{twinkle}{twinkle_speed}ff010500aa'

where:
  power:          0x00 or 0xff (off or on)
  mode:           0x00 for preset; 0x01 for manual
  preset:         0x00 - 0x13 (0 - 19, 20 presets); 0xff if manual
  speed:          0x01 - 0x0a (1 - 10, 10 speeds)
  color (3 bytes): hex color value (0xRRGGBB)
  brightness:     0x01 - 0x64 (1 - 100, 100 levels)
  twinkle:        0x00 or 0xff (off or on)
  twinkle_speed:  0x01 - 0x04 (1 - 4, 4 speeds)
```
