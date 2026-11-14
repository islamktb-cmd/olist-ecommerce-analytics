"""
مراحل العمل
upload File
over view
clean data
"""

import numpy as np
import pandas as pd


#upload File و وضعه فى متغير df
df = pd.read_csv("olist_order_items_dataset.csv")
print ("tabel content is \n",df)

print("info is :")
df.info()##معلومات عن الجدول من حيث عدد الصفوف والاعمده ونوع كل عمود وعدد القيم الغير فارغه

print("Total Duplicates is : \n", df.duplicated().sum())
print ("data shape is : \n",df.shape) #لمعرفه حجم الجدول 

print("Missing Values (Nulls) is :\n",df.isnull().sum())
print ("data type is :\n",df.dtypes)#معرفة ال data type

print ("sample 10 is :\n",df.sample(10)) #عرض عينه عشوائيه حسب القيمه المطلوبه بين ()

#?تصحيح أنواع البيانات 
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])

print("Data Types After Conversion\n", df.dtypes)



#? حفظ الملف بعد التنظيف
save_path = r"D:\my-projects\python\my final project\cleaned_olist_order_items_dataset.csv1.csv"
df.to_csv(save_path, index=False)