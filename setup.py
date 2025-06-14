
from setuptools import setup, find_packages

setup(
    name='viabilidade_modelo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'joblib'
    ],
    author='Thiago Freitas',
    description='Projeto para previsão de viabilidade de projetos usando regressão logística e ML.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seu-usuario/projeto-viabilidade-ml',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
