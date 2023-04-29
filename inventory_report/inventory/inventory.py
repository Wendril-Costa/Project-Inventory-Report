import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            products = list(reader)

        if report_type == "simples":
            report = SimpleReport.generate(products)
        elif report_type == "completo":
            report = CompleteReport.generate(products)
        else:
            raise ValueError("Esse tipo de relatório é inválido.")

        return report
