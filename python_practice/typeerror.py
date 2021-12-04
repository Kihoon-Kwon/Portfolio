outFp=None
outList=[]
i=0
inList=['한국','미국','일본','중국','러시아','영국','싱가포르']
while i<10:
    Country=input('나라 이름을 입력하시오 : ')
    if Country in inList:
        print(inList.index(Country))
        i+=1
    else:
        outFp=open("C:/Temp/errorlog.txt","w")
        outList.append(Country)
        outList[-1]=Country
        print("%s is not in list 국가는 리스트에 존재하지 않습니다. 로그기록" %(Country))
        i+=1

for x in range(len(outList)):
    outFp.writelines(outList[x]+'\n')
    
outFp.close()

