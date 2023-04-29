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
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)

    @staticmethod
    def get_products(file_path):
        if file_path.endswith('.csv'):
            return CsvImporter.import_data(file_path)
        elif file_path.endswith('.json'):
            return JsonImporter.import_data(file_path)
        elif file_path.endswith('.xml'):
            return XmlImporter.import_data(file_path)
