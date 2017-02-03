import csv
import os

from intuitRitChallenge.models import Accounts, Transaction

# TODO: Only run this script when files have changes

# for filename in glob.iglob('../transaction-data/*.csv'):

folder_name = 'transaction-data'


def convert_date(date):
    """
    Found a bug where transactions were listed as invalid dates,
    this method is to correct those entries
    :param date: incorrect/invalid dates
    :return: a corrected date
    """
    mdy = date.split("/")
    if mdy[1] == "32":
        mdy[1] = "31"
    return mdy[2] + "-" + mdy[0] + "-" + mdy[1]


def import_data():
    """
    This function is used to used to import the csv data in the files to
    their corresponding models in the database
    :return: void
    """
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
                        account = Accounts()
                        account.auth_id = int(row[0])
                        account.save()
                    transaction = Transaction()
                    transaction.owner = account
                    transaction.date = convert_date(row[1])
                    transaction.vendor = row[2]
                    transaction.amount = float(row[3])
                    transaction.location = row[4]
                    transaction.save()

            file.close()


def add_accounts():
    """
    The method can be used to only add the accounts to the database,
    without adding the transaction data
    :return:
    """
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
                        account = Accounts()
                        account.auth_id = int(row[0])
                        account.save()
                    else:
                        break


print("Starting script...")
add_accounts()
print("Script completed.")
