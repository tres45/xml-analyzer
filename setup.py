from setuptools import setup, find_packages


setup(
    name="xml_analyzer",
    version="0.1",
    author="Serhii Osadchyi",
    author_email="osadchyi91@gmail.com",
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'xml_analyzer=xml_analyzer.cli:main',
        ],
    },
)