import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if '.csv' not in file_path:
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as file:
            read_data = csv.DictReader(file, delimiter=',', quotechar='"')
            return list(read_data)
