# 🧹 Discord Slash Komut Temizleyici

Bu araç, Discord bot'unuzdan tüm slash komutlarını hızlı ve otomatik bir şekilde temizlemek için tasarlanmıştır.

## ✨ Özellikler

- 🌐 Global komutları temizleme
- 🏠 Sunucu (guild) komutlarını temizleme
- ⏱️ Rate limit yönetimi
- 📊 Detaylı konsol çıktısı

## 🚀 Kurulum

1. Repoyu klonlayın
2. Gerekli paketleri yükleyin:
   ```
   pip install discord.py aiohttp
   ```
3. `config.json` dosyasını oluşturun:
   ```json
   {
     "token": "BOT_TOKEN",
     "application_id": "BOT_APPLICATION_ID"
   }
   ```

## 💻 Kullanım

```
python main.py
```

Program çalıştığında, botunuzun sahip olduğu tüm slash komutlarını bulup silecektir.

## 📋 Çıktı Örneği

```
ExampleBot#1234 olarak giriş yapıldı!
🔍 Toplam 3 global komut bulundu. Silme işlemi başlıyor...
✅ Global komut silindi: yardım
✅ Global komut silindi: ping
✅ Global komut silindi: info
🔍 Test Sunucusu sunucusunda 2 komut bulundu. Silme işlemi başlıyor...
✅ Guild komutu silindi: test (Test Sunucusu)
✅ Guild komutu silindi: echo (Test Sunucusu)
```

## ⚠️ Uyarılar

- Bu araç, **tüm** slash komutlarını siler. Seçici silme işlemi şu anda desteklenmemektedir.
- İşlemi geri alamazsınız, bu yüzden dikkatli kullanın.

## 🔧 Geliştirme

Katkıda bulunmak isterseniz, lütfen bir "pull request" açın veya önerilerinizi "issues" bölümünde paylaşın. 
