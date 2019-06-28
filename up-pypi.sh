#!/bin/bash
rm -r dist || :
# python setup.py sdist && twine upload dist/*
python setup.py bdist_wheel && twine upload dist/*
