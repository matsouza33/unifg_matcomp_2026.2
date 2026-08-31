#Atividade Hands-on Integrada: Auditoria & RBAC
#Aluno: Mateus Luiz Bezerra Souza
#Curso: Ciências da Computação 

#Desafio 1 - Auditoria de Sensores:

# Dados brutos com duplicatas
alpha = ['SEN-01', 'SEN-02', 'SEN-03', 'SEN-05', 'SEN-08', 'SEN-01']
beta = ['SEN-03', 'SEN-04', 'SEN-05', 'SEN-06', 'SEN-09', 'SEN-04']

# 1. Deduplicar via set()
alpha_set = set(alpha)
beta_set = set(beta)

# 2. Total de sensores únicos (A U B)
total_unicos = alpha_set | beta_set

# 3. Sensores redundantes (A ∩ B)
redundantes = alpha_set & beta_set

# 4. Exclusivos da Malha Norte (A \ B)
exclusivos_norte = alpha_set - beta_set

# 5. Sensores sem sobreposição (A Δ B)
sem_sobreposicao = alpha_set ^ beta_set

print("Alpha deduplicado:", alpha_set)
print("Beta deduplicado:", beta_set)
print("Total de sensores únicos:", len(total_unicos), "->", total_unicos)
print("Sensores redundantes:", redundantes)
print("Exclusivos da Malha Norte:", exclusivos_norte)
print("Sensores sem sobreposição:", sem_sobreposicao)


#Desafio 2 - Controle de Acesso (RBAC):

U = {'READ', 'EXPORT', 'EDIT', 'DELETE', 'ADMIN'}

def can_execute(user_perms, action):
    return action in user_perms

def get_missing_perms(user_perms, req_perms):
    return req_perms - user_perms

# Teste: operator < admin (subconjunto estrito)
operator_perms = {'READ', 'EXPORT'}
admin_perms = {'READ', 'EXPORT', 'EDIT', 'DELETE', 'ADMIN'}

is_strict_subset = operator_perms < admin_perms
print("Operator é subconjunto estrito do admin?", is_strict_subset)

print(can_execute(operator_perms, 'EDIT'))       # False
print(get_missing_perms(operator_perms, {'EDIT', 'DELETE'}))  # {'EDIT', 'DELETE'}
