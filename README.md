# 🛣️ Şerit Tespit Pro - Gelişmiş Yol Şerit Algılama Aracı

Python + OpenCV ile gerçek zamanlı şerit tespiti, FPS takibi ve customizable ROI yapısı sunan masaüstü analiz aracı.

## 📋 İçindekiler
- Özellikler
- Gereksinimler
- Kurulum
- Kullanım
- Proje Yapısı
- Detaylı Özellikler
- Yol Haritası
- Katkıda Bulunma
- Lisans

## ✨ Özellikler
- 📷 Video veya kamera kaynağından gerçek zamanlı şerit algılama
- ✂️ ROI maskeleme ile odaklanılacak yol bölgesini daraltma
- ⚙️ Canny + Probabilistic Hough Lines kombinasyonu
- 📊 Anlık FPS hesaplama ve overlay
- 🎞️ Örnek giriş videoları ve kaydedilmiş çıktı (`sonuc.mp4`)
- 🪟 Platform bağımsız: Windows üzerinde test edildi, diğer platformlarda da çalışabilir

## 🚀 Gereksinimler
- Python 3.9 veya üzeri
- `opencv-python`, `numpy`
- GPU gerekmez; CPU yeterli
- Video girişi için yerel dosya veya kamera erişimi

## ⚙️ Kurulum

Adım 1 — Depoyu klonlayın:
```powershell
git clone https://github.com/<kullanici>/SeritTespit.git
cd SeritTespit
```

Adım 2 — (Opsiyonel) sanal ortam oluşturun:
```powershell
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Mac/Linux
```

Adım 3 — Bağımlılıkları yükleyin:
```powershell
pip install --upgrade pip
pip install opencv-python numpy
```

## 💻 Kullanım
```powershell
python road_line_detection.py
```

Temel iş akışı:
1. `road_line_detection.py` içindeki `cv2.VideoCapture("video2.mp4")` satırını:
   - Yerel video dosyası veya
   - Web kamerası (`0`) ile güncelleyin.
2. Betiği çalıştırın ve "img" penceresini izleyin.
3. FPS overlay ve yeşil çizgi maskesiyle eş-leşen şeritleri görün.
4. Çıkmak için uygulama penceresi aktifken `q` tuşuna basın.

## 📁 Proje Yapısı
```
SeritTespit/
├── road_line_detection.py   # Ana algoritma
├── video1.mp4               # Örnek video (gündüz)
├── video2.mp4               # Örnek video (gece/şehir)
├── sonuc.mp4                # Örnek çıktı kaydı
├── LICENSE                  # Unlicense metni
└── README.md                # Bu doküman
```

## 🔧 Detaylı Özellikler
### Şerit Algılama (Lane Detection)
- Gri tonlama, Gaussian blur (OpenCV default)
- Canny kenar algılama (`cv2.Canny(gray, 250, 120)`)
- ROI maskeleme (üçgen bölge): `(0, h)`, `(w/2, h/2)`, `(w, h)`
- Probabilistic Hough Lines (`cv2.HoughLinesP`) ile çizgi üretimi
- `drawLines()` yardımıyla tespit edilen çizgileri overlay etme

### Özelleştirilebilir Parametreler
- **Canny eşikleri**: Farklı ışık koşulları için optimize edin.
- **Hough parametreleri**: `threshold`, `minLineLength`, `maxLineGap` değişkenleri ile uzunluk/gap toleransı ayarlayın.
- **ROI köşeleri**: Farklı kamera perspektiflerinde poligon vertex listesi güncellenebilir.

### Performans ve İzleme
- Basit FPS ölçer (`time.time()` tabanlı)
- Overlay üzerinde FPS ve şeritler aynı anda gösterilir

## 🗺️ Yol Haritası
- [ ] Adaptif ROI ve perspektif düzeltme
- [ ] Sol/sağ şerit sınıflandırması ve eğim ölçümü
- [ ] Kalman filtresi ile çizgi takibi
- [ ] Video çıktısını kaydetme opsiyonu
- [ ] CLI argümanları ile parametre yönetimi
- [ ] Başsız ortamlara uygun kayıt modu

## 🤝 Katkıda Bulunma
1. Repoyu fork edin
2. Özellik dalı açın: `git checkout -b feature/AmazingFeature`
3. Değişiklikleri commit'leyin: `git commit -m "Özellik açıklaması"`
4. Dalınızı push edin: `git push origin feature/AmazingFeature`
5. Pull Request oluşturun

## ⚠️ Önemli Notlar
- Video dosyaları büyük; gerekirse `git lfs` ile yönetilebilir.
- OpenCV pencereleri başsız sunucularda çalışmaz; böyle ortamlarda `cv2.imwrite` veya video kaydı tercih edin.
- Şerit tespiti asfalttaki çizgilerin kontrastına bağlıdır; zayıf ışıkta parametreleri yeniden ayarlayın.

## 📝 Lisans
Bu proje **Unlicense** ile herkese açık alana adanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 👤 Yazar
Talha Eren  
GitHub: [@talha-eren](https://github.com/talha-eren)

## 🙏 Teşekkürler
- OpenCV ve NumPy topluluklarına
- Yol verisi sağlayan tüm açık kaynak projelere

## 📧 İletişim
Sorularınız için GitHub Issues açabilir veya doğrudan Talha Eren ile iletişime geçebilirsiniz.

## 🐛 Bilinen Sorunlar
- Yüksek çözünürlüklü videolarda FPS düşebilir.
- Aşırı parlak veya yağışlı şartlarda yanlış pozitifler artabilir.
- Script sonundaki `cap.release()` satırı eksik; çalıştırmadan önce tamamlayın.

## 💡 İpuçları
- Parametre değişikliklerini küçük adımlarla yapın; her değişiklik sonrası videoyu test edin.
- Web kamerası kullanırken sabit bir tripod tercih edin.
- Video üzerinde LUT/kontrast ayarı yaparak çizgi belirginliğini artırabilirsiniz.

⭐ Projeyi faydalı bulduysanız lütfen yıldız vermeyi düşünün!
