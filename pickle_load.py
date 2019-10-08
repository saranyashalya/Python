import pickle

file_name = open("data","rb")

loaded_data = pickle.load(file_name)

cnt =0
for i in loaded_data:
    print("Data "+str(cnt)+" : "+i)
    cnt +=1
