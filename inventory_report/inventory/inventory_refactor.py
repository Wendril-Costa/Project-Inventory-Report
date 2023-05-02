from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def import_data(self, file_path, report_type):
        products = self.importer.import_data(file_path)
        self.data += products
        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)

    def __iter__(self):
        return InventoryIterator(self.data)
