"""
مراحل العمل
upload File
over view
clean data
"""

import numpy as np
import pandas as pd


#upload File و وضعه فى متغير df
df = pd.read_csv("olist_orders_dataset.csv")
print ("tabel content is \n",df)

print("info is :")
df.info()##معلومات عن الجدول من حيث عدد الصفوف والاعمده ونوع كل عمود وعدد القيم الغير فارغه

print("Missing Values (Nulls) is :\n",df.isnull().sum())

print("Total Duplicates is : \n", df.duplicated().sum())
print ("data shape is : \n",df.shape) #لمعرفه حجم الجدول 

print ("sample 10 is :\n",df.sample(10)) #عرض عينه عشوائيه حسب القيمه المطلوبه بين ()

print ("data type is :\n",df.dtypes)#معرفة ال data type

print ("column name is :\n",df.columns) #معرفه اسماء الاعمده

print("Duplicate Rows Details:\n",df[df.duplicated(subset=['geolocation_zip_code_prefix'], keep=False)].sort_values(by="geolocation_zip_code_prefix"))

#حذف ال duplicate rows
df=df.drop_duplicates()
#عرض محتويات الجدول بعد حذف ال duplicate rows
print ("duplicate values\n", df.duplicated().sum())

# تكبير أول حرف من كل كلمة وإزالة المسافات الزايدة للمدن
df['geolocation_city'] = df['geolocation_city'].str.title().str.strip()

# تحويل الولايات لحروف كابيتال وإزالة المسافات الزايدة
df['geolocation_state'] = df['geolocation_state'].str.upper().str.strip()

print ("tabel content is \n",df)
# تقريب خطوط الطول والعرض لـ 4 أرقام عشرية لتخفيف حجم البيانات وتسريع رسم الخرائط
df['geolocation_lat'] = df['geolocation_lat'].round(4)
df['geolocation_lng'] = df['geolocation_lng'].round(4)
df['geolocation_zip_code_prefix'] = ("0000" + df['geolocation_zip_code_prefix'].astype(str)).str[-5:]
print("info is :")
df.info()

# الحفظ بالاسم الجديد مع إضافة رقم 1 للمقارنة
save_path = r"D:\my-projects\python\my final project\cleaned_olist_geolocation_dataset1.csv"
df.to_csv(save_path, index=False)