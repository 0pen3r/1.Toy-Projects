import os

dir_path='.\\db_list'
#word=''
#new_word=''

print('\n# Path is = ' + dir_path + '\n')
print('# Database List\n')

f_list = os.listdir(dir_path)

for file_name in f_list:
	print(file_name)
#	db_path =+ dir_path + '\\' + file_name
#	print(db_path)

def replace_blank(word, new_word):
	for file_name in f_list:
		db_path = dir_path + '\\' + file_name
		f = open(db_path, 'r')
		lines = f.readlines()
		f.close()

		fw = open(db_path, 'w')
		for lien in lines:
			fw.write(lien.replace(word, new_word))
		fw.close()

replace_blank('mm', 'k')
print('\nE N D')


// 
