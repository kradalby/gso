initjs:
	npm install

dev: 
	pip install -r requirements/dev.txt --upgrade

prod:
	pip install -r requirements/prod.txt --upgrade

env:
	virtualenv -p `which python3` env

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info

test:
	python setup.py test

run:
	python gso.py


