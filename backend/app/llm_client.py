import os
import requests
import mysql.connector

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"   # Replace for safety


def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=os.environ.get("MYSQL_DATABASE", "sales_db")
    )


def fetch_sales(limit=10):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT id, product, quantity, total_price, created_at
    FROM sales
    ORDER BY created_at DESC
    LIMIT %s
    """

    cursor.execute(query, (limit,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def call_openrouter(system_prompt, user_prompt, model=None):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model or "openrouter/sherlock-dash-alpha",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",  "content": user_prompt},
        ],
        "temperature": 0.2
    }

    response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]
