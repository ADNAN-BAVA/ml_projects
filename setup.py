from setuptools  import setup, find_packages

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]: # this function will read the requirements file and return the list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements] # removing the leading and trailing whitespaces using list comprehension 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='ml_project',
version='0.1',
author='Adnan',
author_email='adnan.bava123@gmail.com',
packages=find_packages(), # this will automatically find the packages in the current directory
install_requires= get_requirements('requirements.txt'), # this will read the requirements from the file
)