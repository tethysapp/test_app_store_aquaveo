from setuptools import setup, find_namespace_packages
from setup_helper import find_resource_files
from tethys_apps.base.app_base import TethysAppBase

# -- Apps Definition -- #
app_package = 'test_app_store_aquaveo'
release_package = f'{TethysAppBase.package_namespace}-{app_package}'

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)


resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
setup(
    name=release_package,
    version='0.0.1',
    description='This is my testing app for submission and installation',
    long_description='',
    keywords='',
    author='Aquaveo',
    author_email='gromero@aquaveo.com',
    url='',
    license='MIT',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)