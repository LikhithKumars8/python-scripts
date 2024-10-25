import pandas as pd
import os
from django.core.management.base import BaseCommand
from python_scripts.models import SalesData
from python_project.settings import BASE_DIR
import json

class Command(BaseCommand):
    help = 'Load orders from CSV files located in the FILES directory'

    def handle(self, *args, **kwargs):
        files_dir = self.get_files_directory()
        csv_files = self.get_csv_files(files_dir)

        for csv_file in csv_files:
            self.process_csv_file(os.path.join(files_dir, csv_file))

        self.stdout.write(self.style.SUCCESS('All orders processed successfully.'))

    def get_files_directory(self):
        files_dir = os.path.join(BASE_DIR, 'FILES')
        if not os.path.exists(files_dir):
            self.stdout.write(self.style.ERROR('FILES directory does not exist in the project root.'))
            raise FileNotFoundError('FILES directory not found.')
        return files_dir

    def get_csv_files(self, files_dir):
        return [f for f in os.listdir(files_dir) if f.endswith('.csv')]

    def process_csv_file(self, file_path):
        df = pd.read_csv(file_path)
        region = self.get_region_from_filename(os.path.basename(file_path).lower())

        if region:
            for _, row in df.iterrows():
                self.process_row(row, region)
        else:
            self.stdout.write(self.style.WARNING(f'Filename {os.path.basename(file_path)} does not match expected region names.'))

    def get_region_from_filename(self, filename):
        if 'order_region_a' in filename:
            return 'A'
        elif 'order_region_b' in filename:
            return 'B'
        return None

    def process_row(self, row, region):
        order_id = row['OrderId']
        order_item_id = row['OrderItemId']
        quantity_ordered = row['QuantityOrdered']
        item_price = row['ItemPrice']
        batch_id = row['batch_id']

        # Extracting the promotion discount from JSON
        promotion_discount = self.extract_discount_amount(row['PromotionDiscount'])

        net_sale = self.calculate_net_sale(quantity_ordered, item_price, promotion_discount)

        if net_sale > 0:
            self.save_order(order_id, order_item_id, batch_id, quantity_ordered, item_price, promotion_discount, region, net_sale)
        else:
            self.stdout.write(self.style.WARNING(f'Skipped order {order_id} due to non-positive net sale.'))

    def extract_discount_amount(self, promotion_discount_str):
        """
        Extract the amount from the promotion discount JSON string.
        """
        try:
            discount_data = json.loads(promotion_discount_str)
            return float(discount_data["Amount"]) if "Amount" in discount_data else 0.0
        except json.JSONDecodeError:
            self.stdout.write(self.style.WARNING(f'Invalid promotion discount format: {promotion_discount_str}. Defaulting to 0.'))
            return 0.0

    def calculate_net_sale(self, quantity_ordered, item_price, promotion_discount):
        total_sales = quantity_ordered * item_price
        return total_sales - promotion_discount

    def save_order(self, order_id, order_item_id, batch_id, quantity_ordered, item_price, promotion_discount, region, net_sale):
        if not SalesData.objects.filter(order_id=order_id).exists():
            order = SalesData(
                order_id=order_id,
                batch_id=batch_id,
                order_item_id=order_item_id,
                quantity_ordered=quantity_ordered,
                item_price=item_price,
                promotion_discount=promotion_discount,
                region=region,
                net_sale=net_sale
            )
            try:
                order.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully saved order {order_id}.'))
            except ValueError as e:
                self.stdout.write(self.style.WARNING(f'Skipped order {order_id}: {e}'))
        else:
            self.stdout.write(self.style.WARNING(f'Skipped duplicate order {order_id}.'))

"""
SQL queries
"""
#Count the Total Number of Records
"""
SELECT COUNT(*) AS total_records
FROM python_scripts_salesdata;
"""

#Find the total sales amount by region.
"""
SELECT region, SUM(quantity_ordered * item_price) AS total_sales
FROM python_scripts_salesdata
GROUP BY region;
"""

# Find average sales amount per transaction
"""
SELECT AVG(quantity_ordered * item_price) AS average_sales_per_transaction
FROM python_scripts_salesdata;
"""