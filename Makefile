ENV=./env/bin
PYTHON=$(ENV)/python
PIP=$(ENV)/pip
SETUP=$(PYTHON) setup.py

dev:
	$(PIP) install -r requirements/development.txt --upgrade

prod:
	$(PIP) install -r requirements/production.txt --upgrade

env:
	virtualenv -p `which python3` env

flake8:
	flake8

lint: flake8

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info

test:
	$(SETUP) test

run:
	$(PYTHON) app.py

freeze:
	$(PIP) freeze
