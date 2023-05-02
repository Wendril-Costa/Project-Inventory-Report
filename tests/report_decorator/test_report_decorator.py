from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import csv


def test_decorar_relatorio():
    report_decorator = ColoredReport(SimpleReport).generate(csv_list)
    antiga = "Data de fabricação mais antiga:"
    proxima = "Data de validade mais próxima:"
    produtos = "Empresa com mais produtos:"
    date1 = "2020-09-06"
    date2 = "2023-09-17"
    target = "Target Corporation"

    assert report_decorator == (
        f"\033[32m{antiga}\033[0m \033[36m{date1}\033[0m\n"
        f"\033[32m{proxima}\033[0m \033[36m{date2}\033[0m\n"
        f"\033[32m{produtos}\033[0m \033[31m{target}\033[0m"
    )


with open("inventory_report/data/inventory.csv") as file:
    csv_list = [row for row in csv.DictReader(file)]
