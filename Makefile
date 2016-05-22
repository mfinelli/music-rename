check:
	yapf -d setup.py music_rename/*.py tests/*.py

style:
	yapf -i setup.py music_rename/*.py tests/*.py

test:
	py.test
