import sqlite3
import time

banco = sqlite3.connect('agenda.db')
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios 
(nome text, senha text, email text)""")

print('---> Cadastros <---'.center(15))
print('--- Versão 1.0 ---'.center(20))
print('-='*10)
while True:
    while True:
        print('\n')
        print('='*23)
        print('Escolha um opção abaixo:')
        print('[1] Criar novo usuário')
        print('[2] Consultar usuários')
        print('[3] Deletar um usuário')
        print('[4] Sair')
        print('='*23)
        print('\n')
        escolha = str(input('\nMinha escolha: '))
        time.sleep(0.5)
        if escolha in '1234':
            break
        else:
            print('Erro. Favor escolher uma opção válida.\n')

    if escolha in '1':
        nome = str(input('Digite o nome do usuário: ')).strip().capitalize()
        senha = str(input('Digite a senha do usuário: '))
        email = str(input('Digite o email do usuário: ')).lower()
        try:
            cursor.execute(f"""INSERT INTO usuarios VALUES('{nome}', '{senha}', '{email}')""")
            print(f'Os dados passados foram inseridos no banco de dados.')
            time.sleep(0.5)
        except sqlite3.Error as e:
            print(f'Não foi possível adicionar usuário: {e}')
            time.sleep(0.8)

    if escolha in '2':
        
        usuarios = cursor.execute("SELECT * FROM usuarios")

        for usuario in usuarios:
            print(usuario)
        time.sleep(1.5)

    if escolha in '3':
        user_delete = str(input("Digite o nome do usuário a ser deletado: ")).capitalize()
        try:
            cursor.execute(f"""
            DELETE FROM usuarios WHERE nome = '{user_delete}'""")
            print('Usuário deletado com sucesso.')
            time.sleep(0.5)
        except sqlite3.Error as erro:
            print(f'Não foi possível deletar o usuário: {erro}')
            time.sleep(0.5)
    banco.commit()        

    if escolha in '4':
        break

print('Fechando...')
time.sleep(3.5)

banco.commit()