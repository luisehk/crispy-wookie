install:
	pip install -r requirements.txt
	bower install

migrate:
	python manage.py migrate

run:
	foreman start

test:
	python manage.py test
