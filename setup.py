from setuptools import setup, find_packages

setup(
    name="salt-cumulus",
    version="0.0.1",
    description="Small salt module providing cumulus.managed, to apply basic config on cumulus switches",
    author="Maximilien Cuony",
    author_email="maximilien.cuony@arcanite.ch",
    url='https://github.com/ArcaniteSolutions/salt-cumulus',
    packages=find_packages(),
    install_requires='sh',
    license="MPL",
    entry_points='''
    [salt.loader]
    states_dirs = salt_cumulus.loader:states_dirs
    '''
)
