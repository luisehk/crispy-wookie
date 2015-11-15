migrate:
	python manage.py migrate

run:
	foreman start

install:
	pip install -r requirements.txt

test:
	python manage.py test