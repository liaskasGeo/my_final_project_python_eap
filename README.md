Family Finance Manager

A Python application for tracking family income and expenses.

Installation
Extract the project folder from the ZIP file.
Open a terminal or Command Prompt (CMD) inside the project folder.
Install the required libraries:
pip install -r requirements.txt
Creating the EXE File

If the executable file does not already exist, you can create it by following these steps:

Open CMD in the project folder and run:

python -m PyInstaller --onefile --windowed main.py

After the process is complete, the main.exe file will be created inside the dist folder and can be executed directly.

Running the Application

Alternatively, you can run the application using:

python main.py
Login Credentials
Username: demo
Password: demo
Features
Demo user login
Add income and expense transactions
Predefined transaction categories
Display transactions in a table
Color-coded financial information:
Green for income
Red for expenses
Blue for the current balance
Delete selected transactions
Calculate total income, expenses, and balance
Expense breakdown by category using a pie chart
Export transactions to an Excel file
Store data in an SQLite database
Note

The application was kept relatively simple because the project was completed individually and within a limited timeframe. The main focus was on correctly implementing the core requirements and ensuring that the essential features worked as intended.

Family Finance Manager — Project Report
Project Title

Development of a Family Finance Management Application

Course: PLIPRO — Python Programming Project
Student: Georgios Liaskas
Student ID: std172636
Course Section: PLIPRO-ILE45-3 — Individual Project
Academic Year: 2025–2026

1. Application Overview
Purpose of the Application

The purpose of the application is to manage family finances using Python. It allows users to:

Record income.
Record expenses.
View transactions.
Delete existing records.
View statistics through charts.
Export data to an Excel file.
2. Technologies Used
Python: The main programming language used to develop the application.
Tkinter: Used to create the graphical user interface (GUI).
SQLite: Used to store the application's data in a database.
Matplotlib: Used to generate charts and visualize financial data.
Pandas / OpenPyXL: Used to export transaction data to Excel files.
3. Application Screens and Features
-----------------------------------------------------------

Εφαρμογή και λειτουργίες
Login Screen

<img width="573" height="429" alt="image" src="https://github.com/user-attachments/assets/206a089e-bb07-425b-bcce-e55115957ac1" />


-----------------------------------------------------------------------------------------------------------------------------------
Main App Screen

Δυνατότητες Εφαρμογής

• Προσθήκη νέων εσόδων και εξόδων

• Διαχείριση συναλλαγών ανά κατηγορία

• Διαγραφή επιλεγμένης συναλλαγής

• Υπολογισμός συνολικών εσόδων και εξόδων

• Εμφάνιση τρέχοντος υπολοίπου

• Αποθήκευση δεδομένων σε SQLite βάση

• Logout χρήστη

<img width="955" height="628" alt="image" src="https://github.com/user-attachments/assets/99205703-cb02-4d59-a31f-27d917358f08" />

Τύποι και Κατηγορίες

<img width="528" height="257" alt="image" src="https://github.com/user-attachments/assets/7dcf66e1-fb14-4bae-b759-f666c2efa5ed" />

-----------------------------------------------------------------------------------------------------------------------------------

Στατιστικά Στοιχεία και Export Excel

• Προβολή εξόδων ανά κατηγορία

• Γραφική αναπαράσταση δεδομένων με pie chart

• Εξαγωγή συναλλαγών σε αρχείο Excel

<img width="2269" height="1090" alt="image" src="https://github.com/user-attachments/assets/8031ee31-dfa1-4370-bcad-ab3aaa3fe985" />


-----------------------------------------------------------------------------------------------------------------------------------

Αποτελέσματα

• Ολοκληρώθηκε μια λειτουργική εφαρμογή διαχείρισης εσόδων 
και εξόδων.

• Παρά τις δυσκολίες και τον περιορισμένο χρόνο, υλοποιήθηκαν οι 
βασικές απαιτήσεις του project.

• Αποκτήθηκε εμπειρία σε Python, SQLite και ανάπτυξη γραφικού 
περιβάλλοντος.

• Η εργασία βοήθησε στην καλύτερη κατανόηση της οργάνωσης και 
ανάπτυξης μιας ολοκληρωμένης εφαρμογής






