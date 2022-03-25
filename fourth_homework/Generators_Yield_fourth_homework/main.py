nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list):
	for main_item in nested_list:
		for inner_item in main_item:
			yield inner_item


generator = [item for item in flat_generator(nested_list)]
print(generator)







