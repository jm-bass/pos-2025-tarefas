import users as users

usuario = input("Digite 'l' para listar, 'c' para criar, 'r' para ler, 'u' para atualizar ou 'd' para excluir um usuário: ")
if usuario.lower() == 'l':
    users.list()
elif usuario.lower() == 'c':
    users.create()
elif usuario.lower() == 'r':
    users.read()
elif usuario.lower() == 'u':
    users.update()
elif usuario.lower() == 'd':
    users.delete()
else:
    print("Opção inválida. Por favor, escolha 'l', 'c', 'r', 'u' ou 'd'.")