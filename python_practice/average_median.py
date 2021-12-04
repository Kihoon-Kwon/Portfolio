import numpy as np

players=np.zeros((100,3))
height=175
weight=70
age=22
sigma=10

players[:,0]=height+sigma*np.random.randn(100)
players[:,1]=weight+sigma*np.random.randn(100)
players[:,2]=age+np.floor(sigma*np.random.randn(100))

print('신장 평균값:',np.mean(players[:,0]))
print('신장 중앙값:',np.median(players[:,0]))
print('체중 평균값:',np.mean(players[:,1]))
print('체중 중앙값:',np.median(players[:,1]))
print('나이 평균값:',np.mean(players[:,2]))
print('나이 중앙값:',np.median(players[:,2]))
