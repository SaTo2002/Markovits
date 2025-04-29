import mysql.connector

# الاتصال بقاعدة البيانات
conn = mysql.connector.connect(
    host="localhost",          # أو IP السيرفر لو مش محلي
    user="SaTo",      # اسم المستخدم في MySQL
    password="123.456/789",      # كلمة السر
    database="stok_data"  # اسم القاعدة اللي عاوز تتصل بيها
)

# إنشاء الكورسور للتعامل مع البيانات
cursor = conn.cursor()

# مثال: جلب كل البيانات من جدول
cursor.execute("SELECT * FROM alldata")

# طباعة النتائج
for row in cursor.fetchall():
    print(row)

# اغلاق الاتصال بعد الانتهاء
cursor.close()
conn.close()
