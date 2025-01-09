from database.setup import create_tables
from database.connection import get_db_connection, execute_query
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Ensure the database tables are created before anything else
    create_tables()

    # Collect user input for the author, magazine, and article
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Validate user inputs
    if not author_name or not magazine_name or not article_title or not article_content:
        print("All fields must be filled!")
        return

    try:
        # Create an author
        author = Author(author_name)

        # Create a magazine (this will insert into the database)
        magazine = Magazine(None, magazine_name, magazine_category)  # id should be None here

        # Check if the magazine ID was set correctly after creation
        print(f"Magazine created with ID: {magazine.id}")

        # Create an article
        article = Article(article_title, article_content, author, magazine)

        print(f"Article '{article.title}' created successfully in '{magazine.name}' magazine by {author.name}!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
