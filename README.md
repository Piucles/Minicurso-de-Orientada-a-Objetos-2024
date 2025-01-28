# Curso de Orientação a Objetos 2024

Este repositório contém os códigos e exemplos desenvolvidos durante o curso de **Orientação a Objetos 2024**, ministrado pela Universidade Federal de Viçosa - Campus Rio Paranaíba. O objetivo do curso é introduzir conceitos fundamentais de programação orientada a objetos com exemplos práticos.

---

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Exercícios Implementados](#exercícios-implementados)
  - [Exercício 1: Olá Mundo](#exercício-1-olá-mundo)
  - [Exercício 2: Calculadora](#exercício-2-calculadora)
  - [Exercício 3: Construtores e Destrutores](#exercício-3-construtores-e-destrutores)
    
---

## Descrição do Projeto

O projeto contém exemplos práticos de implementação de conceitos de programação orientada a objetos, como encapsulamento, herança, polimorfismo, construtores e destrutores. Além disso, inclui exercícios básicos e intermediários desenvolvidos para consolidar o aprendizado.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.10 ou superior
- **Bibliotecas:** Nenhuma biblioteca externa (apenas bibliotecas nativas)

---

## Exercícios Implementados

### Exercício 1: Olá Mundo

Este é o exemplo inicial para garantir o funcionamento do ambiente de desenvolvimento Python. O código simplesmente imprime "Olá Mundo" no console.

### Exercício 2: Calculadora
Uma calculadora simples e interativa que realiza as seguintes operações matemáticas:

Soma
- Subtração
- Multiplicação
- Divisão
- Divisão Inteira
- Resto
- Exponenciação

O programa permite ao usuário selecionar a operação desejada por meio de um menu interativo e, em seguida, inserir os números necessários. Também trata casos de divisão por zero para evitar erros durante a execução. O loop principal continua até que o usuário decida encerrar.

### Exercício 3: Construtores e Destrutores

Nesta seção, implementamos dois conceitos principais utilizando a programação orientada a objetos:

#### Classe `Ponto`

A classe `Ponto` representa um ponto no espaço bidimensional (2D) com coordenadas `x` e `y`. Ela foi projetada para demonstrar:

- **Encapsulamento**: Os atributos `x` e `y` são privados, protegidos por convenção com underscores duplos (`__`), e são acessados por meio de métodos `getter` e `setter`.
- **Construtor**: O método especial `__init__` é utilizado para inicializar os valores das coordenadas durante a criação de um objeto.
- **Destrutor**: O método especial `__del__` é chamado automaticamente quando o objeto é destruído, permitindo executar ações específicas, como mensagens de log.
- **Sobrecarga de Operadores**:
  - `+`: Permite somar dois pontos retornando um novo ponto com as coordenadas somadas.
  - `==`: Permite comparar dois pontos e verificar se suas coordenadas são iguais.
- **Método `distancia`**: Um método adicional para calcular a distância euclidiana entre dois pontos no espaço 2D.

---

#### Classe `Ponto3D`

A classe `Ponto3D` expande a funcionalidade da classe `Ponto`, adicionando uma terceira coordenada `z` para representar pontos no espaço tridimensional (3D). Ela demonstra:

- **Herança**: A classe `Ponto3D` herda os métodos e atributos da classe `Ponto` e os estende.
- **Encapsulamento**: A coordenada `z` também é privada e acessada por métodos `getter` e `setter`.
- **Sobrecarga de Operadores**:
  - `+`: Permite somar dois pontos tridimensionais, retornando um novo ponto 3D.
  - `==`: Compara as coordenadas `x`, `y` e `z` para verificar se dois pontos 3D são iguais.
- **Método `distancia`**: Reimplementado para calcular a distância euclidiana entre dois pontos no espaço 3D.


