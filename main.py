def main():
	filepath = "./books/frankenstein.txt"
	file_contents = get_file_contents(filepath)
	count = get_words_count(file_contents)
	char_dict = get_char_count(file_contents)
	sorted_char = sort(char_dict)
	print(f"--- Begin report of {filepath} ---")
	print(f"{count} words found in the document \n")
	for item in sorted_char:
		# print(item)
		k = item["character"]
		c = item["count"]
		print(f"The '{k}' character was found {c} times")
	print("\n--- End report ---")

def get_file_contents(path):
	with open(path) as f:
		file_contents = f.read()
		return file_contents

def get_words_count(contents):
	count = len(contents.split())
	# print(count)
	return count

def get_char_count(contents):
	characters_dict = {}
	for char in contents.lower():
		if char.isalpha():
			if char in characters_dict:
				characters_dict[char] += 1
			else:
				characters_dict[char] = 1
	# print(characters_dict)
	return characters_dict

def sort(char_dict):
	char_list = []
	for k in char_dict:
		char_list.append({"character":k , "count":char_dict[k]})
	char_list = sorted(char_list,key=lambda d: d["character"])
	# print(char_list)
	return char_list


main()