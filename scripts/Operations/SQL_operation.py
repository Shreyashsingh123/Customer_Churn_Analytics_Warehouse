from .connections import connection


class SQL_Operations:

    def __init__(self):
        self.conn = connection()
        self.curr = self.conn.cursor()

    def churn_rate(self):

        query = """
        SELECT
            ROUND(
                COUNT(CASE WHEN customer_status = 'Churned' THEN 1 END)
                * 100.0 / NULLIF(COUNT(*),0),
                2
            ) AS churn_rate
        FROM analytical_table;
        """

        self.curr.execute(query)

        result = self.curr.fetchone()

        print("\n######## CHURN RATE ########")
        print(f"Churn Rate (%): {result[0]}")

    def top_churn_cities(self):

        query = """
        SELECT
            city,
            COUNT(*) AS churned_customers
        FROM analytical_table
        WHERE customer_status = 'Churned'
        GROUP BY city
        ORDER BY churned_customers DESC
        LIMIT 10;
        """

        self.curr.execute(query)

        result = self.curr.fetchall()

        print("\n######## TOP CHURN CITIES ########")

        for city, count in result:
            print(f"{city}: {count}")

    def churn_distribution_by_tenure(self):

        query = """
        SELECT
            CASE
                WHEN tenure <= 12 THEN '0-12 Months'
                WHEN tenure <= 24 THEN '13-24 Months'
                WHEN tenure <= 48 THEN '25-48 Months'
                ELSE '49+ Months'
            END AS tenure_group,
            COUNT(*) AS churn_count
        FROM analytical_table
        WHERE customer_status = 'Churned'
        GROUP BY 1
        ORDER BY 1;
        """

        self.curr.execute(query)

        result = self.curr.fetchall()

        print("\n######## CHURN DISTRIBUTION BY TENURE ########")

        for tenure_group, churn_count in result:
            print(f"{tenure_group}: {churn_count}")

    def revenue_lost_due_to_churn(self):

        query = """
        SELECT
            ROUND(SUM(total_charges), 2) AS revenue_lost
        FROM analytical_table
        WHERE customer_status = 'Churned';
        """

        self.curr.execute(query)

        result = self.curr.fetchone()

        print("\n######## REVENUE LOST DUE TO CHURN ########")
        print(f"Revenue Lost: {result[0]}")

    def population_vs_customer_count(self):

        query = """
        SELECT
            zip_code,
            population,
            COUNT(customer_id) AS customer_count
        FROM analytical_table
        GROUP BY zip_code, population
        ORDER BY customer_count DESC;
        """

        self.curr.execute(query)

        result = self.curr.fetchall()

        print("\n######## POPULATION VS CUSTOMER COUNT ########")

        for zip_code, population, customer_count in result:
            print(
                f"Zip Code: {zip_code}, "
                f"Population: {population}, "
                f"Customers: {customer_count}"
            )

    def close_connection(self):
        self.curr.close()
        self.conn.close()


# if __name__ == "__main__":

#     sql_ops = SQL_Operations()

#     sql_ops.churn_rate()
#     sql_ops.top_churn_cities()
#     sql_ops.churn_distribution_by_tenure()
#     sql_ops.revenue_lost_due_to_churn()
#     sql_ops.population_vs_customer_count()

#     sql_ops.close_connection()