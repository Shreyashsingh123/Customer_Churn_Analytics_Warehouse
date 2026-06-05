from scripts.Operations.SQL_operation import SQL_Operations

def main():

    sql_ops = SQL_Operations()
    sql_ops.churn_rate()
    sql_ops.top_churn_cities()
    sql_ops.churn_distribution_by_tenure()
    sql_ops.revenue_lost_due_to_churn()
    sql_ops.population_vs_customer_count()
    sql_ops.close_connection()


if __name__ == "__main__":
    main()