#/bin/bash

install:
	python3 -m venv ./venv
	. venv/bin/activate 
	pip install -r requirements.txt
	
run:
	python3 main.py
