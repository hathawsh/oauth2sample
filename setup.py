
from setuptools import setup, find_packages
import os
import sys

requires = [
    'pyramid',
    'pyramid_oauth2_client',
    'requests',
    'setuptools',
]

if sys.version_info[:2] < (2, 7):
    requires.append('unittest2')

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='oauth2sample',
    version='0.1',
    description='Sample OAuth2 Client',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author='',
    author_email='',
    url='',
    keywords='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    test_suite='oauth2sample',
    install_requires=requires,
    entry_points="""
    [paste.app_factory]
    main = oauth2sample:main
    """,
)
