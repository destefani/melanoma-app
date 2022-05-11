#!/bin/bash

install:
	@echo "Installing..."
	python3 -m venv ./venv
	. venv/bin/activate
	pip install -r requirements.txt

run:
	@echo "Running..."
	. venv/bin/activate
	streamlit run app.py


