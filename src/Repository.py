import os
import sqlite3 
from dotenv import load_dotenv

load_dotenv()

SQLITE = os.getenv('SQLITE')

conn = sqlite3.connect(SQLITE)

class repository:
    def __init__(self):
        self.conn = sqlite3.connect(SQLITE, check_same_thread=False)  # Allow connections across threads
        self.cursor = self.conn.cursor()
    
    def fetch_all(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()
    
    def fetch_one(self, id):
        self.cursor.execute('SELECT * FROM products WHERE id = ?', (id,))
        return self.cursor.fetchone()
    
    def create(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def update(self, id, name, price):
        self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, id))
        self.conn.commit()
        
    def delete(self, id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        self.conn.commit()