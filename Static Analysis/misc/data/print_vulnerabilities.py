import os
import json
files_list = []
path_to_files = "./libraries_needed/"
path_to_vulnerabilities = "./trivy_results/json/"
prefix = "CVE-codewisdom-ts-"
for i,j,k in os.walk(path_to_files):
    files_list.extend(k)
final_res = {}
upgrades = {}
for name in files_list:
    # print("\nImage Name : ",name[:-4])
    # print("***********************")
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
                severity[i["Severity"]]+=1
    final_res[name[:-4]]=(severity,package_set)
    upgrades[name[:-4]] = suggested_upgrades
    print("------------------------",file=f)
    print(package_set,'\n',suggested_upgrades,"\n",severity,file=f)
    f.close()
# print("\n\n\n\n\n")
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
print("\n\n\n\n\n")
print("Possible Upgrades to fix Vulnerabilities : ")
for i,j in upgrades.items():
    print(i)
    print("***************")
    for a,b in j.items():
        print(a,"\t",b)
    print("....................................................\n")
