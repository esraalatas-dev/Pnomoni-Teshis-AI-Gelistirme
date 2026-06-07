import os
# Kendi yazdığımız modülleri çağırıyoruz
from model_yapi import modeli_olustur
from veri_yukleyici import veri_jeneratorlerini_hazirla

# --- AYARLAR ---
VERI_SETI_YOLU = r"C:\Users\Esra Alataş\Downloads\archive\chest_xray\chest_xray"
IMG_BOYUTU = 224
EPOCH_SAYISI = 10
def baslat():
  # 1. Klasör Kontrolü
  if not os.path.exists(VERI_SETI_YOLU):
    print("❌ HATA: Veri seti klasörü bulunamadı!")
    print("Lütfen 'main.py' içindeki VERI_SETI_YOLU satırını düzeltin.")
    return
  # 2. Verileri Yükleme kısmı
  train_gen, val_gen, test_gen = veri_jeneratorlerini_hazirla(VERI_SETI_YOLU, IMG_BOYUTU)

  # 3. Modeli Oluşturma
  model = modeli_olustur(input_shape=(IMG_BOYUTU, IMG_BOYUTU, 3))
  model.summary()

  # 4. Eğitimi Başlat
  print("\n🚀 Eğitim Başlıyor...")
  history = model.fit(
    train_gen,
    epochs=EPOCH_SAYISI,
    validation_data=val_gen
  )

  # 5. Son Olrak Modeli Kaydet
  model.save("zaturre_modeli_pycharm.h5")
  print("\n✅ Eğitim bitti ve model kaydedildi.")


if __name__ == "__main__":
  baslat()