from setuptools import setup, find_packages

setup(
    name='user-service',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'user-service = user_service.main:main'
        ]
    },
)
