from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version_string = os.environ.get("VERSION_PLACEHOLDER", "1.9.0")
print(version_string)
version = version_string

setup(
        name = 'feeed',
        version = str(version),
        description = 'Feature Extraction from Event Data',
        author = 'Andrea Maldonado',
        author_email = 'andreamalher.works@gmail.com',
        license = 'MIT',
        url='https://github.com/lmu-dbs/feeed.git',
        long_description=long_description,
        long_description_content_type="text/markdown",

        python_requires='>=3.14,

        install_requires=[
            'tqdm==4.65.0',
            'pm4py>=2.7.2',
            'scipy>=1.10.1',
            'Levenshtein==0.27.3',
            ],
        packages = ['feeed', 'feeed.utils'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'Topic :: Software Development',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: 3.13',
            'Programming Language :: Python :: 3.14',
    ],
)
