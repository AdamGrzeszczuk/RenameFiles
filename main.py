import os

# path = "/home/adam/Pictures/03. Zdjecia/Zdjecia Dysk Google/Hank Photoshoot"
path = input("Type the directory of the files you want to rename: ")
# path="/home/adam/Pictures/test"
string_to_add = input("Type the string that you want to add to the file name: ")

items_list = os.listdir(path)

for name in items_list:

	old_name_path = path + "/" + name
	new_name = name.split(".")[-2] + string_to_add + "." + name.rsplit(sep=".", maxsplit=-1)[-1]
	new_name_path = path + "/" + new_name
	os.rename(old_name_path, new_name_path)

print(f"Done! Name changed for {len(items_list)} files")
