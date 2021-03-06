from setuptools import setup

setup(
   name='opennempy',
   version='0.6',
   description='Downloads data from http://opennem.org.au',
   author='See https://github.com/opennem/opennempy',
   author_email='See https://github.com/opennem/opennempy',
   packages=['opennempy'],
   install_requires=[
       'requests',
       'simplejson',
       'pandas'
   ]
)
