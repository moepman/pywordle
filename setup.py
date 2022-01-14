from setuptools import setup, find_packages

setup(
    name="pywordle",
    version="0.1.0",
    author="Markus Hauschild",
    author_email="markus@moepman.eu",
    description="Python-based wordle helper",
    license="ISC",
    url="",
    packages=find_packages(),
    install_requires=[
        "pyenchant"
    ],
    entry_points={
        'console_scripts': [
            'worlde=wordle.wordle:main',
        ],
    }
)
