# tried only for images that exist
# does not try and catch any errors of failures
import os
import re
ip = open("image_names.txt","r")
image_names = ip.readlines()
ip.close()
print(image_names)
for i in image_names:
    if '\n' in i:
        i = i[:-1]
    if ':' in i:
        i = i.split(':')[0]
    i2 = re.sub('/','-',i)
    f_name1 = 'trivy_results/json/CVE-'+i2+'.json'
    f_name2 = 'trivy_results/table/CVE-'+i2+'.txt'
    print(f_name1, f_name2)
    cmd1 = "docker pull "+i
    cmd2 = "trivy image -f json -o "+f_name1+" "+i
    cmd3 = "trivy image "+i+" > "+f_name2
    print("Image Name : ",i)
    print("Pulling image")
    os.system(cmd1)
    print("Pull Complete")
    print("Scanning For Vulnerabilities")
    os.system(cmd2)
    os.system(cmd3)
    print("Scan Complete")
    print("--------------------------------------------------------------------------------")
print("DONE")
