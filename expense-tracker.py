import argparse, datetime
from functions.add import write_csv
from functions.update import update_expense
from functions.delete import delete_expense
from functions.utils import *
from functions.list_expenses import list_expenses, list_expenses_for_category
from functions.summary import summary_expenses, summary_per_month


parser = argparse.ArgumentParser(description='Expenses management, [add, update, delete] functions')
subparsers = parser.add_subparsers(dest='command', help='Subcommands: add, update, delete')

add_parser = subparsers.add_parser('add', help='Add a new expense')
update_parser = subparsers.add_parser('update', help='Update a expense')
delete_parser = subparsers.add_parser('delete', help='Delete a expense')
list_parser = subparsers.add_parser('list', help='List a expenses')
summary_parser = subparsers.add_parser('summary', help='Summary')

add_parser.add_argument('-d', '--description', type=str, help='Description of the amount', default='None', required=False)
add_parser.add_argument('-m', '--amount', type=positive_int, help='Amount spent', required=True)
add_parser.add_argument('-c', '--category', type=str, help='Category of the amount', default='Others', required=False)
add_parser.add_argument('-t', '--date', type=datetime.date.fromisoformat, help="The Start Date - format YYYY-MM-DD", required=False)
update_parser.add_argument('-i', '--id', type=int, help='Expense ID for the update', required=True)
update_parser.add_argument('-d', '--description', type=str, help='Update description of the expense', required=False)
update_parser.add_argument('-m', '--amount', type=int, help='Update Amount spent', required=False)
update_parser.add_argument('-t', '--date', type=datetime.date.fromisoformat, help='Update date', required=False)
update_parser.add_argument('-c', '--category', type=str, help='Update category', required=False)
delete_parser.add_argument('-i', '--id', type=int, help='ID to delete', required=True)
summary_parser.add_argument('-m', '--month', type=int, choices=range(1, 13), help='Summary per month', required=False)
list_parser.add_argument('-c', '--category', type=str, help='List per category', required=False)

args = parser.parse_args()

if args.command == 'add':
    write_csv(args.description, args.amount, args.category, args.date)

if args.command == 'update':
    update_expense(args.id, args.description, args.amount, args.date, args.category)

if args.command == 'delete':
    delete_expense(args.id)

if args.command == 'list' and args.category is None:
    list_expenses()

if args.command == 'summary' and args.month:
    summary_per_month(args.month)

if args.command == 'summary' and args.month is None:
    summary_expenses()

if args.command == 'list' and args.category:
    list_expenses_for_category(args.category)











