run:
	poetry run python src/phoebot/main.py

install:
	poetry install

lock:
	poetry lock --no-update

lint:
	poetry run black src
