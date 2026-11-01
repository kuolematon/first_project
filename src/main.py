from dotenv import load_dotenv 
import os 

print('Hello from repository!')


def print_author():
# Допишите здесь ваш код
    load_dotenv(dotenv_path='.env')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
