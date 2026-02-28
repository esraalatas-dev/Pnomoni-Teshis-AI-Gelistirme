import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras import layers, models
def modeli_olustur(input_shape=(224, 224, 3)):
  """
  VGG16 tabanlı Transfer Learning modelini oluşturur ve döndürür.
  """
  print("🧠 Model mimarisi oluşturuluyor...")

  # 1. VGG16'yı indirme
  base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

  # 2. VGG16'nın ağırlıklarını dondur -- overfittingi önlemek için
  base_model.trainable = False

  # 3. Kendi katmanlarımızı ekleme
  model = models.Sequential([
    base_model,
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),  # Ezber bozucu
    layers.Dense(1, activation='sigmoid')  # Çıkış: 0 (Normal) veya 1 (Zatürre)
  ])

  # 4. Modeli derleme
  model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])

  return model