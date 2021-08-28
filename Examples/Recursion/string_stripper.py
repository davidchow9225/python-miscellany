"""Strips hyphens, spaces, and the word "and" from a number's word form."""
def string_strip(string: str):
	return string.replace('-', '').replace(' ', '').replace('and', '')

if __name__ == '__main__':
	pass
else:
	print(f'{__name__} was successfully imported.')
	if __doc__: print(__doc__, '\n')
