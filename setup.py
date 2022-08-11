from setuptools import setup
#import python-package-template

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='python-package-template',
      #version=python-package-template.__version__,
      version="0.0.1",
      description='Python package template',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/evenmn/python-package-template',
      author='Even Marius Nordhagen',
      author_email='evenmn@mn.uio.no',
      license='GPL-v3',
      packages=['python_package_template'],
      include_package_data=True,
      zip_safe=False)
