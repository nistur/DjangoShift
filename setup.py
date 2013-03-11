from setuptools import setup

setup(name='YourAppName', 
      version='1.0',
      description='Django 1.5 example app',
      author='Philipp Geyer', 
      author_email='admin@example.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=[ 'Django >= 1.5' ],
      dependency_links = ['https://www.djangoproject.com/download/1.5/tarball/#egg=Django-1.5',]
     )
