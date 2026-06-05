from connections import connection

def raw_staging_table():
    conn=connection()
    curr=conn.cursor()
    query="""
    CREATE TABLE raw_customer_churn (
    customer_id VARCHAR(50),
    gender VARCHAR(20),
    age INT,
    married VARCHAR(20),
    number_of_dependents INT,
    city VARCHAR(100),
    zip_code VARCHAR(20),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    number_of_referrals INT,
    tenure_in_months INT,
    offer VARCHAR(50),
    phone_service VARCHAR(20),
    avg_monthly_long_distance_charges DECIMAL(10,2),
    multiple_lines VARCHAR(20),
    internet_service VARCHAR(20),
    internet_type VARCHAR(50),
    avg_monthly_gb_download DECIMAL(10,2),
    online_security VARCHAR(20),
    online_backup VARCHAR(20),
    device_protection_plan VARCHAR(20),
    premium_tech_support VARCHAR(20),
    streaming_tv VARCHAR(20),
    streaming_movies VARCHAR(20),
    streaming_music VARCHAR(20),
    unlimited_data VARCHAR(20),
    contract VARCHAR(50),
    paperless_billing VARCHAR(20),
    payment_method VARCHAR(100),
    monthly_charge DECIMAL(10,2),
    total_charges DECIMAL(12,2),
    total_refunds DECIMAL(12,2),
    total_extra_data_charges DECIMAL(12,2),
    total_long_distance_charges DECIMAL(12,2),
    total_revenue DECIMAL(12,2),
    customer_status VARCHAR(50),
    churn_category VARCHAR(100),
    churn_reason VARCHAR(500)
    )
    """
    curr.execute(query)
    print("Raw table created sucessfully")
    conn.commit()
    curr.close()
    conn.close()

raw_staging_table()
