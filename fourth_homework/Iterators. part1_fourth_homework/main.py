nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

class FlatIterator:
	def __init__(self, list_of_lists):
		self.list_of_lists = list_of_lists
		self.main_cursor = -1
		self.end = len(self.list_of_lists)

	def __iter__(self):
		self.main_cursor += 1
		self.inner_cursor = 0
		return self

	def __next__(self):
		if self.inner_cursor == len(self.list_of_lists[self.main_cursor]):
			iter(self)
		if self.main_cursor == self.end:
			raise StopIteration
		self.inner_cursor += 1
		return self.list_of_lists[self.main_cursor][self.inner_cursor - 1]


flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

