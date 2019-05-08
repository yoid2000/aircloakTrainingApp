SHELL := /bin/bash

env:
	python3 -m venv env

deps: env
	( \
		source env/bin/activate; \
		pip3 install -r devel-requirements.txt; \
		pip3 freeze -r devel-requirements.txt > requirements.txt; \
	)

make start-local:
	( \
		source env/bin/activate; \
		source .env-dev; \
		python3 demo.py; \
	)

make start:
	( \
		source env/bin/activate; \
		python3 demo.py; \
	)
