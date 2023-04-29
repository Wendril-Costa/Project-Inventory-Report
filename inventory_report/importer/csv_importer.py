import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith('.csv'):
            raise ValueError('Arquivo inválido')

        with open(file_path, "r") as file:
            products = list(csv.DictReader(file))
        return products
