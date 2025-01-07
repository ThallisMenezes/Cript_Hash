# Cript_Hash

## Bibliotecas
Este programa usa como base a biblioteca cryptography, além dos módulos Fernet, Hashes, re, string e random.

## Funções

### 1. `criptText()`
Esta função permite criptografar um texto fornecido pelo usuário. O processo de criptografia é feito usando o algoritmo **Fernet** da biblioteca `cryptography`. A função permite ao usuário escolher se deseja salvar o texto criptografado em um arquivo ou gerar uma nova criptografia.

**Passos:**
- O usuário insere um texto.
- O texto é criptografado utilizando uma chave gerada aleatoriamente.
- O texto criptografado é exibido em formato Base64.
- O usuário escolhe salvar o arquivo criptografado ou gerar uma nova criptografia.

### 2. `cript_file()`
Essa função permite criptografar um arquivo fornecido pelo usuário. A chave para criptografia é gerada aleatoriamente e é salva em um arquivo separado. O arquivo criptografado é salvo com um nome aleatório.

**Passos:**
- O usuário fornece o nome de um arquivo para ser criptografado.
- O arquivo é criptografado usando a chave gerada.
- O arquivo criptografado é salvo com um nome aleatório.
- A chave de criptografia é salva em um arquivo com um nome aleatório.

### 3. `gerarHash()`
Esta função gera hashes de um texto fornecido pelo usuário. O usuário pode escolher entre três algoritmos de hash: **SHA256**, **SHA512**, ou **MD5**. O hash gerado pode ser salvo em um arquivo externo.

**Passos:**
- O usuário insere um texto.
- O usuário escolhe o tipo de hash (SHA256, SHA512 ou MD5).
- O hash é gerado e exibido em formato hexadecimal.
- O usuário escolhe salvar o hash gerado em um arquivo.

### 4. `decript_file()`
Esta função permite descriptografar um arquivo usando uma chave fornecida pelo usuário. O arquivo criptografado e a chave devem ser fornecidos, e o arquivo descriptografado será salvo com um nome de saída especificado pelo usuário.

**Passos:**
- O usuário fornece o nome do arquivo que contém a chave de criptografia.
- O usuário fornece o nome do arquivo criptografado.
- O arquivo é descriptografado utilizando a chave fornecida.
- O arquivo descriptografado é salvo com um nome fornecido pelo usuário.

### 5. `menu()`
A função `menu()` serve como ponto de entrada para o programa, apresentando um menu interativo onde o usuário pode escolher entre várias opções de criptografia, hash ou descriptografia.

**Opções disponíveis:**
1. Criptografar um texto.
2. Criptografar um arquivo.
3. Descriptografar um arquivo.
4. Gerar uma hash.
5. Encerra o programa.

**Dependências:**
- `cryptography`: Para a criptografia e decriptação utilizando Fernet e para geração de hashes.
- `random`: Para a geração de nomes aleatórios de arquivos.
- `re` e `string`: Para manipulação de strings e geração de caracteres aleatórios.
