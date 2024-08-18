from gerenciamento_mercado.mercado.mercado import Mercado
from gerenciamento_mercado.cliente.cliente import Cliente
from gerenciamento_mercado.fornecedor.fornecedor import Fornecedor
from gerenciamento_mercado.produto.produto import Produto
from gerenciamento_mercado.transacao.transacao import Transacao

# Exemplo de transação no mercado
if __name__ == "__main__":
    mercado = Mercado()

    cliente = Cliente("Carmen Portinho", "123456789", "Rua Pedro Pires, 123")
    mercado.adicionar_cliente(cliente)

    fornecedor = Fornecedor("Nestlé", "Av. Paulista, 125", "77.377.074/0001-76")
    produto = Produto("Arroz", [fornecedor], "Alimentos", 25)
    mercado.adicionar_produto(produto)

    transacao = Transacao(produto, cliente, 2)
    mercado.registrar_transacao(transacao)