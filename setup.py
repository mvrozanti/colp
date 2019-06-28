import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='colp',  

     version='0.91',

     author="Marcelo V. Rozanti",

     author_email="mvrozanti@hotmail.com",

     description="Color Processor",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/mvrozanti/colp",

     packages=setuptools.find_packages(exclude='test*'),

     scripts=['src/colp.py'],

     classifiers=[
         "Development Status :: 3 - Alpha",
         "Topic :: Internet",
         "License :: OSI Approved :: Apache Software License",
         ],
 )
