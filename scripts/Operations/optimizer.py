from connections import connection

def optimize_redshift():
    conn = connection()

    conn.autocommit = True

    curr = conn.cursor()

    curr.execute("VACUUM analytics;")
    print("Vacuum completed")

    curr.execute("ANALYZE analytics;")
    print("Analyze completed")

    curr.close()
    conn.close()

optimize_redshift()