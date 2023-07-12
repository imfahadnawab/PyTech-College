from setuptools import setup, find_packages
setup(
    name='PyTech',
    version='1.0.0',
    author='Fahad Nawab',
    description='',
    install_requires=[
        'Django>=4.4.3',
        'other-package>=1.0',
    ],
    package_data={
        'PyApp': ['templates/*.html', 'static/*'],
        'users': ['templates/*.html', 'static/*'],
    },
    packages=find_packages(),
)
