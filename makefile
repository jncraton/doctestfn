all:

install:
	python3 setup.py install

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf tmp
	rm -rf doctestfn.egg-info
	rm -rf doctestfn/__pycache__
	rm -rf dist
	rm -rf build
