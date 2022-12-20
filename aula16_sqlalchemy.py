# criando o motor SQLAlchemy
from sqlalchemy import create_engine

# importa a declaração do banco de dados - Super Classe
from sqlalchemy.ext.declarative import declarative_base

# importa as propriedades da tabela
from sqlalchemy import Column, String, Integer

# criando uma sessão
from sqlalchemy.orm import sessionmaker

# criando a variável para receber a conexão ***ANTES DE RODAR O PROGRAMA, VERIFICAR O CAMINHO DO BANCO***
engine = create_engine('mysql+pymysql://root:@localhost:3306/loja_in')
print(engine)

# criando super classe através do 'declarative_base'
Base = declarative_base()

# criando a variável da sessão - SuperClasse - Consulta(SELECT) e Modificação(INSERT, UPDATE e DELETE)
Session = sessionmaker(bind=engine)
session = Session()


# criando Entidades(Classe)
class Usuario(Base):
    # criando a tabela
    __tablename__ = 'usuario'

    # criando os campos da tabela
    nome_usuario = Column(String, primary_key=True)
    endereco_usuario = Column(String, nullable=False)
    idade_usuario = Column(Integer)

    # método para exibir os dados
    def __repr__(self):
        return f'Nome: {self.nome_usuario}, ' \
               f'Endereço: {self.endereco_usuario}, ' \
               f'Idade: {self.idade_usuario}\n'


# --------------------------- INÍCIO -------------------------------
# criando SQL
while True:
    opcao = int(input('------------- BANCO DE DADOS -------------\n'
                      'Para manipular o BD escolha uma opção:\n'
                      '[1] - VISUALIZAR REGISTROS\n'
                      '[2] - INSERIR UM REGISTRO\n'
                      '[3] - EDITAR UM REGISTRO\n'
                      '[4] - EXCLUIR UM REGISTRO\n'
                      '[5] - SAIR DO SISTEMA\n'))
    match opcao:
        case 1:
            # consultando registros(select)
            banco_loja_in_select = session.query(Usuario).all()
            for dados in banco_loja_in_select:
                print(dados, end='')

        case 2:
            # inserindo registro(insert)
            nome = str(input('Informe o nome: ')).title()
            endereco = str(input('Informe o endereço: '))
            idade = int(input('Informe a idade: '))
            print('Confira os dados antes de continuar!')
            inserir = str(input('Confirma o novo cadastro? [S/N]: ')).upper()
            if inserir[0] == 'S':
                banco_loja_in_insert = Usuario(nome_usuario=nome, endereco_usuario=endereco, idade_usuario=idade)
                session.add(banco_loja_in_insert)

        case 3:
            nome_registro = str(input('Informe o nome do registro a ser editado: ')).title()
            for nome in banco_loja_in_select:
                if nome_registro in nome.nome_usuario:
                    editar_registro = str(input('Informe o campo a ser editado [Nome, Endereço ou Idade]: ')).title()
                    if editar_registro == 'Nome':
                        # editando um registro pelo nome (update)
                        novo_nome = str(input('Informe o novo nome: '))
                        session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update(
                            {'nome_usuario': novo_nome})
                    elif editar_registro == 'Endereço':
                        # editando um registro pelo endereço (update)
                        novo_endereco = str(input('Informe o novo endereço: '))
                        session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update(
                            {'endereco_usuario': novo_endereco})
                    elif editar_registro == 'Idade':
                        # editando um registro pela idade (update)
                        nova_idade = str(input('Informe a nova idade: '))
                        session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update(
                            {'idade_usuario': nova_idade})
                else:
                    print('Campo não encontrado!')

        case 4:
            apagar_registro = str(input('Informe o nome do registro a ser excluído: '))
            # apagando um registro (delete)
            apagar = str(input('Tem certeza que deseja excluir algum registro [S/N]: ')).upper()
            if apagar[0] == 'S':
                session.query(Usuario).filter(Usuario.nome_usuario == apagar_registro).delete()

        case 5:
            print('SAINDO DO SISTEMA...')
            break
        case _:
            print('OPÇÃO INVÁLIDA!')
    # aplica as modificações ao banco
    session.commit()
    print()
