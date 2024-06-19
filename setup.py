from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    this function is used to get the packages from requiremnts.txt
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req_name.replace("\n","") for req_name in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='endToendmlproject',
    version='0.0.1',
    author='Govardhan',
    author_email='govardhanar06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)