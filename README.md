# 🏋️‍♂️ Projeto Caos – Simulando a Bagunça na Academia

Este projeto é uma simulação simples, divertida e estatisticamente interessante sobre **como usuários de academia — organizados e bagunceiros — afetam o "nível de caos" do porta-halteres** ao longo do dia.

A ideia nasceu daquele momento clássico na academia:

> “Por que diabos nunca tem um par de 20kg no lugar certo?”  
> — Eu, você, e todo mundo.

Aqui, transformamos essa revolta em **modelagem, simulação e distribuição estatística**.  

---

## 🎯 **Objetivo**

Simular o comportamento de usuários em uma academia, cada um com um nível de organização, e medir o quanto isso gera de **bagunça** no porta-halteres ao final do dia.

---

# 🧠 **Como funciona a simulação**

Existem dois tipos de usuários:

| Tipo | Descrição |
|------|-----------|
| `1` (normal) | devolve o halter no lugar correto — *se possível* |
| `2` (bagunceiro) | devolve no primeiro espaço aleatório que encontrar 😈 |

---

## 🧩 **Classes usadas**

### 🔹 `Academia`
Representa a estrutura do porta-halteres.

- Gera halteres de 10kg a 98kg (pares pares).
- Tem um dicionário `porta_halteres` onde:
  - chave = posição
  - valor = peso do halter
- Possui métodos para:
  - listar halteres disponíveis  
  - pegar halter  
  - devolver halter  
  - reiniciar o dia  
  - calcular o nível de caos (proporção de halteres fora do lugar)

### 🔹 `Usuario`
Representa uma pessoa treinando na academia.

- Tipo: `1` (organizado) ou `2` (bagunceiro)
- Métodos:
  - iniciar treino (pega um peso aleatório disponível)
  - finalizar treino (devolve no lugar certo ou em qualquer lugar, dependendo do tipo)

---

## 🔄 **Fluxo da Simulação**

Para cada dia:

1. Reinicia-se a organização dos halteres  
2. Usuários iniciam e finalizam seus treinos (10 ciclos)  
3. Ao final, calcula-se o nível de caos daquele dia  
4. Repete-se tudo por **1000 simulações**

Por fim:

- É calculada a **média do caos**  
- É gerado um gráfico da distribuição usando **seaborn**

---

## 📊 **Resultados**

O resultado final é um gráfico mostrando a distribuição do caos ao longo de 1000 simulações.

### 📊 O que é o “caos”?

É definido como:


número de halteres fora do lugar / total de posições do porta-halteres

Valores próximos de 0 → academia organizada  
Valores próximos de 1 → caos total

---

## 🙌 Créditos

Este projeto foi desenvolvido como exercício dentro do curso **“Programação Orientada a Objetos com Python” da Azimov Academy**, onde o professor apresenta este mesmo estudo como demonstração prática de simulação e análise.

A implementação aqui é a minha versão pessoal do projeto, com adaptações, organização de código e documentação próprias.
