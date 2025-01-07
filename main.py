from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
import random
import re
import string

def criptText():
    while True:
        chave = Fernet.generate_key()
        fernet = Fernet(chave)

        texto = input("Digite o texto: ")
        textoCript = fernet.encrypt(texto.encode())
        print(f"Texto original: {texto}\nCriptografia - Base64: {textoCript}")
        try:
            salvar = int(input("Deseja salvar em um arquivo?\n1. Sim\n2. Não\n"))
        except:
            continue
        if salvar == 1:
            with open(f"{''.join(random.choices(string.ascii_letters+string.digits, k=10))}.txt", "wb") as arquivo:
                dados = arquivo.write(textoCript)
                print("Salvo com sucesso!")
                break
        else:
            try:
                gerarNovamente = int(input("Deseja gerar novamente?\n1. Sim\n2. Não\n"))
            except:
                continue
            if gerarNovamente == 1:
                pass
            else:
                break

def cript_file():
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    while True:
        try:
            file = input("Digite o nome do arquivo com extensão!: ")
            with open(f"{file}", "rb") as arquivo_read:
                dados = arquivo_read.read()
        except:
            print("Arquivo não encontrado!")
            continue
        with open(f"{''.join(random.choices(string.hexdigits, k=10))}{file}", "wb") as arquivo_write:
            criptografar = fernet.encrypt(dados)
            salvar = arquivo_write.write(criptografar)
            print("Arquivo criptografado com sucesso!")
        with open(f"{''.join(random.choices(string.hexdigits, k=10))}{file}.key", "wb") as chave_write:
            salvarChave = chave_write.write(chave)
            print("Chave salva com sucesso!")
            break

def gerarHash():
    while True:
        texto = input("Digite o texto: ")
        try:
            opcoes = int(input("Digite o tipo de hash:\n1. SHA256 \n2. SHA512\n3. MD5\n"))
        except:
            print("Digite um número!")
            continue
        if opcoes == 1:
            sha256 = hashes.Hash(hashes.SHA256())
            sha256.update(texto.encode())
            resultado256 = sha256.finalize()
            hex_256 = resultado256.hex()
            print(f"Texto original: {texto}\nSHA256: {hex_256}")
            salvar = int(input("Deseja salvar em um arquivo externo?\n1. Sim\n2. Não\n"))
            if salvar == 1:
                with open(f"{''.join(random.choices(string.hexdigits, k=10))}.txt", "w") as arquivo:
                    salvar = arquivo.write(f"Texto: {texto}\nSHA256: {hex_256}")
                    print("Salvo com sucesso!")
                    break
            else:
                break
        elif opcoes == 2:
            sha512 = hashes.Hash(hashes.SHA512())
            sha512.update(texto.encode())
            resultado512 = sha512.finalize()
            hex_512 = resultado512.hex()
            print(f"Texto original: {texto}\nSHA512: {hex_512}")
            salvar = int(input("Deseja salvar em um arquivo externo?\n1. Sim\n2. Não\n"))
            if salvar == 1:
                with open(f"{''.join(random.choices(string.hexdigits, k=10))}.txt", "w") as arquivo:
                    salvar = arquivo.write(f"Texto: {texto}\nSHA512: {hex_512}")
                    print("Salvo com sucesso!")
                    break
            else:
                break
        elif opcoes == 3:
            md5 = hashes.Hash(hashes.MD5())
            md5.update(texto.encode())
            resultadomd5 = md5.finalize()
            hex_md5 = resultadomd5.hex()
            print(f"Texto original: {texto}\nMD5: {hex_md5}")
            salvar = int(input("Deseja salvar em um arquivo externo?\n1. Sim\n2. Não\n"))
            if salvar == 1:
                with open(f"{''.join(random.choices(string.hexdigits, k=10))}.txt", "w") as arquivo:
                    salvar = arquivo.write(f"Texto: {texto}\nMD5: {hex_md5}")
                    print("Salvo com sucesso!")
                    break
            else:
                break
        else:
            break

def decript_file():
    while True:
        try:
            file_name_key = input("Digite o nome do arquivo que contém a chave com extensão!: ")
            with open(f"{file_name_key}", "rb") as arquivo_key:
                dados_key = arquivo_key.read()
        except:
            print("Digite o nome do arquivo corretamente!")
            continue
        try:
            file_name = input("Digite o nome do arquivo com extensão!: ")
            with open(f"{file_name}", "rb") as arquivo :
                dados = arquivo.read()
        except:
            print("Digite o nome do arquivo corretamente!")
            continue

        fernet = Fernet(dados_key)
        decrypt = fernet.decrypt(dados)

        file_saida = input("Digite o nome do arquivo de saída com extensão!: ")
        with open(f"{file_saida}", "wb") as arquivo_saida:
            salvar = arquivo_saida.write(decrypt)
            print("Salvo com sucesso!")
            break

def menu():
    while True:
        try:
            opcao = int(input("Digite um opção!\n1. Criptografar um texto.\n2. Criptografar um arquivo.\n3. Descriptografar um arquivo.\n4. Gerar uma hash.\n5. Outro encerra\n"))
        except:
            print("Digite uma opção válida")
            continue
        if opcao == 1:
            criptText()
            break
        elif opcao == 2:
            cript_file()
            break
        elif opcao == 3:
            decript_file()
            break
        elif opcao == 4:
            gerarHash()
            break
        else:
            print("Aplicação encerrada!")
            break

menu()