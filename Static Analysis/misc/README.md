# Static Analysis of Images

trivy_results contains all the image vulnerabilities of each image obtained by scanning with trivy. \
Has json and table form for viewing. \
 \
libraries_used and libraries_needed have results of running dpkg -S on all files obtained from pmap. \
Vulnerabilities.txt has the vulnerbilities for each image as well as a total of all vulns at the bottom. \
Edit print_vulns.py to modify the format in which the vulns are printed. [or to get other info printed as well].
