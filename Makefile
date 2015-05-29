ENV=./env/bin

initjs:
	npm install

dev: 
	$(ENV)/pip install -r requirements/dev.txt --upgrade

prod:
	$(ENV)/pip install -r requirements/prod.txt --upgrade

env:
	$(ENV)/virtualenv -p `which python` env

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info

test:
	$(ENV)/python setup.py test

run:
	$(ENV)/python gso.py

freeze:
	$(ENV)/pip freeze
