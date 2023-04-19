lint:
	@black ./youtube/
	@isort ./youtube/
	# @flake8 ./youtube/
	@pydocstyle ./youtube/
	@pylint --rcfile=.pylintrc ./youtube/

build: clean
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf build dist youtube.*

check-build:
	@twine check dist/*

test-upload:
	@twine upload --repository testpypi dist/*

upload:
	@twine upload dist/*

bump-tag:
	@cz bump --changelog