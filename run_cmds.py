import asyncio
import time
from bleak import BleakClient


async def run_cmds(address, commands):
    print('=== START ===')
    async with BleakClient(address) as client:
        print('=== connected ===')
        cmd_ptr = 0
        while cmd_ptr < len(commands):
            print(f'Running cmd #{cmd_ptr + 1}')
            cmd = commands[cmd_ptr]
            if 'goto' in cmd:
                cmd_ptr = cmd['goto']
                print(f'Going to cmd #{cmd_ptr + 1}...')
                continue
            else:
                cmd_ptr += 1

            model_number = await client.write_gatt_char(uuid, cmd['gatt_cmd'])
            if cmd['duration'] <= 0:
                while True:
                    time.sleep(10000000)
            else:
                time.sleep(cmd['duration'])

    print('=== END ===')

# destination address
address = '21:0a:00:06:5a:b2'
# attribute service
uuid = '0000ffb1-0000-1000-8000-00805f9b34fb'

# other parts have not been explored yet
cmd_tmpl = r'a5{power}01ff05{color}006400ff05{twinkle}ff010500aa'
cmd_1 = {
        'power': 'ff', # on
        'color': 'ff0000', # red
        'twinkle': '0004', # off
        'duration': 3.5 # sleep after this command (in seconds)
        }

cmd_2 = {
        'power': 'ff', # on
        'color': '00ff00', # green
        'twinkle': '0004', # off
        'duration': 7.5 # sleep after this command (in seconds)
        }

cmd_3 = {
        'power': 'ff', # on
        'color': '0000ff', # blue
        'twinkle': '0001', # off
        'duration': 5.5 # sleep after this command (in seconds)
        }

cmd_4 = {
    'goto': 1
}

cmds = [cmd_1, cmd_2, cmd_3, cmd_4]

commands = []
for cmd in cmds:
    if 'goto' in cmd:
        commands.append(cmd)
        continue
    duration = cmd['duration']
    cmd.pop('duration')

    command = {'gatt_cmd': bytes.fromhex(cmd_tmpl.format(**cmd)), 'duration': duration}
    commands.append(command)        


asyncio.run(run_cmds(address, commands))


