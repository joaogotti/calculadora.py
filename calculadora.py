# Definição da função adicionar, que irá somar dois números.
# A função ainda não foi implementada, então usamos 'pass' temporariamente.
def adicionar(a, b):
    return a + b 

# Definição da função subtrair, que será responsável por subtrair o segundo número do primeiro.
# Assim como a função de adição, ainda não está implementada e usa 'pass' como placeholder.
def subtrair(a, b):
    return a - b 

# Definição da função multiplicar, que multiplicará dois números.
# Também não foi implementada ainda, e 'pass' é usado para marcar a implementação futura.
def multiplicar(a, b):
    return a * b 

# Definição da função dividir, que fará a divisão do primeiro número pelo segundo.
# Novamente, a função ainda não foi implementada, e 'pass' é utilizado.
# É importante que no futuro seja tratado o caso de divisão por zero.
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    
    return a / b 

def exponenciar(base, expoente):
    return base ** expoente

# Função principal da calculadora, responsável por interagir com o usuário e realizar operações.
def calculadora():
    # Exibe as opções de operação disponíveis para o usuário escolher.
    print("Selecione a operação.")
    print("1.Adição")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5. Exponenciação")

    # Recebe a escolha da operação do usuário.
    escolha = input("Digite a opção (1/2/3/4/5): ")

    # Solicita dois números do usuário e converte-os para o tipo float.
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Verifica qual operação foi selecionada pelo usuário.
    if escolha == '1':
        # Se o usuário escolheu adição, chama a função adicionar com os números inseridos e exibe o resultado.
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif escolha == '2':
        # Se o usuário escolheu subtração, chama a função subtrair e exibe o resultado.
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        # Se o usuário escolheu multiplicação, chama a função multiplicar e exibe o resultado.
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        # Se o usuário escolheu divisão, chama a função dividir e exibe o resultado.
        # No futuro, deve-se validar para evitar divisão por zero.
        try:
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        except ValueError as e:
            print(e)
    elif escolha == '5':
        print(f"{num1} ^ {num2} = {exponenciar(num1, num2)}")
    else:
        # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro.
        print("Opção inválida")

# Bloco principal, que executa a função 'calculadora' quando o script é executado diretamente.
if __name__ == "__main__":
    calculadora()
