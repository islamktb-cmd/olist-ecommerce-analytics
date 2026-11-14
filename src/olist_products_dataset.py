"""
مراحل العمل
upload File
over view
clean data
"""

import numpy as np
import pandas as pd


#upload File و وضعه فى متغير df
df = pd.read_csv("olist_products_dataset.csv")
print ("tabel content is \n",df)

print("info is :")
df.info()##معلومات عن الجدول من حيث عدد الصفوف والاعمده ونوع كل عمود وعدد القيم الغير فارغه

print("Total Duplicates is : \n", df.duplicated().sum())
print ("data shape is : \n",df.shape) #لمعرفه حجم الجدول 

print ("sample 10 is :\n",df.sample(10)) #عرض عينه عشوائيه حسب القيمه المطلوبه بين ()

print ("data type is :\n",df.dtypes)#معرفة ال data type
print("Missing Values (Nulls) is :\n",df.isnull().sum())

# فلترة الصفوف اللي اسم القسم فيها (Null)

missing_data = df[df['product_category_name'].isnull()]
columns_to_show = [
    'product_id', 
    'product_category_name', 
    'product_name_lenght', 
    'product_description_lenght',
    'product_photos_qty', 
    'product_weight_g', 
    'product_length_cm', 
    'product_height_cm', 
    'product_width_cm'
]
# السطر ده بيجبر البايثون يعرض كل العواميد وميخبيش حاجة في النقط
pd.set_option('display.max_columns', None)
print("missing category null", missing_data[columns_to_show])



#استبدال الـ Null في عمود (product_category_name) بكلمة Unknown وتوحيد شكل النص
df['product_category_name'] = df['product_category_name'].fillna('Unknown').str.strip().str.title()

# استبدال الـ Null بصفر (0) في العواميد التالية:
# product_name_lenght, product_description_lenght, product_photos_qty
# product_weight_g, product_length_cm, product_height_cm, product_width_cm
df['product_name_lenght'] = df['product_name_lenght'].fillna(0)
df['product_description_lenght'] = df['product_description_lenght'].fillna(0)
df['product_photos_qty'] = df['product_photos_qty'].fillna(0)
df['product_weight_g'] = df['product_weight_g'].fillna(0)
df['product_length_cm'] = df['product_length_cm'].fillna(0)
df['product_height_cm'] = df['product_height_cm'].fillna(0)
df['product_width_cm'] = df['product_width_cm'].fillna(0)

#! 3. إرجاع كل عمود رقمي لنوع الأرقام الصحيحة (int64) بعد ما خلصنا من الـ Null
df['product_name_lenght'] = df['product_name_lenght'].astype('int64')
df['product_description_lenght'] = df['product_description_lenght'].astype('int64')
df['product_photos_qty'] = df['product_photos_qty'].astype('int64')
df['product_weight_g'] = df['product_weight_g'].astype('int64')
df['product_length_cm'] = df['product_length_cm'].astype('int64')
df['product_height_cm'] = df['product_height_cm'].astype('int64')
df['product_width_cm'] = df['product_width_cm'].astype('int64')

# ==========================================
# التأكد من نجاح العملية
# ==========================================
print("--- Missing Values After Cleaning ---")
print(df.isnull().sum())

print("\n--- Data Types After Cleaning ---")
print(df.dtypes)

# حفظ الملف بعد التنظيف
save_path = r"D:\my-projects\python\my final project\cleaned_olist_products_dataset1.csv"
df.to_csv(save_path, index=False)