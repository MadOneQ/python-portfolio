import sqlite3

DB_FILE = "sensor_data.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

#    DROP OLD TABLE
cursor.execute("DROP TABLE IF EXISTS readings")
conn.commit()

#    CREATE NEW TABLE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        temp      REAL,
        humidity  REAL,
        distance  REAL,
        light     INTEGER,
        motion    INTEGER
    )
""")
conn.commit()
print("Database updated.")
conn.close()

#    INSERT FUNCTION
def insert_reading(conn, timestamp, temp, humidity, distance, light, motion):
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO readings (timestamp, temp, humidity, distance, light, motion)
                   VALUES (?, ?, ?, ?, ?, ?)
                   """, (timestamp, temp, humidity, distance, light, motion))
    conn.commit()
