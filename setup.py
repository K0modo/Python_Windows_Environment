from setuptools import setup, find_packages

setup(
name='python_windows_environment',
version='0.1',
packages=find_packages(),
install_requires=['streamlit'],
entry_points={
    'console_scripts': [
        'python-windows-environment=python_windows_environment.app:main'
    ]
},
author='James C Mattingly',
description='A Streamlit app to demystify environment variables in a Windows environment',
# url='https://github.com/yourusername/computer_model_streamlit',
)