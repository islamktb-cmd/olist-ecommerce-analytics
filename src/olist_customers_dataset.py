"""
upload File
over view
clean data
"""

import numpy as np
import pandas as pd


#upload File و وضعه فى متغير df
df = pd.read_csv("olist_customers_dataset.csv")
print ("tabel content is \n",df)

print("info is :")
df.info()##معلومات عن الجدول من حيث عدد الصفوف والاعمده ونوع كل عمود وعدد القيم الغير فارغه

print("Missing Values (Nulls) is :\n",df.isnull().sum())

print("Total Duplicates is : \n", df.duplicated().sum())
print ("data shape is : \n",df.shape) #لمعرفه حجم الجدول 

print ("sample 10 is :\n",df.sample(10)) #عرض عينه عشوائيه حسب القيمه المطلوبه بين ()

print ("data type is :\n",df.dtypes)#معرفة ال data type

print ("column name is :\n",df.columns) #معرفه اسماء الاعمده

df['customer_zip_code_prefix'] = ("0000" + df['customer_zip_code_prefix'].astype(str)).str[-5:] ##تحويل عمود customer_zip_code_prefix الى str و اضافه 4 اصفار امام القيمه و اخذ اخر 5 ارقام فقط
print("info is :")
df.info()##معلومات عن الجدول من حيث عدد الصفوف والاعمده ونوع كل عمود وعدد القيم الغير فارغه

# تكبير أول حرف من كل كلمة وإزالة المسافات الزايدة للمدن
df['customer_city'] = df['customer_city'].str.title().str.strip()

# تحويل الولايات لحروف كابيتال وإزالة المسافات الزايدة
df['customer_state'] = df['customer_state'].str.upper().str.strip()


df.to_csv(r"D:\my-projects\python\my final project\cleaned_olist_customers_dataset.csv1", index=False)