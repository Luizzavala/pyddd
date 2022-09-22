include .env

up:
	docker-compose up -d 
down:
	docker-compose down
build:
	docker-compose build
logs:
	docker-compose logs
logsf:
	docker-compose logs -f
