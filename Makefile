run:
	docker compose unpause hack23-1-api

stop:
	docker compose pause hack23-1-api

update:
	cd api
	docker compose up -d --no-deps --build hack23-1-api
	docker compose exec -w /api hack23-1-api poetry run python -m alembic upgrade head

start:
	docker compose up --build -d
	docker compose exec -w /api hack23-1-api poetry run python -m alembic upgrade head