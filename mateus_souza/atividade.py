from itertools import product

# PARTE 1: EXERCÍCIOS TEÓRICOS

# 1º EXERCÍCIO: Operações com conjuntos

U = set(range(1, 11))
A = {n for n in U if n % 2 == 0}
B = {n for n in U if n > 1 and all(n % d != 0 for d in range(2, n))}

a_uniao_b = A | B

a_inter_b = A & B

a_menos_b = A - B

comp_uniao = U - a_uniao_b

comp_a = U - A
comp_b = U - B
assert comp_uniao == comp_a & comp_b

assert a_uniao_b == {2, 3, 4, 5, 6, 7, 8, 10}
assert a_inter_b == {2}
assert a_menos_b == {4, 6, 8, 10}
assert comp_uniao == {1, 9}

print("=== PARTE 1 | 1º EXERCÍCIO ===")
print("U =", sorted(U))
print("A =", sorted(A))
print("B =", sorted(B))
print("(a) A ∪ B    =", sorted(a_uniao_b))
print("(b) A ∩ B    =", sorted(a_inter_b))
print("(c) A - B    =", sorted(a_menos_b))
print("(d) (A ∪ B)' =", sorted(comp_uniao))
print()


# 2º EXERCÍCIO: Simplificação de (A ∩ B) ∪ (A ∩ B')

original = (A & B) | (A & comp_b)
passo_1 = A & (B | comp_b)
passo_2 = A & U
resultado = A

# Os quatro estágios têm de dar o mesmo conjunto.
assert original == passo_1 == passo_2 == resultado


print("=== PARTE 1 | 2º EXERCÍCIO ===")
print("Expressão original =", sorted(original))
print("Após distributiva  =", sorted(passo_1))
print("Resultado final    =", sorted(resultado))
print()

# 3º EXERCÍCIO: Colisões de hash no set do CPython e busca O(1) médio
'''
Estrutura:
- O set é uma tabela hash com endereçamento aberto: não há listas ligadas.
  Cada posição (slot) guarda o hash e a referência do objeto.
- O tamanho da tabela é sempre potência de 2 (mínimo 8), então o índice
  inicial sai de uma operação de bits barata: indice = hash & (tamanho - 1).

Numa colisão (dois elementos caem no mesmo slot):
1. Sondagem linear curta: testa até 9 slots vizinhos, aproveitando o cache
   da CPU porque ficam próximos na memória.
2. Se não achar, usa perturbação: mistura os bits altos do hash
   (perturb >>= 5) para calcular um novo índice. Hashes que colidem no
   começo tendem a seguir caminhos diferentes.
3. Em cada slot ocupado, compara primeiro o hash guardado (barato), depois
   a identidade (is) e só então __eq__ (caro).

Remoção:
- O slot não é esvaziado: vira um marcador "dummy". Se fosse esvaziado, a
  cadeia de sondagem de outros elementos quebraria e a busca falharia.

Redimensionamento:
- Quando ocupados + dummies passam de cerca de 60% da tabela, ela é
  reconstruída maior. Crescimento geométrico => inserção O(1) amortizado.

Por que a busca é O(1) em média:
- Com boa função de hash e ocupação de no máximo ~60%, o número esperado de
  slots testados por busca é constante e não depende de n.
- Strings usam SipHash com sal aleatório por execução, o que dificulta
  gerar colisões de propósito.

Pior caso:
- Se muitos elementos tiverem o mesmo hash (um __hash__ mal feito), todos
  seguem a mesma sondagem e a busca degrada para O(n).
'''


# PARTE 2: DESAFIO PRÁTICO EM PYTHON

def detectar_rotas_circulares(linhas: dict[str, list[str]]) -> set[tuple[str, str]]:

    estacoes = set(linhas) | {d for destinos in linhas.values() for d in destinos}

    pares_possiveis = set(product(estacoes, repeat=2))

    ligacoes = {(o, d) for o, destinos in linhas.items() for d in destinos}

    ida = ligacoes & pares_possiveis

    volta = {(d, o) for o, d in ida}

    bidirecionais = ida & volta

    return {tuple(sorted(par)) for par in bidirecionais if par[0] != par[1]}


# TESTE DA PARTE 2

rede = {
    "Centro": ["Praça", "Porto"],
    "Praça": ["Centro", "Feira"],
    "Porto": ["Centro"],
    "Feira": ["Praça", "Aeroporto"],   
    "Aeroporto": [],
    "Rodoviária": ["Centro"],          
}

rotas = detectar_rotas_circulares(rede)

assert rotas == {("Centro", "Porto"), ("Centro", "Praça"), ("Feira", "Praça")}
assert detectar_rotas_circulares({}) == set()

print("=== PARTE 2 ===")
print("Conexões bidirecionais:")
for rota in sorted(rotas):
    print(rota)