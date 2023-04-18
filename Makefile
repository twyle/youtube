lint:
	@black ./youtube/
	@isort ./youtube/
	# @flake8 ./youtube/
	@pydocstyle ./youtube/
	@pylint --rcfile=.pylintrc ./youtube/