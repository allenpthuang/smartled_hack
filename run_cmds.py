import asyncio
import time
from bleak import BleakClient

def log_info(text):
    print('[INFO] ' + text)

async def run_cmds(address, commands):
    log_info('START')
    async with BleakClient(address) as client:
        log_info('BT Connected')

        cmd_ptr = 0
        while cmd_ptr < len(commands):
            log_info(f'Running cmd #{cmd_ptr + 1}')
            cmd = commands[cmd_ptr]
            if 'goto' not in cmd:
                cmd_ptr += 1
            elif cmd['infinite'] or cmd['count'] > 0:
                cmd_ptr = cmd['goto']
                log_info(f'Going to cmd #{cmd_ptr + 1}...')
                if not cmd['infinite']:
                    cmd['count'] -= 1
                continue
            else:
                cmd_ptr += 1
                cmd['count'] = cmd['orig_count']
                log_info(f'Loop done! Count reset to {cmd["orig_count"]}.')
                continue

            model_number = await client.write_gatt_char(uuid, cmd['gatt_cmd'])
            if cmd['duration'] <= 0:
                while True:
                    time.sleep(10000000)
            else:
                time.sleep(cmd['duration'])

    log_info('END')

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
        'duration': 1 # sleep after this command (in seconds)
        }

cmd_3 = {
        'power': 'ff', # on
        'color': '0000ff', # blue
        'twinkle': '0001', # off
        'duration': 1 # sleep after this command (in seconds)
        }

cmd_4 = {
    'goto': 1,
    'infinite': False,
    'count': 3,
    'orig_count': 3
}

cmd_5 = {
    'goto': 0,
    'infinite': True,
    'count': -1,
    'orig_count': -1
}

# this runs like 1->2->3->4->(2->3)->4->(2->3)->4->(2->3)->4->5->1->....
cmds = [cmd_1, cmd_2, cmd_3, cmd_4, cmd_5]

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


