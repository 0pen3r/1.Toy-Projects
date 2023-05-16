import os
import time

#패스워드 추출 경로 by 바이너리 리딩
file_path='.\\pw\\'

#파일 리스트 출력
file_list = os.listdir(file_path)
print('[file list]', end='\n\n')
print(file_list)
print('\n\n[passwd get start]\n')


#파싱 전의 passwords 담을 리스트 선언
pw_list_aix =[]
pw_list_aix_smd =[]
pw_list_linux =[]

#파일 몇개 돌렸는지 카운딩 상수
c_aix = 0
c_linux = 0

##aix pass 형식
##{smd5}, {ssha1}, {ssha256}, {ssha512}

##linux /etc/shadow pass 
## $1:md5(취약), $5:sha256, $6:sha512, $y:yscript(john으로 가능)
## $2a:b-crypt, $md5:sun md5

##salt 예시
# {ssha512}06$ㄴㅁㄹㄴㅁㄹㅇㄴ$asfafdsfsdfdsfdsfsfdfdsfsd
# $6$소금값$o2o2o2o2o2o2o2oo2o2o2o2o2

def pass_parse_AIX(pw_list_aix, pw_list_linux):
	for file_name in file_list:
		with open(file_path+file_name, 'rb') as f:
			lines = f.readlines()
			#global pw_list_aix 빼고 pass_parse_AIX(pw_list_aix)로 인자 투입

			for line in lines:
				#ssha 형식은 AIX니까 AIX 분류
				#if b'ssha' in line:로해도됨 
				if 'ssha'.encode() in line:
					#파싱1 XX = {ssha512}
					aaa = str(line).split()
					#파싱2 ..\\n
					bbb = aaa[2].split('\\')
					#리스트에 append
					pw_list_aix.append(bbb[0])

				elif 'smd5'.encode() in line:
					#파싱1 XX = {ssha512}
					aaa = str(line).split()
					#파싱2 ..\\n
					bbb = aaa[2].split('\\')
					#리스트에 append
					pw_list_aix_smd.append(bbb[0])
				
				elif ':$6$'.encode() in line:
					#파싱1 : 으로 구분
					aaa = str(line).split(':')
					#리스트에 append
					pw_list_linux.append(aaa[1])

					
#출력부분
pass_parse_AIX(pw_list_aix,pw_list_linux)
print('\n=== AIX Password List ===\n')
print(pw_list_aix)
print(pw_list_aix_smd)
print('\n=== Linux Password List ===\n')
print(pw_list_linux)

##### 수정 진행 중
