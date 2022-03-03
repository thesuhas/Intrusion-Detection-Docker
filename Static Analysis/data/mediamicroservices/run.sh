cp ../scripts/* .
python3 parse_compose.py
mkdir trivy_results
mkdir trivy_results/table
mkdir trivy_results/json
python3 get_vulnerabilities.py
sudo docker-compose up -d
sleep 120
mkdir pmap
python3 get_pmap_data.py
mkdir libraries_needed
python3 get_libraries.py
python3 unique_libraries.py
docker-compose images > cont_image_map.txt
mkdir vulnerability_list
python3 print_vulnerabilities.py