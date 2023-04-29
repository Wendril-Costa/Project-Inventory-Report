from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path_file, report_type):
        if path_file.endswith(".csv"):
            products_file = CsvImporter.import_data(path_file)

        elif path_file.endswith(".json"):
            products_file = JsonImporter.import_data(path_file)

        elif path_file.endswith(".xml"):
            products_file = XmlImporter.import_data(path_file)

        return Inventory.generate_report_by_type(report_type, products_file)

    @staticmethod
    def generate_report_by_type(report_type, products_file):
        if report_type == "simples":
            return SimpleReport.generate(products_file)
        elif report_type == "completo":
            return CompleteReport.generate(products_file)