git-gpt
=======

Generate commit messages using OpenAI GPT-3.

https://user-images.githubusercontent.com/622192/213011125-e455978e-43a9-46d1-aa61-3385e078c516.mp4

Configuration
-------------

Generate your OpenAI secret API key and set it to an environment variable named ``OPENAI_API_KEY``.

For more information, read `Where do I find my Secret API Key? <https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key>`_

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
