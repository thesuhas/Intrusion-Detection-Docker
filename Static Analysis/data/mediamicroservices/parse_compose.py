filename = input("Enter file name to be parsed for image names : ")
ip = open(filename,'r')
lines = ip.readlines()
ip.close()
op = open("image_names.txt","w")
res = {}
count = 0
for line in lines:
    if '#' not in line:
        if "image:" in line:
            count+=1
            img_name = line.split("image:")[1].strip()
            if img_name in res:
                res[img_name]+=1
            else:
                res[img_name]=1
for img_name in res:
    print(img_name,file=op)
op.close()
print(res)
print("Total Containers : ",count)
print("Image Names found in 'image_names.txt' file")
