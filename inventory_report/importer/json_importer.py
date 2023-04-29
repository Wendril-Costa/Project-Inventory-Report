import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if '.json' not in file_path:
            raise ValueError('Arquivo inválido')
        with open(file_path, 'r') as file:
            return json.load(file)