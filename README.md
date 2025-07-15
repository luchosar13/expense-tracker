# 💰 Expense Tracker

This project is based on an example from [roadmap.sh](https://roadmap.sh/projects/expense-tracker), designed to practice file handling, Python modules, and building Command Line Interfaces (CLI).

## 📌 Description

This is a CLI application for **personal expense management**. It allows you to:

- ✅ Add a new expense
- ✏️ Update an existing expense
- ❌ Delete an expense
- 📋 List of total expenses or by category
- 📊 Show a total or monthly summary

All data is stored in a local `expenses.csv` file.

---

## ⚙️ Requirements

- Python 3.10 or higher

---

## 🚀 Installation & Usage

### 🔧 Clone the Repository

```bash
git clone https://github.com/luchosar13/expense-tracker.git
cd expense-tracker
```
### 🕹 Use the commands
```bash
python expense-tracker.py add --description "Lunch" --amount 20

python expense-tracker.py add --description "Dinner" --amount 10

python expense-tracker.py list

python expense-tracker.py summary

python expense-tracker.py delete --id 2

python expense-tracker.py summary

python expense-tracker.py summary --month 8
```
For more information:
```bash
python expense-tracker.py --help
```
---

## ✅ Validations

The application includes several validations to ensure data consistency:

- **Positive Amount**: The `--amount` value must be greater than 0. A custom type validator is used to enforce this.
- **Valid Date Format**: The `--date` must follow the ISO format `YYYY-MM-DD`, otherwise it will raise an error.
- **Required Fields**:
  - `--amount` is required when adding a new expense.
  - `--id` is required for update and delete operations.
- **File Existence Check**: The program checks if `expenses.csv` exists before attempting updates or deletions. If it doesn’t exist, a message is shown.
- **Default Fallbacks**:
  - If no date is provided, the current date is used.
  - If no category is provided, "Others" is used as default.
- **Valid Month (1–12)**: In the `summary` command, the month must be an integer between 1 and 12.
- **Empty CSV Handling**: The program can handle the case where no expenses have been added yet.

---

## 🧪 Use Cases

Some practical use cases of this CLI tool:

- 📈 **Track Personal Spending**: Log all your daily or weekly expenses via terminal.
- 📁 **Organize by Category**: View spending patterns like how much you spent on groceries, entertainment, or travel.
- 🗓️ **Monthly Budgets**: Use the summary command to see monthly breakdowns of your expenses.
- 🧹 **Clean and Maintain Data**: Easily update or delete incorrect entries by referencing the expense ID.


