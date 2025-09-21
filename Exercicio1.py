
pedidos = [
    {"cliente": "João", "itens": [{"prato": "Pizza", "preco": 30}, {"prato": "Suco", "preco": 8}]},
    {"cliente": "Maria", "itens": [{"prato": "Hambúrguer", "preco": 25}, {"prato": "Suco", "preco": 8}]},
    {"cliente": "João", "itens": [{"prato": "Pizza", "preco": 30}]},
    {"cliente": "Ana", "itens": [{"prato": "Salada", "preco": 20}]}
]


def total_gasto(pedidos, cliente):
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            for item in pedido["itens"]:
                total += item["preco"]
    return total


def prato_mais_vendido(pedidos):
    contagem = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            contagem[prato] = contagem.get(prato, 0) + 1
    return max(contagem, key=contagem.get)

def ranking_clientes(pedidos):
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        gastos[cliente] = gastos.get(cliente, 0) + sum(item["preco"] for item in pedido["itens"])
    return sorted(gastos.items(), key=lambda x: x[1], reverse=True)[:3]


print(total_gasto(pedidos, "João"))     
print(prato_mais_vendido(pedidos))        
print(ranking_clientes(pedidos))          
