import json
from mydb import ard_db


class arduino_database:

    def get_passenger_details(ph_number):
        # print(passenger_id,fullname,ph_number,addr)
        conn = ard_db.my_db_connect()
        cur = conn.cursor()
        query = '''SELECT * FROM `users` WHERE ph_number =%s ORDER BY passenger_id DESC LIMIT 1'''
        cur.execute(query,(ph_number,))
        row_headers = [x[0] for x in cur.description]
        data = cur.fetchall()

        return data

    def add_luggage_details(passenger_id, luggage_dec, rfid):
        # print(passenger_id,fullname,ph_number,addr)
        conn = ard_db.my_db_connect()
        cur = conn.cursor()
        query = '''INSERT INTO `luggage_details`(`passenger_id`, `luggage_dec`, `rfid`) VALUES(%s,%s,%s)'''
        userdata = (passenger_id, luggage_dec, rfid)
        cur.execute(query, userdata)
        conn.commit()

    def get_passenger_phone(rfid):
        # print(passenger_id,fullname,ph_number,addr)
        conn = ard_db.my_db_connect()
        cur = conn.cursor()
        query = f"SELECT users.ph_number FROM `users` INNER JOIN luggage_details ON users.passenger_id=luggage_details.passenger_id and luggage_details.rfid=\"{rfid}\""
        cur.execute(query)
        result = cur.fetchone()
        return result[0]

    def reg_passenger(passenger_data):
        conn = ard_db.my_db_connect()
        cur = conn.cursor()
        query = '''INSERT INTO `users`( `fullname`, `ph_number`, `addr`) VALUES (%s,%s,%s)'''
        cur.execute(query, tuple((passenger_data.values())))
        conn.commit()

