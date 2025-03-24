<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Pytition untuk YunoHost

[![Tingkat integrasi](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Status kerja](https://apps.yunohost.org/badge/state/pytition)
![Status pemeliharaan](https://apps.yunohost.org/badge/maintained/pytition)

[![Pasang Pytition dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Pytition secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Versi terkirim:** 2.8~ynh4

**Demo:** <https://demo.pytition.org>

## Tangkapan Layar

![Tangkapan Layar pada Pytition](./doc/screenshots/stop_doing_teams.webp)

## Dokumentasi dan sumber daya

- Website aplikasi resmi: <https://pytition.org>
- Dokumentasi admin resmi: <https://pytition.readthedocs.io/en/latest/>
- Depot kode aplikasi hulu: <https://github.com/pytition/Pytition>
- Gudang YunoHost: <https://apps.yunohost.org/app/pytition>
- Laporkan bug: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
atau
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
