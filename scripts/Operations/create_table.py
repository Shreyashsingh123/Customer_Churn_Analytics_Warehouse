import psycopg2
from connections import connection

class create_table:
        
    def churn_table(self):
        conn=connection()
        curr=conn.cursor()
        query="""
                CREATE TABLE IF NOT EXISTS customer_churn (
                customer_id VARCHAR(50),
                gender VARCHAR(20),
                age INT,
                city VARCHAR(100),
                zip_code VARCHAR(20),
                tenure INT,
                monthly_charges DECIMAL(10,2),
                total_charges DECIMAL(12,2),
                customer_status VARCHAR(50)
                );
            """
        curr.execute(query)
        print("Churn table created")
        conn.commit()
        curr.close()
        conn.close()

    def zip_population_table(self):
        conn=connection()
        curr=conn.cursor()
        query="""           
                CREATE TABLE zip_population(
                    zip_code VARCHAR(20),
                    population BIGINT
                );
            
            """
        curr.execute(query)
        print("table created successfully")
        conn.commit()
        curr.close()
        conn.close()

    def Analytical_table(self):
        conn = connection()
        curr = conn.cursor()
        query="""
                CREATE TABLE IF NOT EXISTS analytical_table(
                customer_id VARCHAR(50),
                city VARCHAR(100),
                zip_code VARCHAR(20),
                population BIGINT,
                tenure INT,
                monthly_charges DECIMAL(10,2),
                total_charges DECIMAL(12,2),
                customer_status VARCHAR(50)

                )
        
        DISTSTYLE KEY
        DISTKEY(zip_code)
        SORTKEY(tenure)
        """

        curr.execute(query)
        conn.commit()
        print("Analytical table created successfully")
        
        insert_sql="""
                Insert into analytical_table
                SELECT 
                t.customer_id,
                t.city,
                t.zip_code,
                z.population,
                t.tenure,
                t.monthly_charges,
                t.total_charges,
                t.customer_status
                FROM customer_churn t
                join zip_population z on 
                t.zip_code=z.zip_code
            
                """
        curr.execute(insert_sql)
        conn.commit()
        print("Data inserted in final Analytical table")
        curr.close()
        conn.close()
c=create_table()
c.Analytical_table()





