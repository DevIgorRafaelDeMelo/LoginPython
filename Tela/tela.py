import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='Senha')],
    [sg.Checkbox('Salva o login?')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login ' , layout)

while True:
    eventos, valores = janela.read()
    print(eventos)
    print(valores)
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'igor' and valores['senha'] == '123':
            print('Ben-vindo')