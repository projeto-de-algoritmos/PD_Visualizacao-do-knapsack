.ONESHELL:

.DEFAULT_GOAL := run

PYTHON = ./venv/bin/python3
PYXEL = ./venv/bin/pyxel

PIP = ./venv/bin/pip

venv/bin/activate: requirements.txt	
	-python3 -m venv venv
	-chmod -x ./venv/bin/activate
	-. ./venv/bin/activate
	-$(PIP) install -r requirements.txt

venv: venv/bin/activate
	-. ./venv/bin/activate

clear: 
	-rm -r venv
	-rm -r src/__pycache__
	-rm -r .vscode

runfile: venv
	$(PYTHON) src/$(f).py

run: venv 
	-$(PYTHON) src/main.py



.PHONY: run clear runfile