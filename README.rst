|License: MIT| |PyPI3| |PyPI2|

git-gpt
=======

Generate commit messages using OpenAI GPT-3.

Installation
------------

Install using pip:

::

	pip install git-gpt

Usage
-----

To use it as a command-line script:

::

	git-gpt commit

or:

::

	python -m git_gpt commit

For more information, refer to help:

::

	usage: git-gpt [-h] [--dry-run] command

	Run git commands with the assistance of OpenAI GPT-3.

	positional arguments:
	  command     a git command e.g. commit

	options:
	  -h, --help  show this help message and exit
	  --dry-run   prints the output of the command instead of running it
