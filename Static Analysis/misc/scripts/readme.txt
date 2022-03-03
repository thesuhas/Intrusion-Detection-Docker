run parse_compose.py to parse a docker-compose.yml file in the folder and get all the images in the compose file in image_names.txt
run get_vulnerabilities.py and it pulls and scans (trivy) all image names present in image_names.txt.
run get_pmap_data.sh or get_pmap_data_alt.sh to get pmap data of all 64 containers.
run parse_pmap_data.py and it parses all pmap data files in pmap folder and lists all .so filenames in so_files folder and other filename in other_files folder, for each container respectively.
