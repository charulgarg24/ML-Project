from setuptools import find_packages,setup
from typing import List

HYPRN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this finction will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line and not line.startswith(HYPRN_E_DOT):  # Exclude lines starting with '-e .'
                requirements.append(line)
    return requirements
    #     requirements=file_obj.readlines()
    #     requirements=[req.replace("\n","") for req in requirements]

    #     if HYPRN_E_DOT in requirements:
    #         requirements.remove(HYPRN_E_DOT)


    # return requirements


setup(
name='ML-Project',
version='0.0.1',
author='Charul',
author_email='charulgarg24@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   
)