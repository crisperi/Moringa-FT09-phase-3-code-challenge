import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        """
        Initialize a magazine.

        :param id: The ID of the magazine.
        :param name: The name of the magazine.
        :param category: The category of the magazine (e.g., Technology, Fashion).
        """
        self.id = id
        self.name = name
        self.category = category
    
    
    def fetch_from_db(query, params=()):
        conn = sqlite3.connect('../database/magazine.db')
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    def __str__(self):
            return f"Magazine(id={self.id}, name='{self.name}', category='{self.category}')"