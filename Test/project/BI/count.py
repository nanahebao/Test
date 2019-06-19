datas=[]
with open('log123.txt','r') as f:
    for line in f:
        #print(len(line))
        data=eval(line[26:])[4]
        num_int=float(data.strip('%'))
        if num_int<90:
            datas.append(line[26:])
print(datas)

with open('wrong.text','w')as f:
    for i in datas:
        f.write(i)