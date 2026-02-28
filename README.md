🧠 Pnömoni (Zatürre) Teşhis Sistemi - Yapay Zeka (Deep Learning)
Bu proje, göğüs röntgeni görüntülerini analiz ederek pnömoni teşhisi koyan bir Karar Destek Sistemi (KDS) çalışmasıdır. Proje, derin öğrenme mimarileri kullanılarak tıbbi görüntüleme alanında yardımcı bir tanı aracı olarak geliştirilmiştir.

🔬 Teknik Özellikler
Model Mimarisi: VGG16 (Convolutional Neural Networks - CNN)

Kütüphaneler: Python, TensorFlow, Keras, OpenCV

Veri İşleme: Görüntü boyutlandırma, normalizasyon ve veri artırımı (Data Augmentation) teknikleri kullanılmıştır.

📂 Proje İçeriği
main.py: Modelin eğitim ve test süreçlerini yöneten ana akış.

model_yapi.py: VGG16 tabanlı derin öğrenme katmanlarının tanımlandığı dosya.

veri_yukleyici.py: Görüntü veri setinin modele uygun şekilde yüklenmesi ve işlenmesi.

Not: Eğitilmiş model dosyası (.h5), dosya boyutu limitleri nedeniyle bu depoda yer almamaktadır. Talep edilmesi durumunda paylaşılabilir.
