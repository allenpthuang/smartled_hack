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

