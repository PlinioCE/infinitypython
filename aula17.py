# criando o motor SQLAlchemy
from sqlalchemy import create_engine

# importa a declaração do banco de dados - Super Classe
from sqlalchemy.ext.declarative import declarative_base

# importa as propriedades da tabela
from sqlalchemy import Column, String, Integer

# criando uma sessão
from sqlalchemy.orm import sessionmaker

# criando a variável para receber a conexão ***ANTES DE RODAR O PROGRAMA, VERIFICAR O CAMINHO DO BANCO***
engine = create_engine('mysql+pymysql://root:@localhost:3306/escola714')
# print(engine)

# criando super classe através do 'declarative_base'
Base = declarative_base()

# criando a variável da sessão - SuperClasse - Consulta(SELECT) e Modificação(INSERT, UPDATE e DELETE)
Session = sessionmaker(bind=engine)
session = Session()


# criando Entidades(Classe)
class Aluno(Base):
    # criando a tabela
    __tablename__ = 'aluno'

    # criando os campos da tabela
    matricula_aluno = Column(Integer, primary_key=True)
    nome_aluno = Column(String, nullable=False)
    idade_aluno = Column(Integer, nullable=False)
    turma_aluno = Column(String)

    # método para exibir os dados
    def __repr__(self):
        return f'Matrícula: {self.matricula_aluno}, ' \
               f'Nome: {self.nome_aluno}, ' \
               f'Idade: {self.idade_aluno}, ' \
               f'Turma: {self.turma_aluno}\n'


# --------------------------- INÍCIO -------------------------------
# criando SQL
while True:
    opcao = int(input('------------- BANCO ESCOLA -------------\n'
                      'Para manipular o BD escolha uma opção:\n'
                      '[1] - VISUALIZAR REGISTRO\n'
                      '[2] - INSERIR UM REGISTRO\n'
                      '[3] - EDITAR UM REGISTRO\n'
                      '[4] - EXCLUIR UM REGISTRO\n'
                      '[5] - SAIR DO SISTEMA\n'))
    match opcao:
        case 1:
            tipo_select = int(input('Selecione uma opção:\n'
                                    '[1] - BUSCAR POR MATRÍCULA\n'
                                    '[2] - BUSCAR POR NOME\n'
                                    '[3] - VISUALIZAR TODOS\n'))
            match tipo_select:
                case 1:
                    matricula_registro = int(input('Informe a matrícula do(a) aluno(a): '))
                    banco_escola714_select = session.query(Aluno).all()
                    print(banco_escola714_select[matricula_registro - 1])
                    continue
                case 2:
                    nome_registro = str(input('Informe o nome do(a) aluno(a): ')).title()
                    banco_escola714_select = session.query(Aluno).filter({'nome_aluno': nome_registro})
                    print(banco_escola714_select)
                    continue
                case 3:
                    # consultando registros(select)
                    banco_escola714_select = session.query(Aluno).all()
                    for dados in banco_escola714_select:
                        print(dados, end='')
                    continue
                case _:
                    print('OPÇÃO INVÁLIDA!')
                    continue
        case 2:
            # inserindo registro(insert)
            matricula = int(input('Informe a matrícula do(a) aluno(a): '))
            nome = str(input('Informe o nome do(a) aluno(a): ')).title()
            idade = str(input('Informe a idade do(a) aluno(a): '))
            turma = int(input('Informe a turma do(a) aluno(a): '))
            print('Confira os dados antes de continuar!')
            inserir = str(input('Confirma o novo cadastro? [S/N]: ')).upper()
            if inserir[0] == 'S':
                banco_escola714_insert = Aluno(matricula_aluno=matricula, nome_aluno=nome, idade_usuario=idade, turma_aluno=turma)
                session.add(banco_escola714_insert)
        case 3:
            matricula_registro = str(input('Informe o nome do registro a ser editado: ')).title()
            for nome in banco_escola714_select:
                if matricula_registro in nome.matricula_aluno:
                    editar_registro = str(input('Informe o campo a ser editado [Nome, Endereço ou Idade]: ')).title()
                    if editar_registro == 'Nome':
                        # editando um registro pelo nome (update)
                        novo_nome = str(input('Informe o novo nome: '))
                        session.query(Aluno).filter(Aluno.matricula_aluno == matricula_registro).update(
                            {'nome_usuario': novo_nome})
                    elif editar_registro == 'Endereço':
                        # editando um registro pelo endereço (update)
                        novo_endereco = str(input('Informe o novo endereço: '))
                        session.query(Aluno).filter(Aluno.matricula_aluno == matricula_registro).update(
                            {'endereco_usuario': novo_endereco})
                    elif editar_registro == 'Idade':
                        # editando um registro pela idade (update)
                        nova_idade = str(input('Informe a nova idade: '))
                        session.query(Aluno).filter(Aluno.matricula_aluno == matricula_registro).update(
                            {'idade_usuario': nova_idade})
                else:
                    print('Campo não encontrado!')

        case 4:
            apagar_registro = str(input('Informe o nome do registro a ser excluído: '))
            # apagando um registro (delete)
            apagar = str(input('Tem certeza que deseja excluir algum registro [S/N]: ')).upper()
            if apagar[0] == 'S':
                session.query(Aluno).filter(Aluno.matricula_aluno == apagar_registro).delete()

        case 5:
            print('SAINDO DO SISTEMA...')
            break
        case _:
            print('OPÇÃO INVÁLIDA!')
    # aplica as modificações ao banco
    session.commit()
    print()
