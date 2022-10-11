# import Flask
import mysql.connector
class ard_db:
    def my_db_connect():
        connection=mysql.connector.connect(host="bx5kna7dzxyytbpwobko-mysql.services.clever-cloud.com",
        user="ui4c1dtkr7ibq9j9",
        password="jBLQQWC9isApg8oLjX4t",
        database="bx5kna7dzxyytbpwobko")
        return connection
# cur=mydb.cursor()
# cur.execute("select * from users")
# result=cur.fetchall()
# for r in result:
#     print(r)