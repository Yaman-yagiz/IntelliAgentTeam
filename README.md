# AI Tabanlı Proje Planlama Sistemi

Bu proje, yapay zeka teknolojilerini kullanarak kapsamlı proje planları oluşturmaya yardımcı olan, çoklu uzman yaklaşımı kullanılan bir sistemdir.

## Özellikler

- **Çoklu Uzman Yaklaşımı**: Farklı rollerde (Proje Yöneticisi, UX Tasarımcısı, Yazılım Mimarı, Ekip Lideri) AI ajanları kullanarak kapsamlı analiz sağlar.
- **Uzmanlar Arası Etkileşim**: Uzman AI ajanlar arasında sıralı bilgi akışı ile gerçek bir tartışma ortamı simüle edilir.
- **Kapsamlı Analiz**: Her uzman kendi alanında detaylı analizler yaparak projenin farklı yönlerini ele alır.
- **Terminal Çıktısı**: Tüm uzman görüşleri ve analizler konsolda anlaşılır şekilde sunulur.
- **Modüler Mimari**: Kolayca genişletilebilir ve yeni özellikler eklenebilir mimari yapı.

## Gereksinimler

- Python 3.8 veya üstü
- Gemini API anahtarı (Google AI Studio)

## Kurulum

1. Repoyu klonlayın:
   ```
   git clone https://github.com/yourusername/ai-project-planner.git
   cd ai-project-planner
   ```

2. Gerekli paketleri yükleyin:
   ```
   pip install -r requirements.txt
   ```

3. Gemini API anahtarınızı ayarlayın:
   ```
   # .env dosyasına API anahtarınızı ekleyin
   GEMINI_API_KEY=sizin_api_anahtarınız
   ```

## Kullanım

1. Proje açıklamanızı `src/data/project_description.txt` dosyasına ekleyin.

2. Programı çalıştırın:
   ```
   python main.py
   ```

3. Analiz sonuçları terminal ekranında gösterilecektir.

## Proje Yapısı

```
├── main.py                      # Ana program
├── requirements.txt             # Bağımlılıklar
├── .env                         # Çevre değişkenleri
├── src/                         # Kaynak kod
│   ├── agents/                  # Ajan modülleri
│   │   ├── __init__.py          # Ajan paketi tanımı
│   │   └── agents.py            # Ajan sınıfları ve fonksiyonları
│   ├── core/                    # Çekirdek modüller
│   │   ├── __init__.py          # Çekirdek paket tanımı
│   │   └── config.py            # Yapılandırma ayarları
│   ├── data/                    # Veri ve içerik
│   │   ├── __init__.py          # Veri paketi tanımı
│   │   ├── project_description.txt  # Proje açıklaması
│   │   └── instructions/        # Ajan talimatları
│   └── utils/                   # Yardımcı modüller
│       ├── __init__.py          # Yardımcı paket tanımı
│       └── helpers.py           # Yardımcı fonksiyonlar
```

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın. 