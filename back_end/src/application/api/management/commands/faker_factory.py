
from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from application.models import Customer, ProductType, Product, PaymentType, Orders

# This file is executed as part of a larger migration/db reset that is executed by a script I added to my usr/local/bin called "django_data.sh". It takes 2 arguments: The name of the app to delete/add migrations from/to and the name of this file. FMI, look for a django-data repo in my account
class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(ProductType, 12)
    seeder.add_entity(Customer, 25)
    seeder.add_entity(PaymentType, 50, {'account_number': lambda x: random.randint(11111,99999)})
    # Override the seeder "guess" of what faker provider you want it to use
    seeder.add_entity(Product, 100, {'title': lambda x: seeder.faker.catch_phrase()})

    inserted_pks = seeder.execute()