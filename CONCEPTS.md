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