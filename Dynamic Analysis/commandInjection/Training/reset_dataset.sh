rm -rf parsed_data/*
mkdir -p parsed_data/Attack/csv
mkdir -p parsed_data/Normal/csv
python3 parse_sysdig_data.py
python3 convert_to_csv.py
