# __init__() é um método especial (também chamado de "método mágico"). 
# - Serve para inicializar os atributos do objeto.

# super( ) é uma função embutida do Python. 
# Ela retorna uma referência à superclasse da classe atual.
# - Usada para chamar métodos da classe pai, como __init__().


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'\n >> Características da pessoa:\n > nome: {self.nome}\n > idade: {self.idade} anos'

#print('\n---Cadastro de Pessoa---')
#nome_pessoa = input(f'Qual seu nome?: ')
#idade_pessoa = int(input(f'Quantos anos vc tem?: '))

#print(Pessoa(nome_pessoa, idade_pessoa).apresentar())

# Criou uma tipo(sim, um tipo) pessoa, que tem nome e idade, e um método apresentar que exibe uma mensagem com essas informações.












# CRIANDO A CLASSE ALUNO HERDANDO DE PESSOA

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie

    def apresentar(self):
        return f'\n >> Características do aluno:\n > nome: {self.nome}\n > idade: {self.idade} anos\n > série: {self.serie}'

print('\n---Cadastro do Aluno---')
nome_aluno = input(f'Qual seu nome?: ')
idade_aluno = int(input(f'Quantos anos vc tem?: '))
serie_aluno = int(input(f'Qual sua série?: '))

novo_aluno = Aluno(nome_aluno, idade_aluno, f'{serie_aluno}° ano')

print(novo_aluno.apresentar())
    















class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def apresentar(self):
        return f'\n > nome: {self.nome}\n > idade: {self.idade} anos\n > cargo: {self.cargo}'

print('\n---Cadastro de Funcionário---')
nome_funcionario = input(f'Qual seu nome?: ')
idade_funcionario = int(input(f'Quantos anos vc tem?: '))
cargo_funcionario = input(f'Qual seu cargo?: ')

# CRIANDO A CLASSE PROFESSOR HERDANDO DE FUNCIONARIO

if cargo_funcionario == 'professor':
    materia = input(f'Qual sua matéria?: ')
    class Professor(Funcionario):
        def __init__(self, nome, idade, cargo, materia):
            super().__init__(nome, idade, cargo)
            self.materia = materia

        def apresentar_prof(self):
            return f'\n > nome: {self.nome}\n > idade: {self.idade}\n > cargo: {self.cargo}\n > matéria: {self.materia}'
    
    # salvando os dados de professor numa variavel e exibindo esses dados
    novo_professor = Professor(nome_funcionario, idade_funcionario, cargo_funcionario, materia)
    print(novo_professor.apresentar_prof())
else:
    novo_funcionario = Funcionario(nome_funcionario, idade_funcionario, cargo_funcionario)
    print(novo_funcionario.apresentar())

















class Turma:
    def __init__(self, turma):
        self.turma = turma
        self.alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Pessoa):
            self.alunos.append(aluno)
        else:
            raise ValueError("Apenas objetos do tipo Pessoa podem ser adicionados como alunos.")
        
    def apresentar(self):
        return f'\n > Turma: {self.turma}\n > Alunos:\n' + '\n'.join(aluno.apresentar() for aluno in self.alunos)
    
    def listar_alunos(self):
        return [aluno.apresentar() for aluno in self.alunos]

# Execução
print('\n---Formação de Turma---')
nome_turma = input('Qual o nome da turma?: ')
nome_aluno0 = input('Nome do aluno: ')
idade_aluno0 = int(input('Idade do aluno: '))

# Criando objetos
turma = Turma(nome_turma)
aluno0 = Pessoa(nome_aluno0, idade_aluno0)

# Adicionando aluno à turma
turma.adicionar_aluno(aluno0)

# Apresentando turma
print(turma.apresentar())











class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def adicionar_turma(self, turma):
        if isinstance(turma, Turma):
            self.turmas.append(turma)
        else:
            raise ValueError("Apenas objetos do tipo Turma podem ser adicionados.")

    def listar_turmas(self):
        return [turma.nome for turma in self.turmas]

class Diretora(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def apresentar(self):
        return f"{super().apresentar()} Eu sou a diretora da escola."


