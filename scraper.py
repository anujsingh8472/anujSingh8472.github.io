import gspread
import json

# Google Sheets API से कनेक्ट करो
gc = gspread.service_account(filename="credentials.json")  
sh = gc.open("Exam Updates")  
worksheet = sh.sheet1  

# डेटा लोड करो
data = worksheet.get_all_records()

# JSON फाइल में सेव करो
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Data.json अपडेट हो गया!")
