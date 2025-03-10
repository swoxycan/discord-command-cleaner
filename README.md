# Discord Command Cleaner

Discord sunucunuzdaki tüm slash (/) komutlarını tek seferde temizleyen basit bir Discord botu.

## 📋 Özellikler

- Tüm slash komutlarını otomatik olarak temizler
- Rate limit koruması
- İşlem durumunu anlık olarak bildirir
- İşlem bitiminde otomatik kapanır

## ⚙️ Kurulum

1. Projeyi bilgisayarınıza indirin
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install discord.py aiohttp
   ```
3. `config.json` dosyasını düzenleyin:
   ```json
   {
       "token": "BOT_TOKEN_BURAYA",
       "application_id": "UYGULAMA_ID_BURAYA"
   }
   ```

## 🚀 Kullanım

1. Bot tokeninizi ve uygulama ID'nizi `config.json` dosyasına girin
2. Botu çalıştırın:
   ```bash
   python main.py
   ```
3. Bot otomatik olarak:
   - Discord'a bağlanacak
   - Tüm slash komutlarını silecek
   - İşlem bitiminde kendini kapatacak

## 📝 Çıktı Bildirimleri

- ✅ `Komut silindi: [komut_adı]` - Başarılı silme işlemi
- ⚠️ `Rate limit aşıldı! [X] saniye bekleniyor...` - Rate limit uyarısı
- ⚠️ `Silme hatası: [hata_kodu]` - Hata durumu

## 📌 Gereksinimler

- Python 3.8+
- discord.py
- aiohttp

## 🔒 Güvenlik Notları

- `config.json` dosyasını asla public olarak paylaşmayın
- Bot tokeninizi güvende tutun
- `.gitignore` dosyanıza `config.json`'ı eklemeyi unutmayın

## ⚠️ Dikkat

Bu bot, uygulamanıza ait TÜM slash komutlarını siler. Kullanmadan önce emin olun.

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
