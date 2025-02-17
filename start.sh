#!bin/bash

# run docker compose
docker compose up --build -d

# run the migrations
docker-compose exec web python manage.py migrate

cd src/scraper/

# run scraper
python scraper.py

