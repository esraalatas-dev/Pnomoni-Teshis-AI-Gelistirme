🧠 Masaüstü Entegreli Pnömoni (Zatürre) Teşhis Sistemi

Bu proje, göğüs röntgeni (X-Ray) görüntülerini derin öğrenme algoritmalarıyla analiz ederek pnömoni teşhisi koyan ve doktorlara yardımcı bir tanı aracı sunan Masaüstü Entegreli bir Karar Destek Sistemi (KDS) çalışmasıdır. Proje, güçlü bir yapay zeka modelini kullanıcı dostu bir masaüstü arayüzü ile uçtan uca birleştirir.

🔬 Teknik Özellikler & Teknoloji Yığını
Model Mimarisi: VGG16 (Convolutional Neural Networks - CNN) ve Transfer Learning

Arayüz (Desktop UI): PyQt5 / Qt Designer (.ui mimarisi)

Kütüphaneler & Araçlar: Python, TensorFlow, Keras, OpenCV, NumPy

Veri İşleme: Görüntü boyutlandırma (Resizing), normalizasyon ve veri artırımı (Data Augmentation) teknikleri.

📂 Proje İçeriği ve Dosya Yapısı
main.py: Uygulamanın ve arayüz döngüsünün başlatıldığı, ana akışı yöneten dosya.

ana_ekran.py: PyQt5 ile yazılmış, kullanıcının görsel yükleyip tahmini gördüğü masaüstü arayüz kontrol katmanı.

BitirmeProjem.ui: Qt Designer ile tasarlanmış, uygulamanın görsel arayüz şablonu.

model_yapi.py: VGG16 tabanlı derin öğrenme katmanlarının ve transfer learning süreçlerinin tanımlandığı dosya.

veri_yukleyici.py: Görüntü veri setinin modele uygun şekilde yüklenmesi, işlenmesi ve normalize edilmesi.

test_et.py: Modelin performansını ve doğruluk oranlarını bağımsız test verileriyle ölçen script.

⚠️ Not: Eğitilmiş model dosyası (zaturre_modeli_pycharm.h5), dosya boyutu limitleri nedeniyle bu depoda yer almamaktadır. Talep edilmesi durumunda paylaşılabilir.
