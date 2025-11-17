
import os
import mysql.connector
import pandas as pd
from typing import List, Dict, Any

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=os.environ.get("MYSQL_DATABASE", "sales_db")
    )

def query_to_dataframe(query: str) -> pd.DataFrame:
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def execute_query(query: str) -> List[Dict[str, Any]]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

# Analytics queries
def get_sales_summary():
    query = """
        SELECT 
            COUNT(sale_id) as total_sales,
            SUM(total_amount) as total_revenue,
            AVG(total_amount) as avg_order_value,
            COUNT(DISTINCT customer_id) as total_customers
        FROM sales
    """
    return execute_query(query)[0]

def get_top_products(limit=10):
    query = f"""
        SELECT 
            p.product_name,
            p.category,
            SUM(si.quantity) as total_sold,
            SUM(si.quantity * si.price_each) as revenue
        FROM sale_items si
        JOIN products p ON si.product_id = p.product_id
        GROUP BY si.product_id
        ORDER BY revenue DESC
        LIMIT {limit}
    """
    return execute_query(query)

def get_sales_by_category():
    query = """
        SELECT 
            p.category,
            COUNT(DISTINCT s.sale_id) as order_count,
            SUM(si.quantity * si.price_each) as revenue
        FROM sale_items si
        JOIN products p ON si.product_id = p.product_id
        JOIN sales s ON si.sale_id = s.sale_id
        GROUP BY p.category
        ORDER BY revenue DESC
    """
    return execute_query(query)

def get_sales_trend(period='month'):
    if period == 'month':
        query = """
            SELECT 
                DATE_FORMAT(sale_date, '%Y-%m') as period,
                COUNT(sale_id) as order_count,
                SUM(total_amount) as revenue
            FROM sales
            GROUP BY DATE_FORMAT(sale_date, '%Y-%m')
            ORDER BY period
        """
    else:
        query = """
            SELECT 
                DATE(sale_date) as period,
                COUNT(sale_id) as order_count,
                SUM(total_amount) as revenue
            FROM sales
            GROUP BY DATE(sale_date)
            ORDER BY period DESC
            LIMIT 30
        """
    return execute_query(query)

def get_top_customers(limit=10):
    query = f"""
        SELECT 
            c.name,
            c.email,
            COUNT(s.sale_id) as order_count,
            SUM(s.total_amount) as total_spent
        FROM customers c
        JOIN sales s ON c.customer_id = s.customer_id
        GROUP BY c.customer_id
        ORDER BY total_spent DESC
        LIMIT {limit}
    """
    return execute_query(query)

def get_payment_methods():
    query = """
        SELECT 
            payment_method,
            COUNT(sale_id) as count,
            SUM(total_amount) as revenue
        FROM sales
        GROUP BY payment_method
        ORDER BY revenue DESC
    """
    return execute_query(query)
