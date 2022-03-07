rm -rf Dataset/*
mkdir -p Dataset/Attack/csv
mkdir -p Dataset/Normal/csv
python3 parse_sysdig_data.py
python3 convert_to_csv.py
