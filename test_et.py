import os
from tensorflow.keras.models import load_model
from veri_yukleyici import veri_jeneratorlerini_hazirla

# Klasör yolun (main.py ile birebir aynı)
VERI_SETI_YOLU = r"C:\Users\Esra Alataş\Downloads\archive\chest_xray\chest_xray"


def sinavi_baslat():
  print("🧠 Model (Beyin) hafızadan yükleniyor, lütfen bekle...")
  # Sol tarafta gördüğümüz model dosyasını yüklüyoruz
  model = load_model("zaturre_modeli_pycharm.h5")

  print("📂 Test resimleri (624 adet) hazırlanıyor...")
  # Sadece test verisi lazım olduğu için ilk ikisini '_' ile geçiyoruz
  _, _, test_gen = veri_jeneratorlerini_hazirla(VERI_SETI_YOLU, 224, 32)

  print("\n🔍 Final Sınavı başladı! Lütfen bitene kadar bekle...")
  # Modeli sınava sokuyoruz
  loss, accuracy = model.evaluate(test_gen)

  print("\n" + "=" * 40)
  print("🏆 GERÇEK FİNAL SINAVI SONUCU (PYCHARM) 🏆")
  print("=" * 40)
  print(f"✅ Başarı Oranı (Accuracy) : % {accuracy * 100:.2f}")
  print(f"📉 Hata Oranı (Loss)       : {loss:.4f}")
  print("=" * 40)


if __name__ == "__main__":
  sinavi_baslat()