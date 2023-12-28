from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in exam_centers/__init__.py
from exam_centers import __version__ as version

setup(
	name="exam_centers",
	version=version,
	description="for managing exam centers and final exams scheduling",
	author="Wael Al-edrisi",
	author_email="waelaledrisi813636@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
