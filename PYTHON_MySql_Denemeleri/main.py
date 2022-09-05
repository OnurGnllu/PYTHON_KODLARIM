import mysql.connector
def veri_gonder(currency_id , price , date): #(1, 83, '2022-08-17')
    conn = mysql.connector.connect(
        user='root', password='12345', host='127.0.0.1', database='onur_db')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL query to INSERT a record into the database.
    sql1 = "INSERT INTO dolar_birim(currency_id, price, dtarih)VALUES"
    values = (currency_id , price , date)
    str_values = str(values)
    sql_gonderilecek = sql1 + str_values

    try:
        # Executing the SQL command
        cursor.execute(sql_gonderilecek)

        # Commit your changes in the database
        conn.commit()

    except:
        # Rolling back in case of error
        conn.rollback()

    # Closing the connection
    conn.close()


def main():
    veri_gonder(1,13.2,'2022-08-17')


if __name__ == "__main__":
    main()
