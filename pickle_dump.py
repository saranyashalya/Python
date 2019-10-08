import pickle

num = int(input("Enter number of vars: "))
data =[]
for i in range(num):
    raw = input("Enter value "+str(i)+" :")
    data.append(raw)

file_name = open("data","wb")

pickle.dump(data, file_name)

file_name.close()