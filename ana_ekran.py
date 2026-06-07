
import sys
import os
import numpy as np
from datetime import datetime

# PDF OLUŞTURMA
from fpdf import FPDF

# TENSORFLOW VE PYQT5
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(os.path.dirname(PyQt5.__file__), "Qt5", "plugins")


class Uygulama(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("BitirmeProjem.ui", self)

    self.secilen_dosya_yolu = ""
    self.hasta_bilgileri_kaydedildi = False
    self.son_teshis_sonucu = ""
    self.kds_onerisi = ""

    # BUTON BAĞLANTILARI
    self.btn_rontgen_sec.clicked.connect(self.resim_yukle)
    self.btn_analiz_et.clicked.connect(self.analiz_et)
    self.btn_kaydet.clicked.connect(self.hasta_kaydet)
    self.btn_pdf_indir.clicked.connect(self.pdf_olustur)

    # QSS KISMI
    self.setStyleSheet("""
            QMainWindow, QWidget { background-color: #2b2d30; color: #e0e0e0; font-family: 'Segoe UI', Arial; font-size: 13px; }
            #lbl_ana_baslik { color: #b35900; font-size: 20px; font-weight: bold; }
            #lbl_resim_alani { border: 2px dashed #555555; border-radius: 8px; background-color: #1e1f22; color: #888888; }
            QGroupBox { border: 2px solid #b35900; border-radius: 8px; margin-top: 15px; font-weight: bold; }
            QGroupBox::title { subcontrol-origin: margin; left: 15px; padding: 0 5px; color: #b35900; }
            QPushButton { background-color: #3c3f41; color: #ffffff; border: 2px solid #b35900; padding: 6px; font-weight: bold; border-radius: 6px; }
            QPushButton:hover { background-color: #b35900; color: #ffffff; }
            QLineEdit, QComboBox, QTextEdit, QPlainTextEdit { background-color: #1e1f22; border: 1px solid #555555; border-radius: 4px; padding-left: 10px; color: #ffffff; }
            QLineEdit:focus, QComboBox:focus, QTextEdit:focus, QPlainTextEdit:focus { border: 1px solid #b35900; }
            QProgressBar { border: 1px solid #555555; border-radius: 5px; text-align: center; color: white; font-weight: bold; }
            QProgressBar::chunk { background-color: #b35900; border-radius: 4px; }
        """)

    # CİNSİYET KUTUSU
    try:
      self.cmb_cinsiyet.clear()
      self.cmb_cinsiyet.addItems(["Seçiniz", "Kadın", "Erkek"])
    except Exception as e:
      print(f"Cinsiyet kutusu hatası: {e}")

    print("🧠 Yapay Zeka Modeli Yükleniyor...")
    try:
      self.model = load_model("zaturre_modeli_pycharm.h5")
      print("✅ Model Hazır.")
    except Exception as e:
      print(f"❌ Model Yükleme Hatası: {e}")

  def resim_yukle(self):
    try:
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog

      dosya_yolu, _ = QFileDialog.getOpenFileName(self, "Röntgen Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg)",
                                                  options=options)

      if dosya_yolu:
        self.secilen_dosya_yolu = dosya_yolu
        pixmap = QPixmap(dosya_yolu)
        self.lbl_resim_alani.setPixmap(pixmap)
        self.lbl_resim_alani.setScaledContents(True)
        self.lbl_resim_alani.setStyleSheet("border: 2px solid #b35900; border-radius: 8px;")

        # Yeni resim yüklendiğinde eski sonuçları temizle
        self.lbl_teshis_sonucu.setText("Analiz İçin 'Analiz Et' Butonuna Basın")
        self.prg_yuzde.setValue(0)
        try:
          self.txt_kds_oneri.clear()
        except:
          pass
    except Exception as e:
      print(f"Resim yükleme hatası: {e}")

  def analiz_et(self):
    if not self.secilen_dosya_yolu:
      QMessageBox.warning(self, "Uyarı", "Lütfen önce bir röntgen görüntüsü seçin!")
      return

    try:
      img = load_img(self.secilen_dosya_yolu, target_size=(224, 224))
      img_array = img_to_array(img)
      img_array = np.expand_dims(img_array, axis=0)
      img_array /= 255.0

      tahmin = self.model.predict(img_array)
      zat_orani = float(tahmin[0][0]) * 100


      if zat_orani > 50:
        self.son_teshis_sonucu = "ZATURRE TESPIT EDILDI"
        self.prg_yuzde.setValue(int(zat_orani))

        if zat_orani > 80:
          self.kds_onerisi = "KRITIK SEVIYE: Ileri derece pnomoni bulgulari mevcuttur. Acil uzman hekim konsultasyonu ve hospitalizasyon degerlendirilmelidir."
        else:
          self.kds_onerisi = "ORTA SEVIYE: Erken/Orta derece pnomoni infiltrasyonu suphesi. Semptom takibi ve ampirik antibiyotik tedavisi planlamasi onerilir."
      else:
        saglam_orani = 100 - zat_orani
        self.son_teshis_sonucu = "NORMAL / SAGLIKLI"
        self.prg_yuzde.setValue(int(saglam_orani))
        self.kds_onerisi = "KLINIK DURUM NORMAL: Akciger parankim alanlari temiz izlenmistir. Patolojik infiltrasyon saptanmamistir. Rutin takibe devam edilmesi onerilir."


      try:
        self.lbl_teshis_sonucu.setText(self.son_teshis_sonucu)
        self.txt_oneri_kutusu.setText(self.kds_onerisi)
      except Exception as e:
        print(f"Ekrana yazdırma hatası: {e}")

    except Exception as e:
      print(f"❌ Analiz Hatası: {e}")

  def hasta_kaydet(self):
    self.hasta_bilgileri_kaydedildi = True
    self.btn_kaydet.setText("KAYDEDİLDİ ✅")
    self.btn_kaydet.setStyleSheet("background-color: #2E8B57; color: white; border-radius: 6px; font-weight: bold;")
    self.btn_kaydet.setEnabled(False)

  def tr_karekter_temizle(self, metin):
    trans = str.maketrans("şŞıİğĞüÜöÖçÇ", "sSiIgGuUoOcC")
    return metin.translate(trans)

  def pdf_olustur(self):
    if not self.hasta_bilgileri_kaydedildi:
      QMessageBox.critical(self, "Hata", "Lütfen önce 'Kaydet' butonuna basınız!")
      return

    if not self.son_teshis_sonucu:
      QMessageBox.critical(self, "Hata", "Lütfen önce 'Analiz Et' butonuna basınız!")
      return

    try:
      ad = self.tr_karekter_temizle(self.txt_ad_soyad.text())
      yas = self.txt_yas.text()
      cinsiyet = self.tr_karekter_temizle(self.cmb_cinsiyet.currentText())
      tarih = datetime.now().strftime("%d-%m-%Y %H:%M")

      pdf = FPDF()
      pdf.add_page()

      # Başlık
      pdf.set_font("Arial", 'B', 16)
      pdf.cell(200, 15, txt="AKCIGER RONTGENI YAPAY ZEKA ANALIZ RAPORU", ln=True, align='C')
      pdf.line(10, 25, 200, 25)  # Başlık altı çizgisi sabit
      pdf.ln(10)

      # Hasta Bilgileri
      pdf.set_font("Arial", 'B', 12)
      pdf.cell(200, 8, txt="HASTA BILGILERI", ln=True)
      pdf.set_font("Arial", '', 11)
      pdf.cell(100, 8, txt=f"Hasta Ad Soyad: {ad}")
      pdf.cell(100, 8, txt=f"Rapor Tarihi: {tarih}", ln=True)
      pdf.cell(100, 8, txt=f"Yas: {yas}")
      pdf.cell(100, 8, txt=f"Cinsiyet: {cinsiyet}", ln=True)

      # ÇİZGİ SORUNU ÇÖZÜMÜ:
      # get_y() ile metnin tam bittiği dikey konumu alıyoruz, üzerine 3 birim boşluk ekleyip çiziyoruz.
      guncel_y = pdf.get_y()
      pdf.line(10, guncel_y + 3, 200, guncel_y + 3)
      pdf.ln(10)

      # Teşhis
      pdf.set_font("Arial", 'B', 12)
      pdf.cell(200, 8, txt="YAPAY ZEKA TESHIS SONUCU", ln=True)
      pdf.set_font("Arial", 'B', 14)
      pdf.cell(200, 10, txt=self.tr_karekter_temizle(self.son_teshis_sonucu), ln=True)
      pdf.ln(5)

      # KDS
      pdf.set_font("Arial", 'B', 12)
      pdf.cell(200, 8, txt="KLINIK KARAR DESTEK SISTEMI ONERISI", ln=True)
      pdf.set_font("Arial", '', 11)
      pdf.multi_cell(0, 7, txt=self.tr_karekter_temizle(self.kds_onerisi))

      # Dosya Kaydetme Penceresi
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      varsayilan_isim = f"Rapor_{ad.replace(' ', '_')}.pdf"
      kayit_yolu, _ = QFileDialog.getSaveFileName(self, "PDF Raporunu Kaydet", varsayilan_isim, "PDF Dosyaları (*.pdf)",
                                                  options=options)

      if kayit_yolu:
        if not kayit_yolu.endswith('.pdf'):
          kayit_yolu += '.pdf'
        pdf.output(kayit_yolu)
        QMessageBox.information(self, "Başarılı", f"Rapor Başarıyla Kaydedildi!\nKonum: {kayit_yolu}")

    except Exception as e:
      print(f"❌ PDF Hatası: {e}")
      QMessageBox.critical(self, "Hata", f"PDF oluşturulamadı: {e}")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  pencere = Uygulama()
  pencere.show()
  sys.exit(app.exec_())