from datetime import datetime 

def find_day_of_week(date_str:str):
    now=datetime.strptime(date_str,"%Y-%m-%d")
    return now.strftime("%A")
 
print(find_day_of_week("2024-06-27"))

# Example Test Cases
# Input: "2024-06-27"
# Output: "Thursday"

print(find_day_of_week("2024-01-01"))

# Input: "2024-01-01"
# Output: "Monday"



