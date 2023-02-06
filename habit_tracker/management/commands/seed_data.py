# app_dir/management/commands/seed_data.py

from django.core.management.base import BaseCommand, CommandError

from habit_tracker.models import Habit, User
from config import settings
from faker import Faker

# To run this management command:
# python manage.py seed_data
class Command(BaseCommand):
    help = "Create some data for development"

    def add_arguments(self, parser):
        parser.add_argument('limit', nargs='?', default=100, type=int)


    def handle(self, *args, **options):
        if settings.DEBUG:

            user, created = User.objects.get_or_create(username="Belletrix")
            if created:
                user.set_password("badpassword")
                user.save()

            another_user, created = User.objects.get_or_create(username="Anton")
            if created:
                another_user.set_password("badpassword")
                another_user.save()

            fake = Faker()
            limit = options.get('limit')

            for _ in range(limit):
                Habit.objects.get_or_create(
                    title=fake.text(max_nb_chars=20),
                    goal=fake.random_digit_not_null(),
                    unit=fake.random_element(elements=("pages", "miles", "minutes", "times")),
                    owner=fake.random_element(elements=[user, another_user])
                )

            self.stdout.write(self.style.SUCCESS(f"{limit} objects added to database."))

        else:
            raise CommandError("This command only runs when DEBUG is set to True.")
