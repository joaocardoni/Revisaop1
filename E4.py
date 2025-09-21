
filmes = [
    {"titulo": "Filme 1", "diretor": "Dir A", "bilheteria": 500, "avaliacoes": [8, 9, 10]},
    {"titulo": "Filme 2", "diretor": "Dir B", "bilheteria": 700, "avaliacoes": [7, 6, 8]},
    {"titulo": "Filme 3", "diretor": "Dir A", "bilheteria": 300, "avaliacoes": [9, 9, 8]},
    {"titulo": "Filme 4", "diretor": "Dir C", "bilheteria": 1000, "avaliacoes": [10, 9, 9]}
]


def top_bilheteria(filmes):
    return sorted(filmes, key=lambda f: f["bilheteria"], reverse=True)[:3]


def top_avaliacao(filmes):
    return sorted(filmes, key=lambda f: sum(f["avaliacoes"]) / len(f["avaliacoes"]), reverse=True)[:3]


def bilheteria_por_diretor(filmes):
    diretores = {}
    for f in filmes:
        diretores[f["diretor"]] = diretores.get(f["diretor"], 0) + f["bilheteria"]
    return diretores

def campeao(filmes):
    return max(filmes, key=lambda f: f["bilheteria"] * (sum(f["avaliacoes"]) / len(f["avaliacoes"])))


print([f["titulo"] for f in top_bilheteria(filmes)])  
print([f["titulo"] for f in top_avaliacao(filmes)])   
print(bilheteria_por_diretor(filmes))                 
print(campeao(filmes)["titulo"])                      
