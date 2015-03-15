# create virtual environment
venv:
	virtualenv venv

# install all needed for development
develop: venv
	venv/bin/pip install -e . -r requirements-testing.txt tox

# clean the development envrironment
clean:
	-rm -rf venv
