from .models import User
from faker import Faker
fake = Faker()

def seed_db(n):
    for i in range(0, n):
        User.objects.create(
            name = fake.name(),
            email = fake.email(),
            mobile = fake.phone_number()
        )