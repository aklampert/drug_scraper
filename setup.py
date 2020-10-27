from setuptools import setup


setup(name='drug_scraper',
      version='0.0.1',
      description='Tools to scrape drug names from drug resources.',
      url='',
      author='Andrew Klampert',
      author_email='aklampert4@gmail.com',
      license='Andrew Klampert',
      packages=['drug_scraper'],
      install_requires=[
            'pandas==1.1.2',
            'requests==2.24.0'
      ],
      zip_safe=False
      )
