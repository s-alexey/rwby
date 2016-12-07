from setuptools import setup
from pip import req


def parse_requirements(filename):
    return [str(ir.req) for ir in req.parse_requirements(filename, session=False)]


__version__ = __import__('rwby').__version__

setup(
    name='Belarusian Railway API',
    version='0.1',
    author='Alexey Sukharevich',
    author_email='suharevichalexey@gmail.com',
    description='Python wrapper for rasp.rw.by',
    packages=['rwby'],
    install_requires=parse_requirements('requirements.txt'),
    url="https://github.com/s-alexey/rwby",
    include_package_data=True,
)
