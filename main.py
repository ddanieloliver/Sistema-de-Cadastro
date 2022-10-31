# Daniel Vítor Oliveira Nascimento;
# 535840
import os
import datetime
#-------- Função para limpar terminal:
def clear(): os.system('cls')

OK = '\033[92m' #GREEN
ING = '\033[36m' #BLUE    
DESIGN = '\033[95m' #ROSA
DES = '\033[33m' #YELLOU
FAIL = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR


#------- MENU DE ACESSO:
def menu():
  print(f'''
* * * * * * {DESIGN}<Daniel's Club>{RESET} * * * * * *
*                                     *
* {ING}:) O que desejas fazer hoje?{RESET}        *
*                                     *
* {DES}[1]{RESET} Cadastrar cliente               *
* {DES}[2]{RESET} Mostrar dados do cliente        *
* {DES}[3]{RESET} Mostrar clientes cadastrados    *
* {DES}[4]{RESET} Gerar relatório dos clientes    *
* {DES}[0]{RESET} Sair                            *
*                                     *
* * * * * * * * * * * * * * * * * * * *
''')

#------ ENTRADA DE DADOS:
#------
# Cadastra cada novo cliente e o armazena
#------

def cadastrar():
  #------
  # Cria o arquivo que quero guardar os dados
  #------  
  arqClientes = open("clientes.txt", "a", encoding= 'UTF-8') #append

  #------
  # Declara o dicionário principal
  #------  
  nome = str(input("Insira o seu Nome Completo: "))
  login = str(input("Insira o seu login: "))
  
  novoCliente = {}
  novoCliente["nome"] = nome
  novoCliente["login"] = login

  #------
  # Inicia uma verificação antes de terminar o dicionério para evitar que o usuário perda tempo
  #------ 

  lerLogin = open("clientes.txt", "r", encoding= 'UTF-8')
  for linha in lerLogin.readlines():
    cadaLinha = eval(linha)
    if novoCliente['login'] == cadaLinha['login']:
        print(f"{FAIL}Login já em uso, por favor tente outro{RESET}")
        return

  senha = str(input("Insira a sua Senha: "))
  email = str(input("Insira o E-mail: "))
  nascimento= int(input("Insira a sua data de nascimento: "))
  numero = int(input("Insira o seu celular (xx)x xxxx-xxxx: "))
  endereco =  str(input("Insira Endereços para entrega com (rua, número, complemento, bairro, cidade, CEP, ponto de referencia): "))

  novoCliente["SENHA"] = senha
  novoCliente["email"] = email
  novoCliente["nascimento"] = nascimento
  novoCliente["numero"] = numero
  novoCliente["endereco"] = endereco
  #------
  # Cada dicionário "novoCliente" será armazenado em uma linha do arquivo
  #------ 
  
  arqClientes = open("clientes.txt", "a", encoding= 'UTF-8')
  arqClientes.writelines(f"{str(novoCliente)}\n")
  arqClientes.close()
  lerLogin.close()
  clear()
  print(f" {OK}********Cliente cadastrado com sucesso!******** {RESET}")


#------ SAÍDA DE DADOS:
#------
def mostrarDados():
  clear()
  #------
  # Pede o login do cliente para exibir seus dados
  #------ 
  loginDoCliente = str(input("Insira o seu login: "))
  clear()
  dadosClientes = open("clientes.txt", "r", encoding= 'UTF-8')
  #------
  # Abre o documento para leitura
  #------ 
  for linha in dadosClientes.readlines():
    cadaLinha = eval(linha)
    if loginDoCliente == cadaLinha['login']: # verifica se o cliente existe
      clear() 
      for dado in cadaLinha: 
        print(f"{dado} : {cadaLinha[dado]}") # cada chave e cada valor de cada dicionario da linha
      return        
  print(f"{FAIL}Cliente não encontrado!{RESET}")
  dadosClientes.close()
  return
  

def mostrarClientes():
  clear()
  mostrouCliente = False #variável para ver se algum cliente foi cadastrado
  mostraCliente = open("clientes.txt", "r", encoding= 'UTF-8')
  #------
  # Abre o documento para leitura
  #------ 
  for linha in mostraCliente.readlines():
    cadaLinha = eval(linha)    
    mostrouCliente = True
    print(f"{cadaLinha['nome']} - {cadaLinha['login']}") #vai passar por cada linha do meu arquivo e printar login e nome
  if mostrouCliente == False:
    print(f"{FAIL}Ainda não há clientes cadastrados...{RESET}")
  mostraCliente.close()
  

def relatorio():
  clear()
  #------
  # Abre o documento para leitura
  #------
  clientes = open("clientes.txt", "r", encoding= 'UTF-8')
  linhas = clientes.readlines()
  numeroDeClientes = len(linhas)
  relatorioClientes = open("relatorio.txt", "w", encoding= 'UTF-8') #Crio um novo arquivo para o relatório, que vai sobreescrever sempre que eu quiser
  relatorioClientes.write("Relatório de clientes\n\n")
  relatorioClientes.write(f"A loja Daniel's Club possui {numeroDeClientes} clientes que estão listados abaixo:\n\n")
  
  data = datetime.datetime.now()
  for i in range (numeroDeClientes): # passando por cada cliente cadastrado do meu relatorio clientes 
    relatorioClientes.write(f"{i + 1}. {eval(linhas[i])['nome']}\n")
  relatorioClientes.write(f"\nRussas, {data.day} de {data.month} de {data.year}")
  clientes.close()
  relatorioClientes.close()

#------
# Corpo principal do código
#------ 

while True:
  menu()
  opcao = int(input("Insira a opção: "))
  if opcao == 1:
    clear()
    cadastrar()
    pergunta = input(f"O que desejas fazer agora? {DES}[1]{RESET} Cadastrar novamente; {DES}[2]{RESET} Voltar; {DES}[0]{RESET} Sair; ")
    if pergunta =="1":
      clear()
      while pergunta == "1":
        clear()
        cadastrar()
        pergunta = input(f"O que desejas fazer agora? \n{DES}[1]{RESET} Cadastrar novamente; {DES}[2]{RESET} Voltar; {DES}[0]{RESET} Sair; ")
        clear()
    if pergunta =="2":
      clear()
      continue
    else:
      clear()
      print(f"{ING}Obrigado e volte sempre! ;){RESET}")
      break    
  elif opcao == 2:
    clear()
    mostrarDados()

  elif opcao == 3: 
    clear() 
    mostrarClientes()
  elif opcao == 4:
    clear()
    relatorio()
    print(f"{OK}Relatório Gerado!{RESET}")
  elif opcao == 0:
    clear()
    print(f"{ING}Obrigado e volte sempre! ;){RESET}")
    break
