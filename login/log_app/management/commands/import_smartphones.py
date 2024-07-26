import csv
from django.core.management.base import BaseCommand
from log_app.models import Device  

class Command(BaseCommand):
    help = 'Import smartphone data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Device.objects.create(
                    model=row['Model'],
                    brand=row['Brand'],
                    release_year=row['Release Year'],
                    os=row['OS'],
                    display_size=float(row['Display Size (inches)']),
                    ram=int(row['RAM (GB)']),
                    storage=int(row['Storage (GB)']),
                    battery_capacity=int(row['Battery Capacity (mAh)']),
                    main_camera=float(row['Main Camera (MP)']),
                    front_camera=float(row['Front Camera (MP)']), 
                    current_price=int(row['current_price']),
                    previous_price=int(row['previous_price']),
                    image=row['Image']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported smartphone data from CSV file'))
