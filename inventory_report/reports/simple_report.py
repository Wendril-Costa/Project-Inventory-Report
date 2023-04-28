from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        today = datetime.now()

        oldest_fabrication_date = min(
            [
                datetime.fromisoformat(product["data_de_fabricacao"])
                for product in products
            ]
        ).strftime("%Y-%m-%d")

        closest_validity_date = min(
            [
                datetime.fromisoformat(product["data_de_validade"])
                for product in products
                if datetime.fromisoformat(product["data_de_validade"]) > today
            ]
        ).strftime("%Y-%m-%d")

        company_with_most_products = max(
            set([product["nome_da_empresa"] for product in products]),
            key=[product["nome_da_empresa"] for product in products].count,
        )

        report = f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
        report += f"Data de validade mais próxima: {closest_validity_date}\n"
        report += f"Empresa com mais produtos: {company_with_most_products}"
        return report
