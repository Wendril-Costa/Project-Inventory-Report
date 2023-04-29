import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        products = Inventory._get_products(file_path)

        if report_type == "simples":
            report = SimpleReport.generate(products)
        elif report_type == "completo":
            report = CompleteReport.generate(products)

        return report

    @staticmethod
    def _get_products(file_path):
        extension = file_path.split(".")[-1]
        with open(file_path, "r") as file:
            if extension == "csv":
                products = list(csv.DictReader(file))
            elif extension == "json":
                products = json.load(file)
            elif extension == "xml":
                products = xmltodict.parse(file.read())["dataset"]["record"]
        return products
