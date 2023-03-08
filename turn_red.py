import asyncio
import time
from bleak import BleakClient
from crccheck.crc import Crc8Maxim

# destination address
address = '21:0a:00:06:5a:b2'
# attribute service
uuid = '0000ffb1-0000-1000-8000-00805f9b34fb'

# other parts have not been explored yet
cmd_tmpl = r'a5{power}01ff05{color}006400ff05{twinkle}ff010500aa'
configs = {
        'power': 'ff', # on
        'color': 'ff0000', # red
        'twinkle': 'ff04' # on, speed 4
        }


async def send_cmd(address):
    async with BleakClient(address) as client:
        command = bytes.fromhex(cmd_tmpl.format(**configs))
        model_number = await client.write_gatt_char(uuid, command)


asyncio.run(send_cmd(address))


