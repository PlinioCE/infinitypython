import sqlalchemy

# criando o motor SQLAlchemy
from sqlalchemy import create_engine, select

# importa a declaração do banco de dados
from sqlalchemy.ext.declarative import declarative_base

# importa as propriedades da tabela
from sqlalchemy import Column, String, Integer

# criando uma sessão
from sqlalchemy.orm import sessionmaker

# criando a variável para receber a conexão
engine = create_engine('mysql+pymysql://root:@localhost:3306/loja_in')
print(engine)

# criando a conexão básica utilizando SQL puro
# conexao = engine.connect()
# resposta = conexao.execute('select * from usuario')
# resposta = engine.execute('select nome_usuario from usuario;')

# exibir dados do BD
# for contador in resposta:
#     print(contador.nome_usuario)

# criando super classe através do 'declarative_base'
Base = declarative_base()

# criando a variável da sessão
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


# ------------------------ INÍCIO ----------------------------
# criando SQL
while True:
    opcao = int(input('------------- BANCO DE DADOS -------------\n'
                      'Para manipular o BD escolha uma opção:\n'
                      '[1] - VISUALIZAR REGISTROS\n'
                      '[2] - INSERIR UM REGISTRO\n'
                      '[3] - EDITAR UM REGISTRO\n'
                      '[4] - EXCLUIR UM REGISTRO\n'
                      '[5] - SAIR\n'))
    if opcao == 2:
        # inserindo dados(insert)
        nome = str(input('Informe o nome: ')).title()
        endereco = str(input('Informe o endereço: '))
        idade = int(input('Informe a idade: '))
        print('Confira os dados antes de continuar!')
        inserir = str(input('Confirma o novo cadastro? [S/N]: ')).upper()
        if inserir[0] == 'S':
            banco_loja_in_insert = Usuario(nome_usuario=nome, endereco_usuario=endereco, idade_usuario=idade)
            session.add(banco_loja_in_insert)
            # modifica o banco
            session.commit()

    elif opcao == 1:
        # consulta = str(input('Deseja consultar os registros? [S/N]: ')).upper()
        # if consulta[0] == 'S':
        # consultando(select)
        banco_loja_in_select = session.query(Usuario).all()
        print(banco_loja_in_select)

    elif opcao == 4:
        apagar_registro = str(input('Informe o nome do registro a ser excluído: '))
        # apagando um registro (delete)
        apagar = str(input('Tem certeza que deseja excluir algum registro [S/N]: ')).upper()
        if apagar[0] == 'S':
            session.query(Usuario).filter(Usuario.nome_usuario == apagar_registro).delete()
            session.commit()

    elif opcao == 3:
        # editar = str(input('Deseja editar algum registro [S/N]: ')).upper()
        # if editar[0] == 'S':
        nome_registro = str(input('Informe o nome do registro a ser editado: ')).title()
        for nome in banco_loja_in_select:
            if nome_registro in nome.matricula_aluno:
                editar_registro = str(input('Informe o campo a ser editado [Nome, Endereço ou Idade]: ')).title()
                if editar_registro == 'Nome':
                    # editando um registro pelo nome (update)
                    novo_nome = str(input('Informe o novo nome: '))
                    session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update({'nome_usuario': novo_nome})
                    session.commit()
                elif editar_registro == 'Endereço':
                    # editando um registro pelo endereço (update)
                    novo_endereco = str(input('Informe o novo endereço: '))
                    session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update({'endereco_usuario': novo_endereco})
                    session.commit()
                elif editar_registro == 'Idade':
                    # editando um registro pela idade (update)
                    nova_idade = str(input('Informe a nova idade: '))
                    session.query(Usuario).filter(Usuario.nome_usuario == nome_registro).update({'idade_usuario': nova_idade})
                    session.commit()
                else:
                    print('Campo não encontrado!')
    elif opcao == 5:
        print('SAINDO DO SISTEMA...')
        break
    else:
        print('OPÇÃO INVÁLIDA!')
    print()
