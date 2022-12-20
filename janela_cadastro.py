import PySimpleGUI as sg

# cria duas variavel sem receber nada
usuario = ''
senha = ''


# BARRA DE PROGRESSO RESPONSAVEL PARA A TELA DE AUTENTICAÇAO CRANDO A CONTA
# LOGO DEPOIS DE CRIAR O USUARIO VAI APARECE CRIANDO A CONTA DO DO USUARIO
def progress_bar():
    sg.theme('LightBlue2')
    layout = [[sg.Text('Criando sua conta...')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
              [sg.Cancel()]]

    window = sg.Window('Trabalhando...', layout)
    for i in range(1000):
        evento, values = window.read(timeout=1)

        if evento == 'Cancel' or evento == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


# ---------------------------------------------------------------------------

# TELA DE CREDENCIAS DE USUARIO CRIAÇAO DO USUARIO
def create_account():
    global usuario, senha
    sg.theme('LightBlue2')
    layout = [[sg.Text("Inscrição", size=(79, 2), font=60, justification='c')],
              [sg.Text("E-mail:", size=(18, 1), font=16, justification='r'), sg.InputText(key='-email-', font=16)],
              [sg.Text("Confirmar e-mail:", size=(18, 1), font=16, justification='r'),
               sg.InputText(key='-remail-', font=16)],
              [sg.Text("Login:", size=(18, 1), font=16, justification='r'), sg.InputText(key='-usuario-', font=16)],
              [sg.Text("Senha:", size=(18, 1), font=16, justification='r'),
               sg.InputText(key='-senha-', font=16, password_char='*')],
              [sg.Button("Enviar"), sg.Button("Cancelar")]]

    window = sg.Window("Inscrição", layout)

    while True:
        evento, valores = window.read()
        if evento == 'Cancelar' or evento == sg.WIN_CLOSED:
            break
        else:
            if evento == "Enviar":
                senha = valores['-senha-']
                usuario = valores['-usuario-']
                if valores['-email-'] != valores['-remail-']:
                    sg.popup_error("Error", font=16)
                    continue
                elif valores['-email-'] == valores['-remail-']:
                    progress_bar()
                    break
    window.close()


create_account()


# ------------------------------------------------------------------------------------

# TELA DE LOGIN LOGO DEPOIS DA CRIAÇAO DO USUARIO VAI ENTRA ESSA TELA PARA O USUARIO LOGA
def login():
    global usuario, senha
    sg.theme("LightBlue2")
    layout = [[sg.Text("Iniciar sessão ", size=(15, 1), font=40)],
              [sg.Text("Login:", size=(15, 1), font=16, justification='r'), sg.InputText(key='-usrnm-', font=16)],
              [sg.Text("Senha:", size=(15, 1), font=16, justification='r'),
               sg.InputText(key='-pwd-', password_char='*', font=16)],
              [sg.Button('Ok'), sg.Button('Cancelar')]]

    window = sg.Window("Iniciar sessão", layout)

    while True:
        evento, valores = window.read()
        if evento == "Cancelar" or evento == sg.WIN_CLOSED:
            break
        else:
            if evento == "Ok":
                if valores['-usrnm-'] == usuario and valores['-pwd-'] == senha:
                    sg.popup("Bem-vindo!")
                    break
                elif valores['-usrnm-'] != usuario or valores['-pwd-'] != senha:
                    sg.popup("Login inválido. Tentar novamente")
    window.close()


login()
