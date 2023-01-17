import os
import re
from setuptools import setup

github_url = 'https://github.com/programmarchy/git-gpt'
main_module = 'git_gpt'

with open('README.rst', 'rb') as stream:
  long_description = stream.read().decode('utf-8').replace('\r', '')

version_re = re.compile("__version__ = '(?P<version>[0-9\\.]*)'")
with open('git_gpt/__init__.py', 'r') as stream:
  contents = stream.read()
match = version_re.search(contents)
version = match.groupdict()['version']

dependencies = []
filename = os.path.join('requirements.txt')
with open(filename, 'r') as stream:
  for line in stream:
    package = line.strip().split('#')[0]
    if package:
      dependencies.append(package)

setup(
  name=main_module,
  version=version,
  description="Generate commit messages using OpenAI GPT-3.",
  long_description=long_description,
  long_description_content_type='text/x-rst',
  url=github_url,
  download_url='%s/releases' % github_url,
  author='Donald Ness',
  author_email='donald.ness@gmail.com',
  license='MIT',
  packages=[main_module],
  py_modules=[main_module],
  entry_points={
    'console_scripts': ['git-gpt = git_gpt.__main__:main',]
  },
  include_package_data=True,
  install_requires=dependencies,
  python_requires='>=3.6',
)
