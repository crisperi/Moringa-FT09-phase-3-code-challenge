import sqlite3

class Author:
    def __init__(self,name, id=None,category=None):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._id = id
        if not id:
            self.create_author(name)
        
    
    def fetch_from_db(query, params=()):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        conn.close()
        return result

    def create_author(self, name):
        try:
            conn = sqlite3.connect('./database/magazine.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            conn.commit()
            self._id = cursor.lastrowid
        except Exception as e:
            print(f"Error creating author: {e}")
        finally:
            conn.close()


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM articles WHERE author_id = ?
        ''', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = sqlite3.connect('magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT magazines.* FROM magazines
        JOIN articles ON articles.magazine_id = magazines.id
        WHERE articles.author_id = ?
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines