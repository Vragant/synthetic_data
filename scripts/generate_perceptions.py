import csv, random
from faker import Faker
from faker.providers import person
from faker.providers import lorem
from faker.providers import geo


def datagenerate(records, headers):
    fake = Faker('es_MX')
    fake.add_provider(person)
    fake.add_provider(lorem)
    fake.add_provider(geo)

    with open("../data/perceptions_data.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            gender = 'M' if random.randint(0, 1) == 0 else 'F'
            aesthetic = '' if random.randint(0, 1) == 0 else random.randint(1, 7)
            utility = '' if random.randint(0, 1) == 0 else random.randint(1, 7)
            feeling = '' if random.randint(0, 1) == 0 else random.randint(1, 7)
            geographic = '' if random.randint(0, 1) == 0 else random.randint(1, 7)
            comparative = '' if random.randint(0, 1) == 0 else random.randint(1, 7)
            text = '' if random.randint(0, 1) == 0 else fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
            writer.writerow({
                "Email": fake.email(),
                "Gender": gender,
                "Aesthetic": aesthetic,
                "Utility": utility,
                "Feeling": feeling,
                "Geographic": geographic,
                "Comparative": comparative,
                "Location": fake.local_latlng(country_code="MX", coords_only=True),
                "Text": text
            })


if __name__ == '__main__':
    records = 70000
    headers = ["Email", "Gender", "Aesthetic", "Utility", "Feeling", "Geographic", "Comparative", "Location", "Text"]
    datagenerate(records, headers)
    print("CSV generation complete!")
