"""
Αρχείο για τη βάση δεδομένων SQLite.
Η κλάση Database περιέχει όλες τις βασικές εντολές που χρειάζεται η εφαρμογή.
"""

import sqlite3
from datetime import date


class Database:
    """Απλή κλάση που χειρίζεται τη σύνδεση και τις εντολές της SQLite."""

    def __init__(self, db_name="database.db"):
        self.db_name = db_name

    def connect(self):
        """Δημιουργεί σύνδεση με τη βάση δεδομένων."""
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Δημιουργεί τους πίνακες users και transactions αν δεν υπάρχουν."""
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                transaction_date TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def create_default_user(self):
        """Δημιουργεί έναν demo χρήστη για απλό login: demo / demo."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
            ("demo", "demo")
        )
        conn.commit()
        conn.close()

    def check_login(self, username, password):
        """Ελέγχει αν υπάρχουν τα στοιχεία χρήστη στη βάση."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        user = cursor.fetchone()
        conn.close()
        return user is not None

    def add_transaction(self, trans_type, category, title, amount, trans_date=None):
        """Προσθέτει μία συναλλαγή εσόδου ή εξόδου."""
        if trans_date is None:
            trans_date = str(date.today())

        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (type, category, title, amount, transaction_date)
            VALUES (?, ?, ?, ?, ?)
        """, (trans_type, category, title, amount, trans_date))
        conn.commit()
        conn.close()

    def get_transactions(self):
        """Επιστρέφει όλες τις συναλλαγές από τη νεότερη προς την παλιότερη."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, type, category, title, amount, transaction_date
            FROM transactions
            ORDER BY id DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_transaction(self, transaction_id):
        """Διαγράφει μία συναλλαγή με βάση το id."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        conn.commit()
        conn.close()

    def get_summary(self):
        """Υπολογίζει σύνολα εσόδων, εξόδων και υπόλοιπο."""
        rows = self.get_transactions()
        income = sum(row[4] for row in rows if row[1] == "Έσοδο")
        expenses = sum(row[4] for row in rows if row[1] == "Έξοδο")
        balance = income - expenses
        return income, expenses, balance

    def get_expenses_by_category(self):
        """Επιστρέφει έξοδα ομαδοποιημένα ανά κατηγορία για το γράφημα."""
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM transactions
            WHERE type = 'Έξοδο'
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows
