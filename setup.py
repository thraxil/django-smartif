from setuptools import setup, find_packages

setup(name='django-smartif',
      version="0.1",
      author="anders pearson",
      description="Django app wrapper for smartif templatetag",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      install_requires = [],
      zip_safe=False,
      package_data = {'' : ['*.*']},
      include_package_data=False,
      entry_points="""
      """
      )
	
