#    Variables
- Always reassign or changes are lost: **df =** df.method()
- Variable names should reflect their content (*results vs df*)

#    Separator Detection
with open(filepath, 'r') as f:
    first_line = f.readline()
    separator = ";" if ";" in first_line else ","
df = pd.read_csv(filepath, sep = separator)

#    any() keyword matching
any(k in description for k in ["SALARY", "SALAIRE", "FREELANCE"])

#    SQL Injection
xxx cursor.execute(f"INSERT INTO readings VALUES ({temp})")
vvv cursor.execute(f"INSERT INTO readings VALUES (?)", (temp,))

#    Serial Reading
line = ser.readline().decode("utf-8").strip()

#    API
- Structured request/response between scripts and servers (*Analogy of customer, waiter and kitchen*)
- API key stored in .env (*never in code or Git*)
- Authentication: **requests.get("url", headers={})**
- 
