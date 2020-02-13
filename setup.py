from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="salt-cumulus",
    version="0.0.3",
    description="Small salt module providing cumulus.managed, to apply basic config on cumulus switches",
    author="Maximilien Cuony",
    author_email="maximilien.cuony@arcanite.ch",
    url='https://github.com/ArcaniteSolutions/salt-cumulus',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires='sh',
    license="MPL",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Other OS",
        "Programming Language :: Python",
        "Topic :: System :: Networking",
    ],
    entry_points='''
    [salt.loader]
    states_dirs = salt_cumulus.loader:states_dirs
    '''
)
