
atletas = [
    {"nome": "Carlos", "idade": 25, "modalidades": ["Futebol", "Natação"], "treinos": {"Futebol": 10, "Natação": 5}},
    {"nome": "Bruna", "idade": 30, "modalidades": ["Vôlei"], "treinos": {"Vôlei": 15}},
    {"nome": "Diego", "idade": 22, "modalidades": ["Futebol", "Basquete", "Natação"], "treinos": {"Futebol": 8, "Basquete": 12, "Natação": 3}}
]

def media_idade(atletas, esporte):
    praticantes = [a["idade"] for a in atletas if esporte in a["modalidades"]]
    return sum(praticantes) / len(praticantes) if praticantes else 0

def esporte_mais_treinado(atleta):
    return max(atleta["treinos"], key=atleta["treinos"].get)

def atletas_multiesporte(atletas):
    return [a["nome"] for a in atletas if len(a["modalidades"]) > 2]


print(media_idade(atletas, "Futebol"))       # 23.5
print(esporte_mais_treinado(atletas[2]))     # Basquete
print(atletas_multiesporte(atletas))         # ['Diego']
