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
            i_q0 = random.randint(1, 99)
            i_q1 = random.randint(1, 99)
            i_q2 = random.randint(1, 99)
            i_q3 = random.randint(1, 99)
            i_q4 = random.randint(1, 99)
            i_q5 = random.randint(1, 99)
            i_q6 = random.randint(1, 99)
            i_q7 = random.randint(1, 99)

            q0 = '1' if i_q0 <= 13 else ( random.randint(1,5) if i_q0 > 13 and i_q0 <= 65 else random.randint(5,7) )
            q1 = '1' if i_q1 <= 11 else ( random.randint(2,4) if i_q1 > 11 and i_q1 <= 40 else ( random.randint(3,6) if i_q1 > 40 and i_q1 <= 78 else random.randint(6,7) ))
            q2 = '1' if i_q2 <= 13 else ( random.randint(1,3) if i_q2 > 13 and i_q2 <= 32 else ( random.randint(3,6) if i_q2 > 32 and i_q2 <= 76 else random.randint(6,7) ))
            q3 = '1' if i_q3 <= 13 else ( random.randint(1,3) if i_q3 > 13 and i_q3 <= 40 else ( random.randint(3,6) if i_q3 > 40 and i_q3 <= 85 else random.randint(6,7) ))
            q4 = random.randint(1,2) if i_q4 <= 16 else ( random.randint(2,3) if i_q4 > 16 and i_q4 <= 34 else ( random.randint(3,6) if i_q4 > 34 and i_q4 <= 75 else random.randint(6,7) ))
            q5 = '1' if i_q5 <= 5 else ( random.randint(1,2) if i_q5 > 5 and i_q5 <= 20 else ( random.randint(2,5) if i_q5 > 20 and i_q5 <= 61 else random.randint(5,7) ))
            q6 = random.randint(1,2) if i_q6 <= 27 else ( random.randint(2,3) if i_q6 > 27 and i_q6 <= 40 else ( random.randint(3,6) if i_q6 > 40 and i_q6 <= 72 else random.randint(6,7) ))
            q7 = random.randint(1,3) if i_q7 <= 38 else ( random.randint(3,4) if i_q7 > 38 and i_q7 <= 47 else ( random.randint(4,7) if i_q7 > 47 and i_q7 <= 97 else '7' ))

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
    records = 150
    demographic_headers = ["ResponseID", "Email", "Gender", "Age","Text"]
    lickert_headers = ["ResponseID", "Q0", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"]
    demographicInfo(records, demographic_headers)
    lickertResponses(records, lickert_headers)
    print("CSV generation complete!")

