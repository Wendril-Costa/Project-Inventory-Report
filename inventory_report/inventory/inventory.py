from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        products = Inventory.get_products(file_path)

        if report_type == "simples":
            report = SimpleReport.generate(products)
        elif report_type == "completo":
            report = CompleteReport.generate(products)

        return report

    @staticmethod
    def get_products(file_path):
        extension = file_path.split(".")[-1]

        if extension == "csv":
            products = CsvImporter()
        elif extension == "json":
            products = JsonImporter()
        elif extension == "xml":
            products = XmlImporter()
        return products.import_data(file_path)
