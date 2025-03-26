superuser:
	python app/manage.py createsuperuser

test:
	docker compose exec web pytest

up:
	docker compose up

reset:
	docker compose down -v
	docker compose up --build

migrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate
