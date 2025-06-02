import csv

from django.core.management import BaseCommand

from ad.models import Ad


class Command(BaseCommand):
    help = "Ads dataset from provided csv file"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f)
            next(reader)  # Skip the headers
            for row in reader:
                if not row[14]:
                    annual_condominium_fees = None
                else:
                    annual_condominium_fees = float(row[14])
                try:
                    Ad.objects.create(
                        url=row[1],
                        dept_code=row[3].replace(" ", "") or None,
                        zip_code=row[4].replace(" ", "") or None,
                        city=row[5],
                        annual_condominium_fees=annual_condominium_fees,
                    )
                except Exception as e:
                    print(f"Invalid data, skipping line: {e}")
