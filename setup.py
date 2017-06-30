from setuptools import setup

setup(name='hessianfreernn',
      version='0.1',
      description='NN package using hessian free optimization',
      long_description=readme(),
      url='http://github.com/cjwawrzonek/hessianfreernn',
      license='MIT',
      packages=['hessianfreernn'],
      include_package_data=True,
      zip_safe=False)