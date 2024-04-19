#!/bin/bash

# Function to run the client.py for a given website name
run_client() {
    website_name="$1"
    python3 client.py 127.0.0.1 5559 "$website_name" 20
}

# Check if the argument (file name) is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <file_name>"
    exit 1
fi

# Read website names from the text file and execute the client for each
input_file="$1"
if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found."
    exit 1
fi

# Create a directory for storing the performance report files
mkdir -p performance_reports

# Initialize the total time variable
total_time=0

# Loop through each website name and run the client
while read -r website_name; do
    echo "Running client.py for $website_name"
    start_time=$(date +%s.%N)
    run_client "$website_name"
    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc)
    total_time=$(echo "$total_time + $execution_time" | bc)
    echo "Total time for all requests: $execution_time"
done < "$input_file"

# Display the total time for all requests
echo "Total time for all requests: $total_time seconds" >> performance_reports/report.txt