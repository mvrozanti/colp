#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='colp',  
     version='0.0.2',
     author="Marcelo V. Rozanti",
     author_email="mvrozanti@hotmail.com",
     description="Color Processor",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mvrozanti/colp",
     packages=setuptools.find_packages(),
     scripts=['colp/colp'],
     classifiers=[
         "Development Status :: 4 - Beta",
         "Topic :: Artistic Software",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3.4",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3 :: Only",
         ],
 )
