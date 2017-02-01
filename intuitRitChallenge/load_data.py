import csv
import os

from intuitRitChallenge.models import Account, Transaction

# TODO: Only run this script when files have changes

# for filename in glob.iglob('../transaction-data/*.csv'):

folder_name = 'transaction-data'


def convert_date(date):
    mdy = date.split("/")
    if mdy[1] == "32":
        mdy[1] = "31"
    return mdy[2] + "-" + mdy[0] + "-" + mdy[1]


def import_data():
    for filename in os.listdir(folder_name):
        if filename.endswith(".csv"):
            print(filename)

            file = open(folder_name + "/" + filename)
            data_reader = csv.reader(file)
            account = None

            for row in data_reader:
                if row[0] != 'auth_id':  # Ignore the header row, import everything else
                    if not account:
                        # Set the user's auth id for each file
                        account = Account()
                        account.auth_id = int(row[0])
                    transaction = Transaction()
                    transaction.owner = account
                    transaction.date = convert_date(row[1])
                    transaction.vendor = row[2]
                    transaction.amount = float(row[3])
                    transaction.location = row[4]
                    transaction.save()

            file.close()

print("Starting script...")
import_data()
print("Script completed.")
