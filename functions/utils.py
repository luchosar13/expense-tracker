import os, argparse

exist_file = os.path.exists('expenses.csv')

FILE_PATH = 'expenses.csv'


def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("The amount must be a positive number.")
    return ivalue


    