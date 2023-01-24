import rpyc
from pynput.keyboard import Key, Listener

proxy = rpyc.connect('localhost', 18866, config={'allow_public_attrs': True})

print('1 - Enviar mensagem para o piloto')
print('2 - Sair ')
op = input()
while(op != '2'):
    if(op == '1'):
        message = input()
        proxy.root.message_pilot(message)
    print('1 - Enviar mensagem para o piloto')
    print('2 - Sair ')
    op = input()