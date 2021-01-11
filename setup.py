'''
Created on 12 April 2017
@author: Sambit Giri
Setup script
'''

#from setuptools import setup, find_packages
from distutils.core import setup

req_packages = ['numpy','scipy','scikit-learn','scikit-image']
#adding cupy if there's cuda
import os
# cuda_version = input("Enter cuda version (e.g. 110 for 11.0), empty for automatic determination\n")
# if cuda_version != '':
#       cupy_package = "cupy-cuda" + cuda_version
# else:
if os.system('nvidia-smi') == False:
      identifier = "CUDA Version: "
      stream = os.popen(f"nvidia-smi | grep {identifier}")
      output = stream.read()
      index = output.find(identifier) + len(identifier)
      cupy_package = "cupy-cuda" + output[index:index + 4].replace(".", "")
else:
      cupy_package = "cupy"
req_packages.append(cupy_package)

setup(name='tools21cm',
      version='2.0.1',
      author='Sambit Giri',
      author_email='sambit.giri@astro.su.se',
      package_dir = {'tools21cm' : 't2c'},
      packages=['tools21cm'],
      package_data={'share':['*'],},
      install_requires=req_packages,
      #include_package_data=True,
)
