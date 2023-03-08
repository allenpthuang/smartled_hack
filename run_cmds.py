import asyncio
import time
from bleak import BleakClient


async def run_cmds(address, commands):
    async with BleakClient(address) as client:
        for cmd in commands:
            model_number = await client.write_gatt_char(uuid, cmd['gatt_cmd'])
            if cmd['duration'] <= 0:
                while True:
                    time.sleep(10000000)
            else:
                time.sleep(cmd['duration'])

# destination address
address = '21:0a:00:06:5a:b2'
# attribute service
uuid = '0000ffb1-0000-1000-8000-00805f9b34fb'

# other parts have not been explored yet
cmd_tmpl = r'a5{power}01ff05{color}006400ff05{twinkle}ff010500aa'
config_1 = {
        'power': 'ff', # on
        'color': 'ff0000', # red
        'twinkle': 'ff04', # on, speed 4
        'duration': 3.5 # sleep after this command (in seconds)
        }

config_2 = {
        'power': 'ff', # on
        'color': '00ff00', # green
        'twinkle': 'ff01', # on, speed 1
        'duration': 7.5 # sleep after this command (in seconds)
        }

config_3 = {
        'power': 'ff', # on
        'color': '00ffff', # cyan
        'twinkle': '0001', # off
        'duration': 5.5 # sleep after this command (in seconds)
        }

configs = [config_1, config_2, config_3]

commands = []
for config in configs:
    duration = config['duration']
    config.pop('duration')

    cmd = {'gatt_cmd': bytes.fromhex(cmd_tmpl.format(**config)), 'duration': duration}
    commands.append(cmd)        


asyncio.run(run_cmds(address, commands))


