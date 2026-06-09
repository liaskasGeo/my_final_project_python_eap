"""
Γραφικό περιβάλλον της εφαρμογής Family Finance Manager.

"""

from datetime import date
import os
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
import pandas as pd


class FinanceApp:
    """Κλάση που περιέχει όλο το front κομμάτι της εφαρμογής."""

    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Family Finance Manager")
        self.root.geometry("980x640")
        self.root.minsize(900, 560)
        self.root.configure(bg="#f4f6f8")

        self.categories = [
            "Μισθός", "Ενοίκιο", "Επίδομα", "Τρόφιμα", "Λογαριασμοί",
            "Μετακινήσεις", "Διασκέδαση", "Δάνειο", "Υγεία", "Άλλο"
        ]

        # Χρησιμοποιείται για το sorting της στήλης ημερομηνίας.
        # Με κάθε click αλλάζει από newest first σε oldest first και αντίστροφα.
        self.date_sort_desc = True
        self.sort_mode = "id"

        self._setup_styles()
        self.show_login()

    def _setup_styles(self):
        """Ρυθμίζει απλά χρώματα και εμφάνιση για ttk widgets."""
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f4f6f8")
        style.configure("Card.TFrame", background="white", relief="flat")
        style.configure("TLabel", background="#f4f6f8", font=("Segoe UI", 10))
        style.configure("Card.TLabel", background="white", font=("Segoe UI", 10))
        style.configure("Title.TLabel", background="#f4f6f8", font=("Segoe UI", 18, "bold"), foreground="#263238")
        style.configure("Small.TLabel", background="#f4f6f8", font=("Segoe UI", 9), foreground="#607d8b")
        style.configure("Green.TLabel", background="white", font=("Segoe UI", 14, "bold"), foreground="#2e7d32")
        style.configure("Red.TLabel", background="white", font=("Segoe UI", 14, "bold"), foreground="#c62828")
        style.configure("Blue.TLabel", background="white", font=("Segoe UI", 14, "bold"), foreground="#1565c0")
        style.configure("TButton", font=("Segoe UI", 10), padding=7)
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=28, background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def clear_window(self):
        """Καθαρίζει όλα τα widgets από το παράθυρο."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login(self):
        """Εμφανίζει μία απλή οθόνη login."""
        self.clear_window()

        container = ttk.Frame(self.root, padding=30)
        container.pack(expand=True)

        card = ttk.Frame(container, style="Card.TFrame", padding=30)
        card.pack()

        ttk.Label(card, text="Family Finance Manager", style="Card.TLabel", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))
        ttk.Label(card, text="Username", style="Card.TLabel").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(card, text="Password", style="Card.TLabel").grid(row=2, column=0, sticky="w", pady=5)

        self.username_entry = ttk.Entry(card, width=28)
        self.password_entry = ttk.Entry(card, width=28, show="*")
        self.username_entry.grid(row=1, column=1, pady=5, padx=10)
        self.password_entry.grid(row=2, column=1, pady=5, padx=10)

        ttk.Button(card, text="Σύνδεση", command=self.login).grid(row=3, column=0, columnspan=2, pady=18, sticky="ew")
        ttk.Label(card, text="User/pass: demo / demo", style="Card.TLabel", foreground="#78909c").grid(row=4, column=0, columnspan=2)

    def login(self):
        """Ελέγχει τα στοιχεία login και ανοίγει την κύρια εφαρμογή."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if self.db.check_login(username, password):
            self.show_main_app()
        else:
            messagebox.showerror("Λάθος στοιχεία", "Το username ή password δεν είναι σωστό.")

    def show_main_app(self):
        """Δημιουργεί το βασικό παράθυρο της εφαρμογής."""
        self.clear_window()

        main = ttk.Frame(self.root, padding=18)
        main.pack(fill="both", expand=True)
        main.columnconfigure(0, weight=3)
        main.columnconfigure(1, weight=2)
        main.rowconfigure(3, weight=1)

        ttk.Label(main, text="Family Finance Manager", style="Title.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Button(main, text="Logout", command=self.logout).grid(row=0, column=1, sticky="e")
        ttk.Label(main, text="Εφαρμογή καταγραφής εσόδων και εξόδων", style="Small.TLabel").grid(row=1, column=0, sticky="w", pady=(0, 12))

        self.summary_frame = ttk.Frame(main)
        self.summary_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        for i in range(3):
            self.summary_frame.columnconfigure(i, weight=1)

        self.income_label = self._summary_card(self.summary_frame, 0, "Σύνολο εσόδων", "0.00 €", "Green.TLabel")
        self.expense_label = self._summary_card(self.summary_frame, 1, "Σύνολο εξόδων", "0.00 €", "Red.TLabel")
        self.balance_label = self._summary_card(self.summary_frame, 2, "Υπόλοιπο", "0.00 €", "Blue.TLabel")

        left = ttk.Frame(main, style="Card.TFrame", padding=15)
        left.grid(row=3, column=0, sticky="nsew", padx=(0, 10))
        left.columnconfigure(0, weight=1)
        left.rowconfigure(1, weight=1)

        right = ttk.Frame(main, style="Card.TFrame", padding=15)
        right.grid(row=3, column=1, sticky="nsew")

        self._build_form(right)
        self._build_table(left)

        actions = ttk.Frame(main)
        actions.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        ttk.Button(actions, text="Ανανέωση", command=self.load_transactions).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Διαγραφή επιλεγμένης", command=self.delete_selected).pack(side="left", padx=8)
        ttk.Button(actions, text="Γράφημα εξόδων", command=self.show_expense_chart).pack(side="left", padx=8)
        ttk.Button(actions, text="Export Excel", command=self.export_excel).pack(side="left", padx=8)

        self.load_transactions()

    def _summary_card(self, parent, column, title, value, style_name):
        """Φτιάχνει ένα απλό card για τα σύνολα."""
        card = ttk.Frame(parent, style="Card.TFrame", padding=15)
        card.grid(row=0, column=column, sticky="ew", padx=6)
        ttk.Label(card, text=title, style="Card.TLabel", foreground="#607d8b").pack(anchor="w")
        label = ttk.Label(card, text=value, style=style_name)
        label.pack(anchor="w", pady=(6, 0))
        return label

    def _build_form(self, parent):
        """Δημιουργεί τη φόρμα προσθήκης συναλλαγής."""
        ttk.Label(parent, text="Νέα συναλλαγή", style="Card.TLabel", font=("Segoe UI", 13, "bold")).pack(anchor="w", pady=(0, 12))

        ttk.Label(parent, text="Τύπος", style="Card.TLabel").pack(anchor="w")
        self.type_var = tk.StringVar(value="Έξοδο")
        type_combo = ttk.Combobox(parent, textvariable=self.type_var, values=["Έσοδο", "Έξοδο"], state="readonly")
        type_combo.pack(fill="x", pady=(2, 10))

        ttk.Label(parent, text="Κατηγορία", style="Card.TLabel").pack(anchor="w")
        self.category_var = tk.StringVar(value="Τρόφιμα")
        category_combo = ttk.Combobox(parent, textvariable=self.category_var, values=self.categories)
        category_combo.pack(fill="x", pady=(2, 10))

        ttk.Label(parent, text="Τίτλος", style="Card.TLabel").pack(anchor="w")
        self.title_entry = ttk.Entry(parent)
        self.title_entry.pack(fill="x", pady=(2, 10))

        ttk.Label(parent, text="Ποσό", style="Card.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(parent)
        self.amount_entry.pack(fill="x", pady=(2, 10))

        ttk.Label(parent, text="Ημερομηνία", style="Card.TLabel").pack(anchor="w")
        self.date_entry = ttk.Entry(parent)
        self.date_entry.insert(0, str(date.today()))
        self.date_entry.pack(fill="x", pady=(2, 15))

        ttk.Button(parent, text="Προσθήκη συναλλαγής", command=self.add_transaction).pack(fill="x")

    def _build_table(self, parent):
        """Δημιουργεί τον πίνακα συναλλαγών με scrollbar."""
        ttk.Label(parent, text="Συναλλαγές", style="Card.TLabel", font=("Segoe UI", 13, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columns = ("id", "type", "category", "title", "amount", "date")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings")
        headings = ["ID", "Τύπος", "Κατηγορία", "Τίτλος", "Ποσό", "Ημερομηνία"]
        widths = [50, 80, 120, 170, 90, 110]

        for col, heading, width in zip(columns, headings, widths):
            if col == "date":
                self.tree.heading(col, text=heading, command=self.sort_by_date)
            else:
                self.tree.heading(col, text=heading)
            self.tree.column(col, width=width, anchor="center")

        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        self.tree.tag_configure("income", foreground="#2e7d32")
        self.tree.tag_configure("expense", foreground="#c62828")

    def add_transaction(self):
        """Παίρνει τα στοιχεία από τη φόρμα και προσθέτει συναλλαγή στη βάση."""
        trans_type = self.type_var.get()
        category = self.category_var.get().strip()
        title = self.title_entry.get().strip()
        amount_text = self.amount_entry.get().strip().replace(",", ".")
        trans_date = self.date_entry.get().strip()

        if not category or not title or not amount_text or not trans_date:
            messagebox.showwarning("Προσοχή", "Συμπλήρωσε όλα τα πεδία.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Λάθος ποσό", "Το ποσό πρέπει να είναι θετικός αριθμός.")
            return

        self.db.add_transaction(trans_type, category, title, amount, trans_date)
        self.title_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.load_transactions()
        messagebox.showinfo("Ολοκληρώθηκε", "Η συναλλαγή προστέθηκε επιτυχώς.")

    def load_transactions(self):
        """Φορτώνει συναλλαγές, ανανεώνει πίνακα και σύνολα."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = self.db.get_transactions()

        if self.sort_mode == "date":
            rows = sorted(rows, key=lambda row: row[5], reverse=self.date_sort_desc)

        for row in rows:
            tag = "income" if row[1] == "Έσοδο" else "expense"
            shown_row = (row[0], row[1], row[2], row[3], f"{row[4]:.2f} €", row[5])
            self.tree.insert("", tk.END, values=shown_row, tags=(tag,))

        income, expenses, balance = self.db.get_summary()
        self.income_label.config(text=f"{income:.2f} €")
        self.expense_label.config(text=f"{expenses:.2f} €")
        self.balance_label.config(text=f"{balance:.2f} €")

    def sort_by_date(self):
        """Κάνει ταξινόμηση των συναλλαγών με βάση την ημερομηνία."""
        self.sort_mode = "date"
        self.date_sort_desc = not self.date_sort_desc
        self.load_transactions()

    def logout(self):
        """Επιστρέφει τον χρήστη στην οθόνη login."""
        self.show_login()

    def delete_selected(self):
        """Διαγράφει τη συναλλαγή που έχει επιλέξει ο χρήστης."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Προσοχή", "Επίλεξε πρώτα μία συναλλαγή.")
            return

        values = self.tree.item(selected[0], "values")
        transaction_id = values[0]

        if messagebox.askyesno("Επιβεβαίωση", "Θέλεις σίγουρα να διαγράψεις τη συναλλαγή;"):
            self.db.delete_transaction(transaction_id)
            self.load_transactions()

    def show_expense_chart(self):
        """Δείχνει γράφημα πίτας με τα έξοδα ανά κατηγορία."""
        data = self.db.get_expenses_by_category()
        if not data:
            messagebox.showinfo("Δεν υπάρχουν δεδομένα", "Δεν υπάρχουν έξοδα για γράφημα.")
            return

        labels = [row[0] for row in data]
        amounts = [row[1] for row in data]

        plt.figure(figsize=(7, 5))
        plt.pie(amounts, labels=labels, autopct="%1.1f%%")
        plt.title("Έξοδα ανά κατηγορία")
        plt.tight_layout()
        plt.show()

    def export_excel(self):
        """Εξάγει όλες τις συναλλαγές σε Excel στον φάκελο exports."""
        rows = self.db.get_transactions()
        if not rows:
            messagebox.showinfo("Δεν υπάρχουν δεδομένα", "Δεν υπάρχουν συναλλαγές για export.")
            return

        os.makedirs("exports", exist_ok=True)
        filename = os.path.join("exports", f"transactions_{date.today()}.xlsx")
        df = pd.DataFrame(rows, columns=["ID", "Τύπος", "Κατηγορία", "Τίτλος", "Ποσό", "Ημερομηνία"])
        df.to_excel(filename, index=False)
        messagebox.showinfo("Export", f"Το αρχείο δημιουργήθηκε:\n{filename}")

    def run(self):
        """Ξεκινάει το mainloop της tkinter."""
        self.root.mainloop()
