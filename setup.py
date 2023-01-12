(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) (Pdb) from setuptools import setup, find_namespace_packages
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) from setup_helper import find_resource_files
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) from tethys_apps.base.app_base import TethysAppBase
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) 
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) # -- Apps Definition -- #
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) (Pdb) app_package = 'test_app_store_aquaveo'
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) release_package = f'{TethysAppBase.package_namespace}-{app_package}'
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) 
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) # -- Python Dependencies -- #
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) dependencies = []
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) 
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) # -- Get Resource File -- #
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) 
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) 
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
(Pdb) (Pdb) (Pdb) (Pdb) (Pdb) (Pdb) (Pdb) (Pdb) resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' +                     app_package)
(Pdb) setup(
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