from setuptools import setup, find_packages

setup(
	name="DDuplicate",
	version="1.1",
	description='The helper to find and manager duplicates of files',
	url='https://github.com/messiasthi/dduplicated',
	author='Thiago Messias',
	author_email='messiasthi@gmail.com',
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			"dduplicated=dduplicated.cli:main"
		]
	}
)
