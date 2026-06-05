import boto3
from connections import connection

def load_raw_customer_churn():
    conn = connection()
    curr = conn.cursor()

    query = """
    COPY raw_customer_churn
    FROM 's3://pro-at-22/raw/telecom_customer_churn.csv'
    IAM_ROLE 'arn:aws:iam::050451400118:role/service-role/AmazonRedshift-CommandsAccessRole-20260604T224736'
    CSV
    IGNOREHEADER 1
    DELIMITER ','
    EMPTYASNULL
    BLANKSASNULL
    TRUNCATECOLUMNS;
    """

    curr.execute(query)
    conn.commit()

    print("Raw data loaded successfully")

    curr.close()
    conn.close()

def insert_churn_data():
    conn = connection()
    curr = conn.cursor()
    query="""

        INSERT INTO customer_churn (
        customer_id,
        gender,
        age,
        city,
        zip_code,
        tenure,
        monthly_charges,
        total_charges,
        customer_status
    )

        SELECT
            customer_id,
            gender,
            age,
            city,
            zip_code,
            tenure_in_months,
            monthly_charge,
            total_charges,
            customer_status
        FROM raw_customer_churn
        
        """
    curr.execute(query)
    conn.commit()
    print("data inserted successsfully")
    curr.close()
    conn.close()

def insert_zip_population():
    conn = connection()
    curr = conn.cursor()
    query="""
    COPY zip_population
    FROM 's3://pro-at-22/raw/telecom_zipcode_population.csv'
    IAM_ROLE 'arn:aws:iam::050451400118:role/service-role/AmazonRedshift-CommandsAccessRole-20260604T224736'
    CSV
    IGNOREHEADER 1
    DELIMITER ','
    EMPTYASNULL
    BLANKSASNULL
    TRUNCATECOLUMNS;
    """
    
    curr.execute(query)
    print("Data inserted in zip table")

    conn.commit()
    curr.close()
    conn.close()

    
# insert_churn_data()
insert_zip_population()