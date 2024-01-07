from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    returns list of requirements
    '''
    requirements=[]
    e_dot = "-e ."
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]
    
        if e_dot in requirements:
            requirements.remove(e_dot)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author ='Charmaine',
    author_email='charmaine08fernz@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)