from time import sleep

c = ('\033[m',        # 0 - colorless
     '\033[0;30;41m'  # 1 - red
     '\033[0;30;42m', # 2 - green
     '\033[0;30;43m', # 3 - yellow
     '\033[0;30;44m', # 4 - blue
     '\033[0;30;45m', # 5 - purple
    )

def helpsystem(com):
    title(f'Accessing command manual \'{com}\'', 4)
    help(com)
    print(c[0], end='')
    sleep(2)
    

def title(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Main program
command = ''
while True:
    title('Pyhelp Help System', 2)
    command = str(input('Pyhelp: '))
    if command == 'exit':
        break
    else:
     helpsystem(command)
title('Goodbye', 1)