from collections import defaultdict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        report = SimpleReport.generate(products)
        companies = defaultdict(int)

        for product in products:
            companies[product["nome_da_empresa"]] += 1

        report += "\nProdutos estocados por empresa:\n"

        for company, count in companies.items():
            report += f"- {company}: {count}\n"

        return report
