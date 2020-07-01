run:
	docker-compose up -d

stop:
	docker-compose down

shell:
	docker exec -it rota_viagem_dev bash

test:
	pytest --cov=api api/tests/ -vv