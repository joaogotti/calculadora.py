# Importa o módulo unittest, que é utilizado para escrever e rodar testes unitários em Python.
import unittest

# Importa as funções adicionar, subtrair, multiplicar e dividir do módulo calculadora.
# Essas são as funções que serão testadas.
from calculadora import adicionar, subtrair, multiplicar, dividir, exponenciar

# Definição da classe TestCalculadora que herda de unittest.TestCase.
# Esta classe contém os métodos de teste para verificar o comportamento correto das funções da calculadora.
class TestCalculadora(unittest.TestCase):

    # Teste da função adicionar.
    # Este método irá testar se a função adicionar está retornando os valores esperados.
    def test_adicionar(self):
        # Verifica se adicionar(10, 5) retorna 15.
        # A função assertEqual compara o valor retornado pela função com o valor esperado (15).
        self.assertEqual(adicionar(10, 5), 15)

        # Verifica se adicionar(-1, 1) retorna 0.
        # Este teste verifica se a função funciona corretamente com números negativos.
        self.assertEqual(adicionar(-1, 1), 0)

        # Verifica se adicionar(-1, -1) retorna -2.
        # Teste para verificar a soma de dois números negativos.
        self.assertEqual(adicionar(-1, -1), -2)

    # Teste da função subtrair.
    # Atualmente, este teste está vazio, com o uso de 'pass' como placeholder.
    # Isso indica que a implementação do teste para a função subtrair será feita no futuro.
    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(-1, 1), -2)
        self.assertEqual(subtrair(-1, -1), 0)

    # Teste da função multiplicar.
    # Assim como o teste anterior, ainda não foi implementado.
    # Quando for implementado, verificará se a função multiplicar está funcionando corretamente.
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 5), 15)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(multiplicar(0, 5), 0)

    # Teste da função dividir.
    # Este teste também está vazio por enquanto, aguardando implementação futura.
    # Deve-se garantir que a função de divisão lide com casos como divisão por zero.
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(-10, -2), 5)
        self.assertEqual(dividir(0, 1), 0)

        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_exponenciar(self):
        self.assertEqual(exponenciar(2, 3), 8)   # 2^3 = 8
        self.assertEqual(exponenciar(5, 0), 1)   # 5^0 = 1
        self.assertEqual(exponenciar(-1, 3), -1) # (-1)^3 = -1
        self.assertEqual(exponenciar(-1, 2), 1)  # (-1)^2 = 1
        self.assertEqual(exponenciar(0, 5), 0)   # 0^5 = 0
        self.assertEqual(exponenciar(2, -2), 0.25)  # 2^(-2) = 1/4


# Bloco principal que verifica se o script está sendo executado diretamente.
# Se for o caso, ele chama unittest.main(), que roda todos os métodos de teste da classe TestCalculadora.
if __name__ == '__main__':
    unittest.main()
