#### J. Tharcísio R. Lima, 09/24.

1. Criação de Dicionário:
```python
meu_dicionario = {}
meu_dicionario["nome"] = "Ana"
meu_dicionario["idade"] = 28
meu_dicionario["cidade"] = "São Paulo"
```

2. Acesso a Valores:
```python
print(meu_dicionario["nome"])
# print(meu_dicionario["endereço"]) # Gera KeyError
```

3. Verificação de Chaves:
```python
if "idade" in meu_dicionario:
    print("Idade está presente")
```

4. Atualização de Valores:
```python
meu_dicionario["idade"] = 29
print(meu_dicionario)
```

5. Remoção de Itens:
```python
del meu_dicionario["cidade"]
print(meu_dicionario)
```

6. Listas de Chaves e Valores:
```python
print(meu_dicionario.keys())
print(meu_dicionario.values())
```

7. Combinação de Dicionários:
```python
novo_dicionario = {"profissão": "Engenheira", "empresa": "TechCorp"}
meu_dicionario.update(novo_dicionario)
print(meu_dicionario)
```

8. Uso do Método get():
```python
print(meu_dicionario.get("profissão"))
print(meu_dicionario.get("salário", "N/A"))
```

9. Loop em Dicionários:
```python
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
```

10. Limpeza do Dicionário:
```python
meu_dicionario.clear()
print(meu_dicionario)
```

11. Contagem de Frequências:
```python
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem = {}
for fruta in frutas:
    contagem[fruta] = contagem.get(fruta, 0) + 1
print(contagem)
```

12. Dicionário de Quadrados:
```python
quadrados = {num: num**2 for num in range(1, 6)}
print(quadrados)
```

13. Ordenação de Chaves:
```python
numeros = {"três": 3, "um": 1, "dois": 2}
ordenado = dict(sorted(numeros.items()))
print(ordenado)
```

14. Explorando Métodos:
```python
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())    # Retorna as chaves
print(d.values())  # Retorna os valores
print(d.items())   # Retorna pares (chave, valor)
```

15. Usando defaultdict:
```python
from collections import defaultdict
d = defaultdict(lambda: "Não encontrado")
print(d["chave_inexistente"])
```