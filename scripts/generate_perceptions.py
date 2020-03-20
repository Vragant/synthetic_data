import csv, random
from faker import Faker
from faker.providers import person
from faker.providers import lorem
from faker.providers import geo


def demographicInfo(records, headers):
    fake = Faker('es_MX')
    fake.add_provider(person)
    fake.add_provider(lorem)
    fake.add_provider(geo)

    with open("../data/demographic_info.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        resp_id = 0
        for i in range(records):
            response_id = resp_id
            gender = 'M' if random.randint(0, 1) == 0 else 'F'
            age = random.randint(12, 74)
            aesthetic = '' if random.randint(0, 7) == 0 else random.randint(1, 7)
            text = '' if random.randint(0, 7) == 0 else fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)
            writer.writerow({
                "ResponseID": response_id,
                "Email": fake.email(),
                "Gender": gender,
                "Age": age,
                "Text": text
            })
            resp_id = resp_id + 1


def lickertResponses(records, headers):

    with open("../data/lickert_responses.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        resp_id = 0
        for i in range(records):
            response_id = resp_id
            q0 = random.randint(5, 7)
            q1 = random.randint(5, 7)
            q2 = random.randint(4, 6)
            q3 = random.randint(4, 6)
            q4 = random.randint(2, 4)
            q5 = random.randint(4, 6)
            q6 = random.randint(5, 7)
            q7 = random.randint(4, 6)
            writer.writerow({
                "ResponseID": response_id,
                "Q0": q0,
                "Q1": q1,
                "Q2": q2,
                "Q3": q3,
                "Q4": q4,
                "Q5": q5,
                "Q6": q6,
                "Q7": q7
            })
            resp_id = resp_id + 1


if __name__ == '__main__':
    records = 50
    demographic_headers = ["ResponseID", "Email", "Gender", "Age","Text"]
    lickert_headers = ["ResponseID", "Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]
    demographicInfo(records, demographic_headers)
    lickertResponses(records, lickert_headers)
    print("CSV generation complete!")
