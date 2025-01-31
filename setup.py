from setuptools import setup, find_packages

def get_requirements():

    req_list = []

    with open('requirements.txt') as f:
        lines = f.readlines()

        for req in lines:
            requirement=req.strip()

            if requirement and requirement != "-e .":
                req_list.append(requirement)
    return req_list


setup(
    name='dog-vs-cat-classifier',
    version='0.0.1',
    description='Dog Vs Cat Classifier',
    author='Kapish',
    author_email='kapishashtankar10@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements()

)