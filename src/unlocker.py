import psutil
from pywinhandle import find_handles, close_handle

TARGET_HANDLES = [
    {'type': 'Event', 'signature': 'StarCraft II Game Application'},
    {'type': 'Event', 'signature': 'StarCraft II Game Application (Global)'},
    {'type': 'Section', 'signature': 'StarCraft II'},
    {'type': 'Section', 'signature': 'StarCraft II IPC Mem'},
]


def get_process(name='SC2_x64.exe'):
    for proc in psutil.process_iter():
        if proc.name() == name:
            return proc


def main():
    process = get_process()
    if not process:
        print('Please run SC2 before running this script.')
        return
    for handle in find_handles(process_ids=[process.pid]):
        for target_handle in TARGET_HANDLES:
            if target_handle['type'] == handle['type'] and \
                    type(handle['name']) == str and \
                    handle['name'].endswith(target_handle['signature']):
                print(f'Closed: {target_handle["signature"]}')
                close_handle(handle['process_id'], handle['handle'])
                break
    print('Done. Now you can start another SC2 client.')


if __name__ == '__main__':
    main()
