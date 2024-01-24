# Generate some some sample synthetic PII Data to replicate the type of data the client would be sharing with LiveRamp. The client data is likely to differ in structure, this is purely for example purposes.
# Here we used Faker, please see here for documentation should you need to change the fields, etc...  https://faker.readthedocs.io/en/master/

from faker import Faker
import csv
import pandas as pd
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

fake = Faker('en_GB')  # 'en_GB' for English (United Kingdom)

def generate_fake_data(num_records):
    """
    Generate fake personal data records for testing or demonstration purposes.

    Parameters:
    - num_records (int): The number of fake records to generate.

    Returns:
    - list: A list of dictionaries, each representing a fake personal data record.
      Each dictionary has the following keys:
        - 'first_name' (str): Fake first name.
        - 'last_name' (str): Fake last name.
        - 'date_of_birth' (date): Fake date of birth within a reasonable age range.
        - 'postcode' (str): Fake UK postcode.

    Example:
    If num_records = 5, generate_fake_data(5) might return:
    [
        {'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': '1990-05-15', 'postcode': 'SW1A 1AA'},
        {'first_name': 'Jane', 'last_name': 'Smith', 'date_of_birth': '1985-10-22', 'postcode': 'EC1A 1BB'},
        {'first_name': 'Alice', 'last_name': 'Johnson', 'date_of_birth': '1978-12-05', 'postcode': 'W1A 1CA'},
        {'first_name': 'Bob', 'last_name': 'Brown', 'date_of_birth': '1982-08-31', 'postcode': 'NW1A 1DA'},
        {'first_name': 'Charlie', 'last_name': 'Davis', 'date_of_birth': '1995-04-18', 'postcode': 'SE1A 1EA'}
    ]
    """
    fake_data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        postcode = fake.postcode()
        
        fake_data.append({
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'postcode': postcode
        })

    return fake_data

def save_to_csv(fake_data, filename='fake_data.csv'):
    """
    Save fake personal data records to a CSV file.

    Parameters:
    - fake_data (list of dict): A list of dictionaries, each representing a fake personal data record.
      Each dictionary should have the following keys:
        - 'first_name' (str): Fake first name.
        - 'last_name' (str): Fake last name.
        - 'date_of_birth' (date): Fake date of birth within a reasonable age range.
        - 'postcode' (str): Fake UK postcode.
    - filename (str, optional): The name of the CSV file to be created. Defaults to 'fake_data.csv'.

    Returns:
    - None

    Example:
    If fake_data is a list of fake records and filename is 'output.csv', 
    save_to_csv(fake_data, 'output.csv') will create a CSV file with the following format:
    first_name,last_name,date_of_birth,postcode
    John,Doe,1990-05-15,SW1A 1AA
    Jane,Smith,1985-10-22,EC1A 1BB
    Alice,Johnson,1978-12-05,W1A 1CA
    Bob,Brown,1982-08-31,NW1A 1DA
    Charlie,Davis,1995-04-18,SE1A 1EA
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'date_of_birth', 'postcode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in fake_data:
            writer.writerow(record)

if __name__ == "__main__":
    num_records = 5  # Adjust the number of fake records you want
    fake_data = generate_fake_data(num_records)
    
    # Print fake data
    print("Generated Fake Data:")
    for record in fake_data:
        print(f"First Name: {record['first_name']}, Last Name: {record['last_name']}, "
              f"Date of Birth: {record['date_of_birth']}, Postcode: {record['postcode']}")

    # Save to CSV with a custom filename
    csv_filename = 'fake_data.csv'
    save_to_csv(fake_data, filename=csv_filename)
    print(f"\nFake Data saved to '{csv_filename}'")
