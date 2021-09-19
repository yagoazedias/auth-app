test:
	coverage run -m unittest tests/all.py && make coverage

coverage:
	coverage report --fail-under=95 --show-missing --omit=".venv/*","*/test*"

install:
	pip3 install -r requirements.txt

install-virtual-env:
	source venv/bin/activate && pip3 install -r requirements.txt

run:
	python3 authorize.py 
