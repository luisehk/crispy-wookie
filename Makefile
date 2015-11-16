# If the first argument is "manage"...
ifeq (manage,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "manage"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif

install:
	pip install -r requirements.txt
	bower install

manage:
	python manage.py $(RUN_ARGS)

migrate:
	python manage.py migrate

report:
	coverage report

run:
	foreman start

test:
	coverage run --source=. manage.py test -v 2
