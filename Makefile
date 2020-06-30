run:
	docker-compose up

stop:
	docker-compose down

test:
	pytest --cov=api api/tests/ -vv