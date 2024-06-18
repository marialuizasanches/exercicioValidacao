class Cadastro:
  def __init__(self, nome, idade, saldo, statusCadastro, endereco):
      self._nome = None
      self._idade = None
      self._saldo = None
      self._statusCadastro = None
      self._endereco = None

      self.set_nome(nome)
      self.set_idade(idade)
      self.set_saldo(saldo)
      self.set_statusCadastro(statusCadastro)
      self.set_endereco(endereco)
#exercico 2
  def set_nome(self, nome):
      if len(nome) > 0:
          self._nome = nome
          print("Cadastro do nome feito.")
      else:
          print("Erro: Nome não pode ser vazio.")

  def set_idade(self, idade):
      if idade > 18:
          self._idade = idade
          print("Cadastro da idade feito.")
      else:
          print("Erro: Idade deve ser maior que 18 anos.")

  def set_saldo(self, saldo):
      if saldo >= 0:
          self._saldo = saldo
          print("Cadastro do saldo feito.")
      else:
          print("Erro: Saldo não pode ser negativo.")

  def set_statusCadastro(self, statusCadastro):
      if statusCadastro:
          self._statusCadastro = statusCadastro
          print("Cadastro do status feito.")
      else:
          print("Erro: Status deve ser verdadeiro.")

  def set_endereco(self, endereco):
      if len(endereco) >= 3:
          self._endereco = endereco
          print("Cadastro do endereço feito.")
      else:
          print("Erro: Endereço não pode ser vazio e precisa ter pelo menos 3 letras.")
#exercico 3
class Cadastro:
  def __init__(self, nome, idade, saldo, statusCadastro, endereco):
      self._nome = None
      self._idade = None
      self._saldo = None
      self._statusCadastro = None
      self._endereco = None

      self.set_nome(nome)
      self.set_idade(idade)
      self.set_saldo(saldo)
      self.set_statusCadastro(statusCadastro)
      self.set_endereco(endereco)

  def set_nome(self, nome):
      if len(nome) > 0:
          self._nome = nome
          print("Cadastro do nome feito.")
      else:
          print("Erro: Nome não pode ser vazio.")

  def set_idade(self, idade):
      if idade > 18:
          self._idade = idade
          print("Cadastro da idade feito.")
      else:
          print("Erro: Idade deve ser maior que 18 anos.")

  def set_saldo(self, saldo):
      if saldo >= 0:
          self._saldo = saldo
          print("Cadastro do saldo feito.")
      else:
          print("Erro: Saldo não pode ser negativo.")

  def set_statusCadastro(self, statusCadastro):
      if statusCadastro:
          self._statusCadastro = statusCadastro
          print("Cadastro do status feito.")
      else:
          print("Erro: Status deve ser verdadeiro.")

  def set_endereco(self, endereco):
      if len(endereco) >= 3:
          self._endereco = endereco
          print("Cadastro do endereço feito.")
      else:
          print("Erro: Endereço não pode ser vazio e precisa ter pelo menos 3 letras.")

# Exemplo de uso:
cadastro1 = Cadastro("João", 25, 100.0, True, "Rua ABC")
cadastro2 = Cadastro("", 17, -50.0, False, "R")
