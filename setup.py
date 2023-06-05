from numpy import find_common_type
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]


        return requirements


setup (
    name='DiamondPricePrediction',
    version='0.0.1',
    author='amit',
    author_email='example@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )
