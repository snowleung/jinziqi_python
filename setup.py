#coding:utf-8
from setuptools import setup, find_packages

setup(name='jinziqi',
      version='0.1.0',
      description="jinziqi for python",
      long_description="""""",
      classifiers=['Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: Implementation :: PyPy',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      author='samleung',
      author_email='callsamleung@gmail.com',
      url='https://github.com/callsamleung/jinziqi_python',
      license='mit',
      packages=find_packages(exclude=('tests',)),
      zip_safe=False,
      test_suite='tests',
      setup_requires=[
          'versiontools>=1.8',
          ],
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      )
