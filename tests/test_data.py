from faker import Faker

fake = Faker()


def generate_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "address": fake.address(),
        "address2": fake.address(),
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "mobile_number": fake.phone_number(),
        "subject": fake.sentence(),
        "message": fake.paragraph(),
    }