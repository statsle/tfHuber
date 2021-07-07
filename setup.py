from setuptools import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

tfHuber_module = Extension('tfHuber',
                           include_dirs = ['eigen'],
                           sources = ['module.cpp'])

setup(
    name='tfHuber',
    version='0.1.2',
    description='Python Package for tuning-free Huber Regression',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author= ['Yifan Dai', 'Qiang Sun'],
    author_email = ['yifandai@yeah.net', 'qsun.ustc@gmail.com'],
    license='GPL(>=3)',
    ext_modules=[tfHuber_module]
)