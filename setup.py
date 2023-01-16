from setuptools import setup, find_namespace_packages
from setup_helper import find_all_resource_files


# -- Apps Definition -- #




namespace = 'tethysapp'
app_package = 'test_app_store_aquaveo'
release_package = f'{namespace}-{app_package}'


# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, namespace)


#hola comment hey

setup(
    name=release_package,
    version='0.0.3',
    description='This is my testing app for submission and installation',
    long_description='',
    keywords='',
    author='Aquaveo',
    author_email='gromero@aquaveo.com',
    url='https://github.com/Aquaveo/test_app_store_aquaveo',
    license='MIT',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)