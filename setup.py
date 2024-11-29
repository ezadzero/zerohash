from setuptools import setup, find_packages

setup(
    name="zerohash",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zerohash=zerohash:main',
        ],
    },
    install_requires=[],
)
