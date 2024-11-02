# Projet DJANGO : Gestionnaire de collections


- Zineb, SUKIENNIK, zineb.sukiennik@etu.univ-orleans.fr
- Nisrine, ABHARI, nisrine.abhari@etu.univ-orleans.fr
- Thomas, FOUCHER, thomas.foucher1@etu.univ-orleans.fr
- Sullivan, DEMARET, sullivan.demaret@etu.univ-orleans.fr


## Commande Django utilisées

### Question 1

```bash
django-admin startproject cc
cd cc/
python manage.py startapp collec_management
python manage.py runserver 0.0.0.0:8000
```
Accès au serveur sur **le port 8088**

### Question 3

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```
### Question 4

```bash
python manage.py shell
from collec_management.models import Collec
from datetime import date

collectionsexemples = [{"title": "Collection de parfums", "description": "Parfums de niche", "date": date(2024, 1, 1)},{"title": "Collection de livres", "description": "Littérature française", "date": date(2024, 2, 2)}, {"title": "Collection de voitures", "description": "Voitures de collection vintage des années 90", "date": date(2024, 3, 3)},{"title": "Collection de billets", "description": "Billets de pays étrangers", "date": date(2024, 4, 4)},
{"title": "Collection de cartes Pokémon", "description": "Cartes Pokémon rares", "date": date(2024, 5, 5)},{"title": "Collection de timbres", "description": "Timbres allemands datant de la 2nde Guerre Mondiale", "date": date(2024, 6, 6)},{"title": "Collection de cristaux", "description": "Pierres rares en provenance de Sardaigne", "date": date(2024, 7, 7)},{"title": "Collection de montres", "description": "Montres vintage de différentes marques", "date": date(2024, 8, 8)},{"title": "Collection de vins", "description": "Vins provenant de différents terroirs", "date": date(2024, 9, 9)},{"title": "Collection de bougies", "description": "Bougies de formes diverses et variées", "date": date(2024, 10, 10)},{"title": "Collection de sneakers", "description": "Sneakers disponibles en seulement quelques exemplaires dans le monde", "date": date(2024, 11, 11)},{"title": "Collection de poupées russes", "description": "Poupées russes en porcelaine", "date": date(2024, 12, 12)}]

for collec in collectionsexemples :
Collec.objects.create(**collec)

Collec.objects.all()
python manage.py loaddata collec_management/fixtures/examples.json
python manage.py shell
from collec_management.models import Collec
collections = Collec.objects.all()
print(collections)
```
