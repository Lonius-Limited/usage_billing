from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in usage_billing/__init__.py
from usage_billing import __version__ as version

setup(
	name="usage_billing",
	version=version,
	description="Automated billing of client apps installed in client sites",
	author="Lonius Dev <railamolo@gmail.com>",
	author_email="raiilamolo@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
