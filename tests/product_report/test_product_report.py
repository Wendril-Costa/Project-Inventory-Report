import datetime
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=2,
        nome_do_produto="arroz",
        nome_da_empresa="Arrozeiro",
        data_de_fabricacao=datetime.date(2022, 1, 1),
        data_de_validade=datetime.date(2024, 1, 1),
        numero_de_serie="AR123",
        instrucoes_de_armazenamento="em local seco e fresco",
    )

    assert str(product) == (
        "O produto arroz"
        " fabricado em 2022-01-01"
        " por Arrozeiro com validade"
        " até 2024-01-01"
        " precisa ser armazenado em local seco e fresco."
    )
