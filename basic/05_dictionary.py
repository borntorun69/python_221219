# dictionary key는 중복 불허, value는 중복 허용

dict_a = {
  "name": "홍길동",
  "grade": 1,
  "stdNo": 1,
  "mobile": "010",
}
dict_a['score'] = [98, 100, 89]
print(dict_a)
print(dict_a["name"])

d1 = {
  0: "꽃", 1: "달", 2: "해"
}
d1[0] = 8  # key가 중복되면 overwrite
d1[10] = 7  # key가 다르면 add
print(d1)

for key in d1:
  print(key, d1[key])
print(f'{"dictionary 역정렬 ":=^20}')
li = reversed(d1.keys())
for key in li:
  print(key, d1[key])

print(f'{"dictionary 정렬 ":=^20}')
li = sorted(d1.keys())
for key in li:
  print(key, d1[key])

print(f'{"dictionary 함수 ":=^20}')
print(d1.keys())  # key만
print(d1.values())  # value만
print(d1.items())  # key, value
print(d1.get(2))  # key가 문자인지 숫자인지 파악
# print(d1[0], d1.get(0))
print(d1.get(100, 100))  # key100이 없으니 defoult 지정가능

print(1 in d1)
print(1 not in d1)
