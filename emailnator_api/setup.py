#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'requests' ]

test_requirements = [ ]

setup(
    author="John Kierns",
    author_email='beandog720@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This API generates free gmail emails using https://emailnator.com",
    # entry_points={
    #     'console_scripts': [
    #         'emailnator_api=emailnator_api.cli:main',
    #     ],
    # },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='emailnator_api',
    name='emailnator_api',
    packages=find_packages(include=['emailnator_api', 'emailnator_api.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/skeltoncodez/emailnator_api',
    version='0.1.0',
    zip_safe=False,
)
