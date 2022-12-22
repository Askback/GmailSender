from email.message import EmailMessage
import ssl
import smtplib
import os


def enviar_email(email_destino, assunto, corpo, email_origem, email_senha):
    e = EmailMessage()
    e['From'] = email_origem
    e['To'] = email_destino
    e['Subject'] = assunto
    e.set_content(corpo)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_origem, email_senha)
        smtp.sendmail(email_origem, email_destino, e.as_string())
        print("Mensagem enviada com sucesso! \n")
        smtp.close()
        exit()


def dados_email(email_origem, email_senha):
    email_destino = input("Email do destinatário: \n")
    assunto = input("Assunto do email: \n")
    corpo = input("Escreva sua mensagem: \n")
    enviar_email(email_destino, assunto, corpo, email_origem, email_senha)


def cadastrar_credenciais(email_origem):
    print("Não encontramos as credenciais, vamos cadastrar! \n")

    with open('token.txt', 'a') as arquivo:
        email_senha = input("Digite a senha de App Gmail: \n")
        arquivo.write("{},{}\n".format(email_origem, email_senha))


def verificacao(email_origem):
    if os.path.isfile('./token.txt'):
        with open('token.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                for linha in linhas:
                    detalhes = linha.strip().split(',')
                    email = detalhes[0]
                    senha = detalhes[1]
                    if email_origem == email:
                        print("Já encontramos seu email \n")
                        dados_email(email, senha)
                cadastrar_credenciais(email_origem)
            else:
                cadastrar_credenciais(email_origem)
    else:
        cadastrar_credenciais(email_origem)


def escolha(opcao):
    match opcao:
        case '1':
            email = input("Qual o seu email? \n")
            verificacao(email)
        case '0':
            exit()


def menu():
    print('1 - Enviar email')
    print('0 - Sair')
    print("\n")


while True:
    menu()
    escolha(input("Escolha uma opção \n"))










