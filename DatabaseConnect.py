# Use a breakpoint in the code line below to debug your script.
import ibm_db
import ibm_db_dbi
import jdatetime


def dbConnect():
    try:
        connection = ibm_db.connect(
            "DATABASE=ICMS;HOSTNAME=192.168.33.74;PORT=50000;PROTOCOL=TCPIP;UID=rayan; PWD=rayan9708;", "", "")
        return connection
    except:
        print("Error in connection, sqlstate = ")
        errorState = ibm_db.conn_error()
        errorMsg = ibm_db.conn_errormsg()
        print(errorMsg)
        print(errorState)


ibm_db_conn = dbConnect()
conn = ibm_db_dbi.Connection(ibm_db_conn)
conn.tables('SYSCAT', '%')
sql = "select  * from CRM.TB_INVOLVED_PARTY fetch first 20 rows only"
stmt = ibm_db.exec_immediate(ibm_db_conn, sql)
# dictionary = ibm_db.fetch_both(stmt)
# print(dictionary.keys())
# while dictionary:
#     print("The ID is : ", dictionary["ID"])
#     print("The Name is : ", dictionary[3])
#     print("The LastName is : ", dictionary[4])
#     dictionary = ibm_db.fetch_both(stmt)
tuple_1 = ibm_db.fetch_tuple(stmt)
while tuple_1:
    print("The ID is : {} The name is : {} The LastName is {} : ".format(tuple_1[0], tuple_1[3], tuple_1[4]))
    tuple_1 = ibm_db.fetch_tuple(stmt)

    # import ibm_db
    # conn = ibm_db.connect("database","username","password")
    # sql = "SELECT EMPNO, LASTNAME FROM EMPLOYEE WHERE EMPNO > ? AND EMPNO < ?"
    # stmt = ibm_db.prepare(conn, sql)
    # max = 50
    # min = 0
    # # Explicitly bind parameters
    # ibm_db.bind_param(stmt, 1, min)
    # ibm_db.bind_param(stmt, 2, max)
    # ibm_db.execute(stmt)
    # # Process results
    #
    # # Invoke prepared statement again using dynamically bound parameters
    # param = max, min,
    # ibm_db.execute(stmt, param)
gregorian_date = jdatetime.date(1396, 2, 30).togregorian()
jalali_date = jdatetime.date.fromgregorian(day=19, month=5, year=2017)
fa_date = jdatetime.date(1397, 4, 23, locale='fa_IR')
fa_datetime = jdatetime.datetime(1397, 4, 23, 11, 40, 30, locale='fa_IR')
