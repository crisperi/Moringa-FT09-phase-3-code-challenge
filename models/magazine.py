import sqlite3

from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id  
        self.name = name
        self.category = category
        self.create_magazine()

    def create_magazine(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
            conn.commit()
            self.id = cursor.lastrowid 
        except Exception as e:
            print(f"Error creating magazine: {e}")
        finally:
            conn.close()

    def __repr__(self):
        return f'<Magazine {self.name}>'

    def __str__(self):
        return f"Magazine(id={self.id}, name='{self.name}', category='{self.category}')"
