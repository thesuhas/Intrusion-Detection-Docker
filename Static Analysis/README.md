Create a new folder **[WITHOUT '_' IN THE NAME]** and copy the run.sh file and docker-compose.yml file into the folder.\
Run the run.sh script in the created folder.\
The overall results are found in res.txt.\
The vulnerability_list folder contains the exposed vulnerabilities of each container.\
The unique libraries used by each container are found in the libraries_needed folder and pmap results for each container in the pmap folder.\
The trivy results folder stores all the vulnerabilities of every container in table an json format.



The following tasks are performed by these scripts :
1) extract image names - parse_compase.py
2) run trivy on all images [.json and .txt results] - get_vulnerabilities.py
3) start the microservice application - docker-compose up command
4) run pmap on the main process of each container and obtain all files [.so and .jar] being used - get_pmap_data.py
5) run dpkg -S "path/to/file" on every entry obtained by pmap to get all libraries - get_libraries.py
6) get all unique libraries being used by each container - unique_libraries.py
7) check trivy results and obtain all vulnerabilities image has that might be a threat - print_vulnerabilities.py
