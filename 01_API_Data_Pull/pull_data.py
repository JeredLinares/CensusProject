'''
Pull data from census.gov API
By: JD Linares
Created: 2024 01 02
Updated: 2024 01 03
'''

import csv
import requests
import time

# Demographic Profile
# https://api.census.gov/data/2020/dec/dp?get=DP1_0001C&for=county:*

# Demographic and Housing Characteristics
# https://api.census.gov/data/2020/dec/dhc?get=NAME&for=county:*&in=state:*

# Variables to pull
# CSV format: "Description" , Variable, For, In

request_string_a1 = "https://api.concus.gov/data/2020/dec/dp?"
request_string_a2 = "https://api.concus.gov/data/2020/dec/dhc?"

request_string_b = "get="
#   NAME for geography
#   <Variable>

request_string_c = "&for="
#   state,county
#   Place

request_string_d = "&in="
#   state

request_string_e = "&key="      #Enter your own key using .env file
#   Note to self: Never add key in script

with open("data_to_pull.csv") as f:
    reader = csv.reader(f)
    for row in reader: 
        print(row)






