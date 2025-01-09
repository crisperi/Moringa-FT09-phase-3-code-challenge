import sqlite3

class Article:
    def __init__(self, title, content, author, magazine):
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(content, str) or not content:
            raise ValueError("Content must be a non-empty string.")
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        
        self._title = title
        self._content = content
        self._author = author  
        self._magazine = magazine  
        self.create_article()

    def create_article(self):
        try:
            conn = sqlite3.connect('./database/magazine.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                           (self._title, self._content, self._author.id, self._magazine.id))
            conn.commit()
            self._id = cursor.lastrowid  # Store the ID of the newly inserted article
        except Exception as e:
            print(f"Error creating article: {e}")
        finally:
            conn.close()

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

