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

# لستة بأسماء عواميد التواريخ
date_columns = [
    'order_purchase_timestamp', 
    'order_approved_at', 
    'order_delivered_carrier_date', 
    'order_delivered_customer_date', 
    'order_estimated_delivery_date'
]

# تحويلهم كلهم دفعة واحدة لنوع (datetime)
for col in date_columns:
    df[col] = pd.to_datetime(df[col])

print("\nData Types after cleaning:\n", df.dtypes)

# الحفظ بالاسم الجديد مع إضافة رقم 1 للمقارنة
save_path = r"D:\my-projects\python\my final project\cleaned_olist_orders_dataset1.csv"
df.to_csv(save_path, index=False)