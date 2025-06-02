from django.core.management import BaseCommand

from ad.models import Ad


class Command(BaseCommand):
    help = "Clears dataset"

    def handle(self, *args, **kwargs):
        Ad.objects.all().delete()
