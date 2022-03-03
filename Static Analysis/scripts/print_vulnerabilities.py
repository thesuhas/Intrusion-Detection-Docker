import os
import json
import re
files_list = []
# Directory storing all the required libraries for various components
path_to_files = "./libraries_needed/"
# Trivy results
path_to_vulnerabilities = "./trivy_results/json/"
prefix = "CVE-"
# Expands the file tree from the given path
for i,j,k in os.walk(path_to_files):
    # Goes through all the files in the given directory
    files_list.extend(k)
final_res = {}
upgrades = {}
# A file mapping various containers to their images
f = open("cont_image_map.txt","r")
x = f.readlines()
f.close()
ci_map = {}
# Starts iterating from the first container image mapping
for i in x[2:]:
    # Gets the container name
    cont = i.split()[0]
    # Gets the image name (under repository section)
    img = re.sub('/','-',i.split()[1])
    # Adds to dictionary
    ci_map[cont]=img
for name in files_list:
    # print("\nImage Name : ",name[:-4])
    # print("***********************")
    # Reads each individual file
    f = open(path_to_files+name,'r')
    x = f.readlines()
    f.close()
    i = 0
    for j in x:
        if "----" in j:
            break
        i+=1
    # Extracts list of packages
    x = x[i+1:]
    # Removes unnecesary characters
    x = [i[:-1] for i in x]
    # Loads all the vulnerabilities associated with that image
    f = open(path_to_vulnerabilities+prefix+ci_map[name[:-4]]+".json",'r')
    vulns = json.load(f)
    f.close()
    cve_set = set()
    package_set = set()
    suggested_upgrades = {}
    severity = {"CRITICAL":0,"HIGH":0,"MEDIUM":0,"LOW":0}
    vulns = vulns[0]["Vulnerabilities"]
    f = open("./vulnerability_list/"+name,'w')
    for i in vulns:
        if i["PkgName"] in x:
            package_set.add(i["PkgName"])
            if "FixedVersion" in i:
                if i["PkgName"] in suggested_upgrades:
                    suggested_upgrades[i["PkgName"]].add(i["FixedVersion"])
                else:
                    suggested_upgrades[i["PkgName"]] = set()
                    suggested_upgrades[i["PkgName"]].add(i["FixedVersion"])
            if i["VulnerabilityID"] not in cve_set:
                severity[i["Severity"]]+=1
            print(i["VulnerabilityID"],file=f)
            cve_set.add(i["VulnerabilityID"])
            print("Package Name : ",i["PkgName"],file=f)
            print("Severity : ",i["Severity"],file=f)
            if "Title" in i:
                print("Title : ",i["Title"],file=f)
            if "Descreption" in i:
                print("Descreption : ",i["Description"],file=f)
            print("CVSS : ",i["CVSS"],file=f)
            print("\n................\n",file=f)
    final_res[name[:-4]]=(severity,package_set)
    upgrades[name[:-4]] = suggested_upgrades
    print("------------------------",file=f)
    print(cve_set,'\n',package_set,'\n',suggested_upgrades,"\n",severity,file=f)
    f.close()
# print("\n\n\n\n\n")
f = open("res.txt",'w')
print("Vulnerability Counts and Vulnerable Packages : \n")
print("Vulnerability Counts and Vulnerable Packages : \n",file=f)
print(" "*60,"|CRITICAL|","|HIGH|","|MEDIUM|","|LOW|","|TOTAL|","\tPACKAGES",sep="")
print(" "*60,"|CRITICAL|","|HIGH|","|MEDIUM|","|LOW|","|TOTAL|","\tPACKAGES",sep="",file=f)
for i,j in final_res.items():
    print(i.ljust(60," "),end="")
    print(i.ljust(60," "),end="",file=f)
    tot = 0
    for a in j[0]:
        print(str(j[0][a]).center(len(a)+1," "),end=" ")
        print(str(j[0][a]).center(len(a)+1," "),end=" ",file=f)
        tot+=j[0][a]
    print(str(tot).center(5," "),end="\t")
    print(str(tot).center(5," "),end="\t",file=f)
    print(j[1])
    print(j[1],file=f)
    # print("\n---------------------\n")
print("\n\n\n\n\n")
print("\n\n\n\n\n",file=f)
print("Possible Upgrades to fix Vulnerabilities : ")
print("Possible Upgrades to fix Vulnerabilities : ",file=f)
for i,j in upgrades.items():
    print(i)
    print(i,file=f)
    print("***************")
    print("***************",file=f)
    for a,b in j.items():
        print(a,"\t",b)
        print(a,"\t",b,file=f)
    print("....................................................\n")
    print("....................................................\n",file=f)
f.close()