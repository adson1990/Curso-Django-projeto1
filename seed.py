import os
from string import digits
import django
from faker import Faker
from random import choice, randint

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

fake = Faker('pt_BR')

def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_recipe():
    return {
    'id' : fake.random_number(digits=2, fix_len=True),
    'title': fake.sentence(nb_words=6),
    'description': fake.text(max_nb_chars=150),
    'preparation_time': fake.random_int(min=1, max=120),
    'preparation_time_unit': 'Minutos',
    'servings': fake.random_number(digits=2, fix_len=True),
    'servings_unit': 'Porções',
    'preparation_steps': fake.text(3000),
    'created_at': fake.date_time(),
    'updated_at': fake.date_time_this_year(),
    'author': {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'username': fake.user_name(),
        'email': fake.email(),
        'password': fake.password(),
    },
    'category': {
        'name': fake.word()
    },
    'cover': {
    'url': f'https://picsum.photos/{rand_ratio()[0]}/{rand_ratio()[1]}?random={randint(1, 10000)}',
    'alt': 'Imagem de comida'
    }

    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())