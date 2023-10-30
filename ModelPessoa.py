class ModelPessoa:

    def __init__(self): #Representa o método construtor
        self.cpf = 0
        self.nome = ""
        self.telefone = 0
        self.endereco = ""
        self.email = ""

    def cadastrarPessoa(self, cpf, nome, telefone, endereco, email):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def consultarPessoa(self):
        consulta = f"CPF: {self.cpf}\nNome: {self.nome}\n Telefone: {self.telefone}\n Endereco: {self.endereco}\n Email: {self.email}"
        return consulta

    def atualizarPessoa(self, opcao, dado):
        if opcao == 1:
            self.nome = dado
        elif  opcao == 2:
            self.telefone = dado
        elif opcao == 3:
            self.endereco = dado
        elif opcao == 4:
            self.email = dado

    def excluirPessoa(self):
        self.cpf = 0
        self.nome = ""
        self.telefone = 0
        self.endereco = ""
        self.email = ""

