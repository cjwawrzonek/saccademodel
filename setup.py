from setuptools import setup

setup(name='saccademodel',
      version='0.1',
      description='NN package simulating delayed saccade task',
      long_description=readme(),
      url='http://github.com/cjwawrzonek/saccademodel',
      license='MIT',
      packages=['saccademodel'],
      include_package_data=True,
      zip_safe=False)