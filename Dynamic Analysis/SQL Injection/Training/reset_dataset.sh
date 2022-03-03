echo "Removing Dataset folder and its contents"
rm -rf Dataset/*
echo "Done"
echo "Creating paths Dataset/Attack/csv and Dataset/Normal/csv"
mkdir -p Dataset/Attack/csv
mkdir -p Dataset/Normal/csv
echo "Done"
echo "Parsing sysdig data"
python3 parse_sysdig_data.py
echo "Done"
echo "Generating csv files"
python3 convert_to_csv.py
echo "Done"