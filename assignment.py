class Lion:
    def __init__(self,name,phone,gender):
        self.name = name
        self.phone = phone
        self.gender = gender
    def met(self):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다."%(self.name, self.phone, self.gender))

student_list = []

while True:
    name = input("이름을 입력하세요: ")
    if name == '그만':
        for lion in student_list:
            lion.met()
        break
    phone = input("휴대전화 번호를 입력하세요: ")
    gender = input("성별을 입력하세요: ")
    
    if (gender == 'male') or (gender =='female'):
        gender = gender
    
    else: 
        gender = 'unknown'
    
    info = Lion(name,phone,gender)
    student_list.append(info)

    for lion in student_list:
        lion.met()
    print()



    