import sqlite3

DB_FILE = "sensor_data.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

#    ALL READINGS
print("=== All Readings ===")
cursor.execute("SELECT * FROM readings")
rows = cursor.fetchall()
for row in rows:
    print(row)

#    AVERAGE VALUES
print("\n=== Averages ===")
cursor.execute("""
    SELECT 
        ROUND(AVG(temp), 2)     AS avg_temp,
        ROUND(AVG(humidity), 2) AS avg_humidity,
        ROUND(AVG(distance), 2) AS avg_distance,
        ROUND(AVG(light), 2)    AS avg_light
    FROM readings
""")
print(cursor.fetchone())

#    LAST 5 READINGS
print("\n=== Last 5 Readings ===")
cursor.execute("""
    SELECT timestamp, temp, distance, light 
    FROM readings 
    ORDER BY id DESC 
    LIMIT 5
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
