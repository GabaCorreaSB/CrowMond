#
# Copyright (c) 2025 Gabriel Correa dos Santos Barbosa
# All rights reserved.

import os
import time
import json
import subprocess
import psycopg2

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def init_db(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id SERIAL PRIMARY KEY,
            scenario TEXT,
            source_ip TEXT,
            message TEXT,
            created_at TIMESTAMP
        );
    """)

def insert_alert(cur, alert):
    scenario = alert.get('scenario', '')
    source_ip = alert.get('source', {}).get('ip', '')
    message = alert.get('message', '')
    created_at = alert.get('timestamp', '')
    cur.execute("""
        INSERT INTO alerts (scenario, source_ip, message, created_at)
        VALUES (%s, %s, %s, %s)
    """, (scenario, source_ip, message, created_at))

def fetch_alerts():
    result = subprocess.run(
        ["cscli", "alerts", "list", "-o", "json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return json.loads(result.stdout)

def main():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER,
        password=DB_PASSWORD, dbname=DB_NAME
    )
    cur = conn.cursor()
    init_db(cur)

    while True:
        print("[*] Fetching alerts...")
        alerts = fetch_alerts()
        for alert in alerts:
            insert_alert(cur, alert)
        conn.commit()
        time.sleep(60)

if __name__ == "__main__":
    main()
