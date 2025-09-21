
musicas = [
    {"titulo": "Song A", "artista": "X", "downloads": 100, "avaliacoes": [5, 4, 4, 5]},
    {"titulo": "Song B", "artista": "Y", "downloads": 200, "avaliacoes": [3, 4, 2]},
    {"titulo": "Song C", "artista": "X", "downloads": 150, "avaliacoes": [5, 5, 5]}
]


def media_avaliacoes(musicas):
    return {m["titulo"]: sum(m["avaliacoes"]) / len(m["avaliacoes"]) for m in musicas}


def artista_top_downloads(musicas):
    artistas = {}
    for m in musicas:
        artistas[m["artista"]] = artistas.get(m["artista"], 0) + m["downloads"]
    return max(artistas, key=artistas.get)


def ranking_musicas(musicas):
    return sorted(musicas, key=lambda m: sum(m["avaliacoes"]) / len(m["avaliacoes"]), reverse=True)

print(media_avaliacoes(musicas))          
print(artista_top_downloads(musicas))     
print([m["titulo"] for m in ranking_musicas(musicas)])  
