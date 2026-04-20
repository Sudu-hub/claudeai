import sqlite3
from werkzeug.security import generate_password_hash


def get_db():
    """Open a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect("spendly.db")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create database tables if they don't exist."""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """Insert demo data if not already present."""
    conn = get_db()
    cursor = conn.cursor()

    # Check if already seeded
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # Insert demo user
    cursor.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123"))
    )

    # Get the demo user's ID
    cursor.execute("SELECT id FROM users WHERE email = ?", ("demo@spendly.com",))
    user_id = cursor.fetchone()["id"]

    # Insert 8 sample expenses
    expenses = [
        (45.50, "Food", "2026-04-01", "Grocery shopping"),
        (15.00, "Transport", "2026-04-02", "Bus pass"),
        (120.00, "Bills", "2026-04-03", "Electricity bill"),
        (35.00, "Health", "2026-04-05", "Pharmacy"),
        (25.00, "Entertainment", "2026-04-07", "Movie tickets"),
        (89.99, "Shopping", "2026-04-10", "New shirt"),
        (12.50, "Food", "2026-04-12", "Lunch"),
        (50.00, "Other", "2026-04-15", "Miscellaneous"),
    ]

    cursor.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        [(user_id, *exp) for exp in expenses]
    )

    conn.commit()
    conn.close()
