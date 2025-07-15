# 💰 Expense Tracker

This project is based on an example from [roadmap.sh](https://roadmap.sh), designed to practice file handling, Python modules, and building Command Line Interfaces (CLI).

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
git clone [https://github.com/your-username/expense-cli-manager.git](https://github.com/luchosar13/expense-tracker.git)
cd expense-cli-manager


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

