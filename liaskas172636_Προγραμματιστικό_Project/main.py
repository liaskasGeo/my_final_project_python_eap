"""
Family Finance Manager - εφαρμογή για διαχείριση οικογενειακών οικονομικών.
Ξεκινάει το γραφικό περιβάλλον της εφαρμογής.
"""

from database.db import Database
from gui.app import FinanceApp


def main():
    """Κύρια συνάρτηση εκκίνησης της εφαρμογής."""
    db = Database("database.db")
    db.create_tables()
    db.create_default_user()

    app = FinanceApp(db)
    app.run()


if __name__ == "__main__":
    main()
