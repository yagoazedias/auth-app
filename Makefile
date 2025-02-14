test:
	coverage run -m unittest tests/all.py && make coverage

single-test:
	python3 -m unittest

coverage:
	coverage report --fail-under=95 --show-missing --omit=".venv/*","*/test*","lib/business/authorizer.py"

install:
	pip3 install -r requirements.txt

install-virtual-env:
	source venv/bin/activate && pip3 install -r requirements.txt

run:
	python3 authorize.py < samplefile
