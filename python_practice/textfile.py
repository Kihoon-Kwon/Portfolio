inFp=None
inList,inStr=[],""
i=1

inFp=open("C:/Temp/sample.txt","r",encoding="UTF8")
inList=inFp.readlines()
def inSum(x):
    return int(x)
x=list(map(inSum,inList))
x_sum=sum(x)
print("전체 합은 %d입니다." %(x_sum))
print("전체 평균은 %d입니다." %(x_sum/len(x)))
inFp.close()
