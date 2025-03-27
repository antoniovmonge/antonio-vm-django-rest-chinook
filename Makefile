superuser:
	python app/manage.py createsuperuser

test:
	docker compose exec web pytest

up:
	docker compose up

up-d:
	docker compose up -d

stop:
	docker compose stop

down:
	docker compose down -v

reset:
	docker compose down -v
	docker compose up --build

migrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate
