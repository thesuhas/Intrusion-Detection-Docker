# tried only for images that exist
# does not try and catch any errors of failures
import os
import re
# Gets list of images
ip = open("image_names.txt","r")
image_names = ip.readlines()
ip.close()
print(image_names)
for i in image_names:
    # Remove newline at the end
    if '\n' in i:
        i = i[:-1]
    # Substitute / with -, if / not present, string is returned unmodified
    i2 = re.sub('/','-',i)
    f_name = 'CVE-'+i2+'.json'
    print(f_name)
    # Pull docker image
    cmd1 = "docker pull "+i
    # Run trivy on the docker image of the container
    cmd2 = "trivy image -f json -o "+f_name+" "+i
    print("Image Name : ",i)
    print("Pulling image")
    os.system(cmd1)
    print("Pull Complete")
    print("Scanning For Vulnerabilities")
    os.system(cmd2)
    print("Scan Complete [results in",f_name,"]")
    print("--------------------------------------------------------------------------------")
print("DONE")
