from setuptools import setup, find_packages

setup(
	name='sessionlexer',
	packages=find_packages(),
	entry_points=
	"""
	[pygments.lexers]
	sessionlexer = sessionlexer.lexer:SessionLexer
	""",
)
