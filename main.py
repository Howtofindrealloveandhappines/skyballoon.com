list= for grouping elements
#리스트의 응용

x = [1,2,3,4] 
y = ["hello", "there"]
if "hello" in y:-특정 상수가 포함되어 있는지 물어보고
#  print("ㅅㅅ") -맞으면 ㅅㅅ을 출력

x = [1,2,3,4]-#특정 자릿수에 있는 데이터를 출력#print(x[3])

x = [1,2,3,4]
num_elments = len(x)
#print(num_elments)


#important concept
#x = [1,2,3,4] #c에다가 리스트에 있는 elements를 하나씩 차례대로 넣어서 보여줘
#y = ["hello", "world"]
#for c in y:
 #print(c)

#x = [1,2,3,4]#element가 어디있는지 찾는 index function
#print(x.index(4)) 

#x = [1,2,3,4]#element가 x에 있는지만 궁금할 때 쓰는 함수.
#print(3 in x)
#////////////////////////////////////////////////////////

#튜플. 리스트에 있는 함수를 대부분 이용할 수 있따.
#But asignment is not allowed in Tuple= 리스트는 가변적(mutable), 튜플은 불변적(inmutable).

#x = {1,2,3}
#y = {'a','b','c'}
#print{'a' in y}

#딕셔너리= key랑 value로 이루어짐.
#x = {
# "name" : "워니", # name=key, 워니=value 
# "age"  : "20",  # age=key, 20=value
#}
#print(x["name"]) #name의 value를 print 해라
#print(x["age"]) #age의 value를 print 해라

#print("name" in x) #name이라는 key가 x 안에 들어있나요?

#x = {
#  0:"wonie",
#  1:"Hello",
#  "age": 20,
#}

#x["school"] = "이름" #school이라는 key와 이름이라는 value를 추가
#print(x)


fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d={}

for f in fruit: # f= 사과
 if f in d: # 사과가 d 안에 있나요? (d는 비어있으니 당연히 없음)
  d[f] = d[f]+1 #있으면 사과라는 key 의 vaule를 1 올려줘
 else: #없다면
  d[f]=1 #사과라는 key에 1이라는 vaule를 더해줘
print(d)
