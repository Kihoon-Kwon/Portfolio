import matplotlib.pyplot as plt

D_Length = [77,89,85,83,73,77,73,80] 
D_Height = [25,28,29,30,21,22,17,35] 
S_Length = [75,77,86,86,79,83,83,88]
S_Height = [56,57,50,53,60,53,49,61]
M_Length = [34,38,38,41,30,37,41,35]
M_Height = [22,25,19,30,21,24,28,18]

plt.scatter(D_Length, D_Height, c='red', marker='o',label='Dachshund')
plt.scatter(S_Length, S_Height, c='blue', marker='^',label='Samoyed')
plt.scatter(M_Length, M_Height, c='green',marker='s',label='Maltese')
         
plt.title("Dog size") 
 
plt.xlabel("Length")
plt.ylabel("Height")
plt.title("Dog size")  
plt.legend()
plt.show()
