HELP_1 = """✅ <u>Yönetici Komutları:</u>

c kanal oynatma anlamına gelir.

/pause veya /cpause - Çalınan müziği duraklatın.

/resume veya /cresume - Duraklatılan müziği devam ettirir.

/mute veya /cmute - Çalan müziğin sesini kapatır.

/unmute veya /cunmute - Sessiz müziğin sesini açar.

/shuffle veya /cshuffle - Sıraya alınan çalma listesini rastgele karıştırır.

/atla veya /cskip - Geçerli çalan müziği atla.

/son veya /cstop - Müzik çalmayı durdurur.

/restart veya /reload - """ sohbetiniz için botu yeniden başlatın

HELP_2 = """✅<u> Yetkili Kullanıcılar: </u>
Kimlik Doğrulama Kullanıcılar, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

/auth [Kullanıcı Adı] - Grubun YETKİ LİSTESİNE bir kullanıcı ekleyin.

/unauth [Kullanıcı adı] - Bir kullanıcıyı grubun YETKİLENDİRME LİSTESİ'nden kaldırın.

/authusers - Grubun YETKİLENDİRME LİSTESİNİ kontrol edin."""

HELP_3 = """⚠️ <u>KARA LİSTE SOHBET İŞLEVİ:</u>

/blacklistchat [CHAT_ID] - Müzik Botu kullanılarak yapılan tüm sohbetleri kara listeye alın

/whitelistchat [CHAT_ID] - Müzik Botu kullanılarak kara listeye alınan tüm sohbetleri beyaz listeye ekleyin

/blacklistedchat - Kara listedeki tüm sohbetleri kontrol edin.


👤 <u>ENGELLENMİŞ FONKSİYON:</u>

/block [Kullanıcı Adı veya Kullanıcıya Yanıtla] - Kullanıcının bot komutlarını kullanmasını engeller.

/unblock [Kullanıcı Adı veya Kullanıcıya Yanıtla] - Bir kullanıcıyı Bot'un Engellenen Listesinden kaldırın.

/blockedusers - Engellenen Kullanıcı Listelerini kontrol edin
"""

HELP_4 = """🌐 <u>YAYIN İŞLEVİ:</u>
/broadcast [Mesaj Gönder veya Mesaja Yanıt Ver] - Herhangi bir mesajı Bot'un Sunulan Sohbetlerine yayınla.

<u>yayın seçenekleri:</u>

-pin : Bu mesajınızı sabitleyecektir

-pinloud : Bu, mesajınızı yüksek sesli bildirimle sabitler

-user : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır.

-assistant : Bu, mesajınızı botunuzun asistan hesabından yayınlayacaktır.

-nobot : Bu, botunuzu mesaj yayınlamamaya zorlar

Örnek: /broadcast -user -assistant -pin Hello Testing

"""
HELP_5 = """✅<u> Ekstra Komutlar: </u>

/loop veya /cloop [etkinleştir/devre dışı bırak] veya [1-10 arası sayılar]
- Etkinleştirildiğinde bot, sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır. Varsayılan olarak 10 kez.

/dil veya /langs : dili İngilizce'den türçeye'ya değiştirmek için

/lyrics [Müzik Adı] - Web'de belirli bir Müziğin Şarkı Sözlerini arar.."""

HELP_6 = """✅ <u>Bot'un Sunucu Oynatma Listeleri:</u>

/playlist - Sunuculardaki Kayıtlı Çalma Listenizi Kontrol Edin.

/deleteplaylist - Çalma listenizdeki kayıtlı müzikleri silin

/oynat - Kayıtlı Çalma Listenizi Sunuculardan oynatmaya başlayın."""

HELP_7 = """✨ ping cmd'si:

/ping - Bot'a ping atın ve Bot'un Ram, Cpu vb. istatistiklerini kontrol edin.

/stats - En İyi 10 Parçanın Küresel İstatistiklerini, Botun En İyi 10 Kullanıcısını, Bottaki En İyi 10 Sohbeti, Sohbette Oynanan En İyi 10 Sohbeti vb...."""

HELP_8 = """✅<u> Komutları Çal: </u>

Kullanılabilir Komutlar = oynat, bgt, vplay, cplay

ForcePlay Komutları = playforce, bgtforce vplayforce, cplayforce

c kanal oynatma anlamına gelir.
v video oynatma anlamına gelir.
kuvvet, kuvvet oyunu anlamına gelir.

/oynat veya /bgt veya /voynat veya /cplay - Bot, sesli sohbette verilen sorgunuzu oynatmaya veya sesli sohbetlerdeki canlı bağlantıları yayınlamaya başlayacaktır.

/playforce veya /force veya /vplayforce veya /cplayforce - Force Play, sesli sohbette geçerli çalınan parçayı durdurur ve aranan parçayı sırayı bozmadan/temizlemeden anında çalmaya başlar.

/channelplay [Sohbet kullanıcı adı veya kimliği] veya [Devre Dışı Bırak] - Kanalı bir gruba bağlayın ve kanalınızın sesli sohbetinde grubunuzdan müzik akışı yapın.."""

HELP_9 = """🔰 <u>SUDO KULLANICILARI EKLE VE KALDIR:</u>

/addsudo [Kullanıcı adı veya kullanıcıya yanıt ver]

/delsudo [Kullanıcı Adı veya Kullanıcıya Cevap Ver]

🛃 <u>HEROKU:</u>

/usage - Dyno Kullanımı.

🌐 <u>YAPILANDIRMA DEĞİŞKENLERİ:</u>

/get_var - Heroku veya .env'den bir yapılandırma değişkeni alın.

/del_var - Heroku veya .env'deki tüm değişkenleri silin.

/set_var [Var Name] [Value] - Heroku veya .env üzerinde bir Var Ayarlayın veya Bir Var Güncelleyin. Var ve Değerini boşlukla ayırın.


🤖 <u>BOT KOMUTLARI:</u>

/reboot - Botunuzu yeniden başlatın.
/update - Botu Güncelle.
/speedtest - Sunucu hızlarını kontrol edin
/maintenance [etkinleştir / devre dışı bırak]
/logger [etkinleştir / devre dışı bırak] - Bot, aranan sorguları günlükçü grubunda günlüğe kaydeder.
/get_log [Satır Sayısı] - Heroku veya vps'ten botunuzun günlüğünü alın. Her ikisi için de işe yarar.

⚡️ <u>ÖZEL BOT İŞLEVİ:</u>
/authorize [CHAT_ID] - Botunuzu kullanmak için sohbete izin verin.
/unauthorize [CHAT_ID] - Sohbetin botunuzu kullanmasına izin vermeyin.
/authorized - Botunuzun izin verilen tüm sohbetlerini kontrol edin.
"""

HELP_10 = """🤑 <u>Aktif Sohbetler:</u>

/activevoice - Bottaki aktif sesli sohbetleri kontrol edin.
/activevideo - Bottaki etkin video görüşmelerini kontrol edin.
/autoend [enable|disable] - Kimse dinlemiyorsa 3 dakika sonra otomatik akışın sonlandırılmasını etkinleştirin.."""

HELP_11 = """😅 <u> botla başladı</u>
/start : botu başlat

/help : Komutların ayrıntılı açıklamalarını içeren Komut Yardımcı Menüsünü alın.

/reboot : sohbetiniz için botu yeniden başlatın.

/settings - Satır içi düğmelerle tüm grubun ayarlarını alın.

/sudolist - Müzik Botunun Sudo Kullanıcılarını Kontrol Et"""

HELP_12 = """👤 <u>GBAN İŞLEVİ:</u>

/gban [Kullanıcı Adı veya Bir kullanıcıya yanıt ver] - Bir kullanıcıyı botun sunulan sohbetinden yasaklayın ve onun botunuzu kullanmasını engelleyin.

/ungban [Kullanıcı Adı veya Kullanıcıya Cevap Ver] - Bir kullanıcıyı Bot'un yasaklı Listesinden kaldırın ve botunuzu kullanmasına izin verin

/gbannedusers - Gbanned Kullanıcı Listelerini kontrol edin."""

HELP_13 = """🆔 <u>Kimlik/BİLGİ İŞLEVİ:</u>

/id veya /info - Kullanıcı bilgilerini oluşturmak için kullanılan bu cmd."""

HELP_14 = """ <u>GOOGLE İŞLEVİ:</u>

/google - Google'dan Başka Her Şeyi Ara."""

HELP_15 = """ <u>GÖRÜNTÜ İŞLEVİ:</u>

/image - """ Resmini Al

HELP_16 = """ <u>DAHA FAZLA İŞLEV:</u>

/ask - Herhangi bir şey sor

/bikash - Bikash'ın kim olduğunu kontrol edin

/owner - bu reponun yaratıcısının kim olduğunu kontrol edin

/donate - bot sahibine bağış yapın 🙂"""

HELP_17 = """ <u>REPO İŞLEVİ:</u>

/repo - """ deposu için

HELP_18 = """ <u>ARAMA İŞLEVİ:</u>

/seek veya /cseek - İleri Müziği istediğiniz süreye göre arayın

/seekback veya /cseekback - Geriye doğru Müziği istediğiniz süreye göre arayın."""
