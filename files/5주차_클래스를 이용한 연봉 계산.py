class Employ:

    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("%s님의 연차는 %d입니다." %(name,year))
    
    def salary(self):
        if(self.year<5 and self.year>0):
            self.salary=3000+(self.year*100)
            print("%s님의 연봉은 %d만원입니다." %(a.name,a.salary))
        elif(self.year<10):
            self.salary=3500+(self.year*110)
            print("%s님의 연봉은 %d만원입니다." %(a.name,a.salary))
        elif(self.year>=10):
            self.salary=4000+(self.year*130)
            print("%s님의 연봉은 %d만원입니다." %(a.name,a.salary))
        else:
            print("잘못된 입력입니다.")

    def getDegree(self):
        self.salary_d=self.salary+1200
        print("%s님의 연봉은 학위 소지로 인하여 %d만원입니다." %(a.name,a.salary_d))

    def __getattr__(self,name):
        print("잘못된 값입니다.")
        
a=Employ("홍길동",7)

a.salary()
a.getDegree()
a.money

