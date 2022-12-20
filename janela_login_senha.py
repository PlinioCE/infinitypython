from PySimpleGUI import PySimpleGUI as jt

# Layout - Estrutura - Colunas e Linhas
jt.theme('Default1')
colunas_linhas = [
    [jt.Text('LOGIN:', size=(6, 1), justification='r'), jt.Input(key='login', size=(30, 1))],
    [jt.Text('SENHA:', size=(6, 1), justification='r'), jt.Input(key='senha', password_char='*', size=(30, 1))],
    [jt.Checkbox('Salvar Senha')],
    [jt.Button('ENTRAR', size=(16, 1)), jt.Button('SAIR', size=(16, 1))]
]

# Criar Janela
janela = jt.Window('Tela de Login', colunas_linhas)

# Eventos
while True:
    eventos, valores = janela.read()
    if eventos in ('SAIR', jt.WIN_CLOSED):
        break
    if eventos == 'ENTRAR':
        if valores['login'] == 'Plinio' and valores['senha'] == '123':
            jt.popup('ACESSO PERMITIDO!')
        else:
            jt.popup('ACESSO NEGADO!')
