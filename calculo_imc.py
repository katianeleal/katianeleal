def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Classifica o IMC de acordo com os intervalos especificados
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 24.9 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Exemplo de uso
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
```

### Explicação do código:

1. **Função `calcular_imc`**: Recebe o peso e a altura, calcula o IMC e retorna o valor.
2. **Função `classificar_imc`**: Recebe o valor do IMC e retorna a classificação de acordo com os intervalos especificados.
3. **Exemplo de uso**: Solicita ao usuário que insira seu peso e altura, calcula o IMC, classifica o resultado e imprime ambos.
