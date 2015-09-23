try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = None
with open("guildwars2api/__init__.py", "r") as file:
    for line in file.read().splitlines():
        if line.startswith("__version__"):
            version = line.split('=')[1].replace('"', '').strip()

requirements = []
with open("requirements.txt", "r") as file:
    for line in file.read().splitlines():
        if not line.startswith('#'):
            requirements.append(line)

setup(
    name='guildwars2api',
    version=version,
    packages=['guildwars2api'],
    url='https://github.com/marcardioid/GuildWars2API-Python',
    license='MIT',
    author='Marc Sleegers',
    author_email='mail@marcsleegers.com',
    description='A Python wrapper for the second version of the Guild Wars 2 API.',
    install_requires=requirements
)