
print('패딩제거용 제작이지만 텍스트 스위칭 가능')


file_path='.\\testdb.txt'
word=''
new_word=' '


def replace_blank(file_path, word, new_word):
		f = open(file_path, 'r')
		lines = f.readlines()
		f.close()

		fw = open(file_path, 'w')
		for lien in lines:
			fw.write(lien.replace(word, new_word))
		fw.close()

replace_blank(file_path, word, new_word)

#바꿀횟수
#replace_blank(file_path, word, new_word, 1) 전체 1
#replace_blank(file_path, word, new_word, -1) 뒤에서 1
