
# WriteUp
[WriteUp.md](WriteUp.md)

## Installing and Running

### Essential Dependencies
To get the environment setup, your machine must include the following:

- python 3
- django 1.9

To determine if you have django 1.9, run the command in cmd:

`$ python -m django version`

If a number appears that is 1.9.1,
then you're all set

If not, run this command:

`$ python -m pip install django==1.9`

### Other Dependencies

If you would like the run the scripts that include machine learning
([machine_learning.py](intuitRitChallenge/scripts/machine_learning.py),
[visualize_data.py](intuitRitChallenge/scripts/visualize_data.py), and
[data_table.py](intuitRitChallenge/scripts/data_table.py)), you will
need the following dependencies:

- NumPy
- SciPy
- Scikit-learn

### Running

* To get the server running, download the code and extract it (or pull it)

* In any console, navigate to the top directory of the project. There
should be a file called manage.py in the folder.

* Then start the server by running the command in cmd:

`$ python manage.py runserver 8000`

You can now access the server at http://127.0.0.1:8000

## API
To access the api you have four options:

* Request a list of account numbers:
api/accounts

    - ex: http://127.0.0.1:8000/api/accounts


* Retrieve transactions for a given account:
api/transactions/<account_number>

    - ex: http://127.0.0.1:8000/api/transactions/624

* Retrieve features for a given account:
api/features/<account_number>

    - ex: http://127.0.0.1:8000/api/features/624

* Retrieve transactions for a given account:
api/matchmaker/<account_number>/<account_number>

    - ex: http://127.0.0.1:8000/api/matchmaker/624/1882

