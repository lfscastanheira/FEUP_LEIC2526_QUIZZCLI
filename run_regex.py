import json

data = json.load(open('subjects/ltw/ltw.json'))
print(f"Total initially: {len(data['questions'])}")

# First run add_regex_1
with open('add_regex_1.py') as f:
    exec(f.read())

print("Added regex 1")

# Patch add_regex_2.py
with open('add_regex_2.py', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = {
    396: {
        "A": "Lança um TypeError interno porque a engine requer que as matrizes de captura sejam estritas.",
        "B": "Devolve exclusivamente um boolean true se a variável original for iterativa no buffer global.",
        "C": "Retorna um array com o primeiro match completo e todos os seus grupos de captura internos.",
        "D": "A engine não faz iterativamente qualquer match porque match é exclusivo do DOM de lógicas."
    },
    397: {
        "A": "O parêntesis exige a ordem completa 'abc'; o colchete pesquisa apenas por a, b ou c isolado.",
        "B": "A sintaxe de matriz iterativa paralela inverte o parser no root log do motor síncrono web.",
        "C": "Avalias a sintaxe estritamente para iterar chaves de memória estritas num log paralelo base.",
        "D": "Nenhuma, tratam puramente as capturas nativas em lógicas iterativas em dicionários root log."
    },
    398: {
        "A": "O sinal de adição ou mais `+`, significando no estrito log de 1 a infinito síncrono root.",
        "B": "O marcador opcional interativo local `?` que converte a string num valor boolean puro de base.",
        "C": "O símbolo de asterisco `*` que dita ocorrência facultativa ou infinitas vezes consecutivas.",
        "D": "O grupo curvo isolado na lógica paralela e iterativamente associativo log síncrono raiz."
    },
    399: {
        "A": "A sintaxe síncrona base iterativa de lógicas nativas `/(a+)+$/` log array iterado perfeitamente.",
        "B": "A expressão limpa puramente iterativamente root `/^[a-zA-Z]+$/` estritamente paralela puros.",
        "C": "A sintaxe paralela estrita de lógicas `/(a|a)+/` iterativamente assíncronos root puramente.",
        "D": "Avalia o síncrono paralela puramente síncrona local raiz `/ (.*a){10}/` nativa paralela."
    },
    400: {
        "A": "Modifica o iterador para parar no primeiro limite de matriz raiz iterativa log local estritamente.",
        "B": "Força o ponto a tratar estritamente todos os carateres, incluindo todas as quebras de linha.",
        "C": "Garante perfeitamente matriz lógicas de root puramente nativas iterativas síncronos isoladamente.",
        "D": "Obriga a avaliação síncrona array puramente case-insensitive local de rotina iterativamente root."
    }
}

import re
# We just replace the questions array directly in data after running add_regex_2
with open('add_regex_2.py') as f:
    exec(f.read())

print("Added regex 2")

# Now re-open json, apply fixes to 396-400 and save
data2 = json.load(open('subjects/ltw/ltw.json'))
for q in data2['questions']:
    if q['id'] in fixes:
        q['options'] = fixes[q['id']]

with open('subjects/ltw/ltw.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f, ensure_ascii=False, indent=2)

print(f"Total finally: {len(data2['questions'])}")
