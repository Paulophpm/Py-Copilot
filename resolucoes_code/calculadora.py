n1 = int(input("Digite o primeiro Número: "))
n2 = int(input("Digite o segundo Número: "))
op = int(input("Qual operação deseja realiza? 1:[+] 2:[-] 3[*] 4[/]"))

if op == 1:
    print(n1+n2)
elif op == 2:
    print(n1-n2)
elif op == 3:
    print(n1*n2)
elif op == 4:
    print(n1/n2)
else:
    print("Digite um número válido")

