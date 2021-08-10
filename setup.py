import os
from setuptools import setup, find_packages
from dual_sessions import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dual-sessions',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Manage your Django sessions differently for authenticated and unauthenticated users - with minimal configuration '
                'required.',
    long_description=README,
    url='https://github.com/Aristotle-Metadata-Enterprises/',
    author='Aristotle Cloud Services Australia',
    author_email='hello@aristotlemetadata.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django sessions management',
    install_requires=[
        'django',  # I mean obviously you'll have django installed if you want to use this.
    ],
)
