from setuptools import find_packages , setup

HYPEN_E_DOT ="-e ."
def get_requirements(requirements_file_path):
    requirements =[]
    with open(requirements_file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n" ,"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) 

    return requirements


setup(
    name= "mlproject",
    version= "0.0.1",
    author = "chetan",
    email= "cp@gmail.com",
    package = find_packages(),
    install_requires = get_requirements('requirements.txt')
)