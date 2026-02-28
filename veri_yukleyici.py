import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
def veri_jeneratorlerini_hazirla(veri_seti_yolu, img_size=224, batch_size=32):
  """
  Belirtilen klasör yolundaki verileri okur, ön işleme yapar ve hazırlar.
  """
  print(f"📂 Veriler şu konumdan yükleniyor: {veri_seti_yolu}")

  train_dir = os.path.join(veri_seti_yolu, 'train')
  val_dir = os.path.join(veri_seti_yolu, 'val')
  test_dir = os.path.join(veri_seti_yolu, 'test')

  # Veri Artırma (Data Augmentation) - Sadece Eğitim için
  train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
  )

  # Test ve Val için sadece normalizasyon
  test_val_datagen = ImageDataGenerator(rescale=1. / 255)

  print("--- Eğitim Seti ---")
  train_gen = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='binary'
  )

  print("--- Test Seti ---")
  test_gen = test_val_datagen.flow_from_directory(
    test_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False
  )

  # Validation seti (Eğer varsa)
  val_gen = test_val_datagen.flow_from_directory(
    val_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False
  )

  return train_gen, val_gen, test_gen