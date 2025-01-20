# -*- coding: utf-8 -*-
"""“araba veri seti”.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DpOgYT-eE6P9lLdARIee36zvHTnFyYkN
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics




# Veri dosyanızın yolunu belirtin
data_path = 'car data.csv'

# Verileri okuyun
df = pd.read_csv(data_path)
# İlk beş satırı görüntüleyin
df.head(150)

data_path = 'car data.csv'

# Verileri okuyun
df = pd.read_csv(data_path)

# DataFrame hakkında bilgi alın
df.info()

# Boş değerleri kontrol edin
null_values = df.isnull().sum()

# Boş değerleri yazdırın
print(null_values)

# Veri dosyanızın yolunu belirtin
data_path = 'car data.csv'

# Verileri okuyun
df = pd.read_csv(data_path)

# DataFrame hakkında istatistiksel bilgi alın
df.describe()

print(df.columns)

car_data = pd.read_csv("car data.csv")
print(car_data['Fuel_Type'].value_counts())
print(car_data['Seller_Type'].value_counts())
print(car_data['Transmission'].value_counts())

car_data = pd.read_csv("car data.csv")
fuel_type = car_data['Fuel_Type']
seller_type = car_data['Seller_Type']
transmission_type = car_data['Transmission']
selling_price = car_data['Selling_Price']

import matplotlib.pyplot as plt
import matplotlib.style as style

# Stili ayarla
style.use('ggplot')

# Yeni bir figür oluştur
fig = plt.figure(figsize=(15,5))

# Figürün üst başlığını ayarla
fig.suptitle('Visualizing categorical data columns')

# İlk alt grafiği seç
plt.subplot(1,3,1)

# Yakıt tipine göre satış fiyatını gösteren bir çubuk grafiği çiz
plt.bar(fuel_type, selling_price, color='royalblue')

# X ve Y eksenlerinin etiketlerini ayarla
plt.xlabel("Fuel Type")
plt.ylabel("Selling Price")

# İkinci alt grafiği seç
plt.subplot(1,3,2)

# Satıcı tipine göre satış fiyatını gösteren bir çubuk grafiği çiz
plt.bar(seller_type, selling_price, color='red')

# X ekseninin etiketini ayarla
plt.xlabel("Seller Type")

# Üçüncü alt grafiği seç
plt.subplot(1,3,3)

# Transmisyon tipine göre satış fiyatını gösteren bir çubuk grafiği çiz
plt.bar(transmission_type, selling_price, color='purple')

# X ekseninin etiketini ayarla
plt.xlabel('Transmission type')

# Grafiği göster
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Stili ayarla
plt.style.use('ggplot')

# Yeni bir figür oluştur ve bu figürü 1 satır ve 3 sütunlu bir ızgara halinde böler
fig, axes = plt.subplots(1,3,figsize=(15,5), sharey=True)

# Figürün üst başlığını ayarla
fig.suptitle('Visualizing categorical columns')

# Yakıt tipine göre satış fiyatını gösteren bir çubuk grafiği çiz ve bu grafiği ilk alt grafiğe yerleştir
sns.barplot(x=fuel_type, y=selling_price, ax=axes[0])

# Satıcı tipine göre satış fiyatını gösteren bir çubuk grafiği çiz ve bu grafiği ikinci alt grafiğe yerleştir
sns.barplot(x=seller_type, y=selling_price, ax=axes[1])

# Transmisyon tipine göre satış fiyatını gösteren bir çubuk grafiği çiz ve bu grafiği üçüncü alt grafiğe yerleştir
sns.barplot(x=transmission_type, y=selling_price, ax=axes[2])

# Grafiği göster
plt.show()

petrol_data = car_data.groupby('Fuel_Type').get_group('Petrol')
petrol_data.describe()

seller_data = car_data.groupby('Seller_Type').get_group('Dealer')
seller_data.describe()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Bağımsız ve bağımlı değişkenleri belirleyin
X = df.drop('Selling_Price', axis=1) # Tüm özellikler
y = df['Selling_Price'] # Hedef değişken

# Veri setini eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluşturun ve eğitin
model = LinearRegression()
model.fit(X_train, y_train)

from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df = pd.read_csv('car data.csv')


# OneHotEncoder nesnesi oluşturalım
encoder = OneHotEncoder(handle_unknown='ignore')

# Her bir kategorik sütun için one-hot encoding uygulayalım
for column in ['Car_Name', 'Fuel_Type', 'Seller_Type', 'Transmission']:
    # Sütunu one-hot encode edelim
    encoder_df = pd.DataFrame(encoder.fit_transform(df[[column]]).toarray())

    # one-hot encoded DataFrame'deki sütun isimlerini güncelleyelim
    encoder_df.columns = [f"{column}_{i}" for i in range(len(encoder_df.columns))]

    # one-hot encoded sütunları orijinal DataFrame'e ekleyelim
    df = pd.concat([df, encoder_df], axis=1)

    # Son olarak, orijinal sütunu DataFrame'den silelim
    df.drop(column, axis=1, inplace=True)

plt.figure(figsize=(10,7))
sns.heatmap(car_data.corr(numeric_only=True), annot=True)
plt.title('Correlation between the columns')
plt.show()

fig=plt.figure(figsize=(7,5))
plt.title('Correlation between present price and selling price')
sns.regplot(x='Present_Price', y='Selling_Price', data=car_data)

import matplotlib.pyplot as plt

# Tahminler yapma
y_pred = model.predict(X_test)

# Gerçek değerler ve tahminler arasındaki ilişkiyi gösteren bir dağılım grafiği çizme
plt.scatter(y_test, y_pred)
plt.xlabel('Gerçek Değerler')
plt.ylabel('Tahminler')
plt.title('Gerçek Değerler vs Tahminler')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Tahminler yapma
y_pred = model.predict(X_test)

# Gerçek değerler ve tahminler arasındaki ilişkiyi gösteren bir dağılım grafiği çizme
plt.scatter(y_test, y_pred)

# Çizgiyi ekleyin
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k-', color = 'r')

plt.xlabel('Gerçek Değerler')
plt.ylabel('Tahminler')
plt.title('Gerçek Değerler vs Tahminler')
plt.show()

# Veri çerçevenizi yükleyin
df = pd.read_csv('car data.csv')

# 'Car_Name' adlı sütuna göre gruplama yapın
grouped = df.groupby('Car_Name')

# Her grubun 'Fuel_Type', 'Seller_Type', 'Transmission' adlı değişkenlerinin modunu hesaplayın
mode_target_per_group = grouped[['Fuel_Type', 'Seller_Type', 'Transmission']].agg(pd.Series.mode)

# Sonucu yazdırın
print(mode_target_per_group)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Veri çerçevenizi yükleyin
df = pd.read_csv('car data.csv')

# Veri çerçevenizdeki sütunları yazdırın
print(df.columns)

# Scatter plot matrix oluşturun
sns.pairplot(df[['Selling_Price', 'Present_Price', 'Kms_Driven']])
plt.show()

from sklearn.metrics import r2_score

# Gerçek ve tahmin edilen değerler
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# R^2 puanını hesaplama
r2 = r2_score(y_true, y_pred)

print(f"R^2 puanı: {r2}")

