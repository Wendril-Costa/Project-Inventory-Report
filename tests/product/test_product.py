from inventory_report.inventory.product import Product
from datetime import date


def test_cria_produto():
    produto = Product(
        id=1,
        nome_do_produto='frango',
        nome_da_empresa='Frigo',
        data_de_fabricacao=date(2022, 4, 1),
        data_de_validade=date(2023, 4, 1),
        numero_de_serie='123456',
        instrucoes_de_armazenamento='Seco e arejado',
    )

    assert produto.id == 1
    assert produto.nome_do_produto == 'frango'
    assert produto.nome_da_empresa == 'Frigo'
    assert produto.data_de_fabricacao == '2022-04-01'
    assert produto.data_de_validade == '2023-04-01'
    assert produto.numero_de_serie == '123456'
    assert produto.instrucoes_de_armazenamento == 'Seco e arejado'
