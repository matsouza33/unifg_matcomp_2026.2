# STARTED KIT: CONTROLADOR SAFETRAFFIC (AULA 3)

def decidir_sinal_verde(
        ambulancia: bool,
        fluxo_alto: bool,
        pedestre: bool,
        cancela_trem: bool
) -> bool:

    # A cancela ferroviária bloqueia qualquer avanço.
    if cancela_trem:
        return False
    
    # Ambulância têm prioridade quando a via está liberada.
    if ambulancia:
        return True

    # No fluxo comum, só libera se houver movimento e não se houver pedestre atravessando.
    return fluxo_alto and not pedestre

# Testes:

#Teste 1:
assert decidir_sinal_verde(True, False, True, False) is True

#Teste 2:   
assert decidir_sinal_verde(False, True, False, False) is True

#Teste 3:  
assert decidir_sinal_verde(False, True, True, False) is False

#Teste 4:  
assert decidir_sinal_verde(True, True, False, True) is False

#Teste 5:
assert decidir_sinal_verde(False, False, False, False) is False

print('SUCESSO: TODAS AS REGRAS LÓGICAS FORAM HOMOLOGADAS')