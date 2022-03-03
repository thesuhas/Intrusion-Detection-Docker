import os
import json
files_list = []
path_to_files = "./libraries_needed/"
path_to_vulnerabilities = "./trivy_results/json/"
prefix = "CVE-codewisdom-ts-"
for i,j,k in os.walk(path_to_files):
    files_list.extend(k)
final_res = {}
for name in files_list:
    print("\nImage Name : ",name[:-4])
    print("***********************")
    f = open(path_to_files+name,'r')
    x = f.readlines()
    f.close()
    i = 0
    for j in x:
        if "----" in j:
            break
        i+=1
    x = x[i+1:]
    x = [i[:-1] for i in x]
    f = open(path_to_vulnerabilities+prefix+name[:-4]+".json",'r')
    vulns = json.load(f)
    f.close()
    cve_set = set()
    package_set = set()
    severity = {"CRITICAL":0,"HIGH":0,"MEDIUM":0,"LOW":0}
    vulns = vulns[0]["Vulnerabilities"]
    for i in vulns:
        if i["PkgName"] in x:
            if i["VulnerabilityID"] not in cve_set:
                print(i["VulnerabilityID"])
                cve_set.add(i["VulnerabilityID"])
                print("Package Name : ",i["PkgName"])
                package_set.add(i["PkgName"])
                print("Severity : ",i["Severity"])
                if "Title" in i:
                    print("Title : ",i["Title"])
                if "Descreption" in i:
                    print("Descreption : ",i["Description"])
                print("CVSS : ",i["CVSS"])
                print("\n................\n")
                severity[i["Severity"]]+=1
            else:
                package_set.add(i["PkgName"])
    final_res[name[:-4]]=(severity,package_set)
    print("------------------------")
print("\n\n\n\n\n")
print("Vulnerability Counts and Vulnerable Packages : \n")
print(" "*30,"|CRITICAL|","|HIGH|","|MEDIUM|","|LOW|","|TOTAL|","\tPACKAGES",sep="")
for i,j in final_res.items():
    print(i.ljust(30," "),end="")
    tot = 0
    for a in j[0]:
        print(str(j[0][a]).center(len(a)+1," "),end=" ")
        tot+=j[0][a]
    print(str(tot).center(5," "),end="\t")
    print(j[1])
    # print("\n---------------------\n")
