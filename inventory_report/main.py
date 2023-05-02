from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def print_report(report):
    sys.stdout.write(report)


def print_error(error):
    sys.stderr.write(str(error))


def import_data(importer, file_path, report_type):
    print_report(InventoryRefactor(importer).import_data(
        file_path, report_type
    ))


def get_importer(file_path):
    if file_path.endswith(".csv"):
        return CsvImporter()
    elif file_path.endswith(".json"):
        return JsonImporter()
    elif file_path.endswith(".xml"):
        return XmlImporter()


def main():
    try:
        file_path, report_type = sys.argv[1], sys.argv[2]
        import_data(get_importer(file_path), file_path, report_type)
    except IndexError:
        print_error("Verifique os argumentos\n")
