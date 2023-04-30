import pymysql

db = pymysql.connect(
    host='localhost', user='root', password='123', database='graduate-design')
cursor = db.cursor()

sqlStr = 'TRUNCATE TABLE activeTCP;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE cpuPercentage;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE imapStatus;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE jamesStatus;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE openSnoop;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE passiveTCP;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE pidPerSec;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE popStatus;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE processCount;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE residentMemorySize;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE runQSlower;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE smtpStatus;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE tcpClose;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE tcpConnLat;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE tcpLife;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE threadSnoop;'
cursor.execute(sqlStr)
db.commit()
sqlStr = 'TRUNCATE TABLE virtualMemorySize;'
cursor.execute(sqlStr)
db.commit()

cursor.close()
db.close()