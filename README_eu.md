<!--
Ohart ongi: README hau automatikoki sortu da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>ri esker
EZ editatu eskuz.
-->

# Pytition YunoHost-erako

[![Integrazio maila](https://dash.yunohost.org/integration/pytition.svg)](https://dash.yunohost.org/appci/app/pytition) ![Funtzionamendu egoera](https://ci-apps.yunohost.org/ci/badges/pytition.status.svg) ![Mantentze egoera](https://ci-apps.yunohost.org/ci/badges/pytition.maintain.svg)

[![Instalatu Pytition YunoHost-ekin](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Irakurri README hau beste hizkuntzatan.](./ALL_README.md)*

> *Pakete honek Pytition YunoHost zerbitzari batean azkar eta zailtasunik gabe instalatzea ahalbidetzen dizu.*  
> *YunoHost ez baduzu, kontsultatu [gida](https://yunohost.org/install) nola instalatu ikasteko.*

## Aurreikuspena

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Paketatutako bertsioa:** 2.8~ynh2

**Demoa:** <https://demo.pytition.org>

## Pantaila-argazkiak

![Pytition(r)en pantaila-argazkia](./doc/screenshots/stop_doing_teams.webp)

## Dokumentazioa eta baliabideak

- Aplikazioaren webgune ofiziala: <https://pytition.org>
- Administratzaileen dokumentazio ofiziala: <https://pytition.readthedocs.io/en/latest/>
- Jatorrizko aplikazioaren kode-gordailua: <https://github.com/pytition/Pytition>
- YunoHost Denda: <https://apps.yunohost.org/app/pytition>
- Eman errore baten berri: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Garatzaileentzako informazioa

Bidali `pull request`a [`testing` abarrera](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

`testing` abarra probatzeko, ondorengoa egin:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
edo
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Informazio gehiago aplikazioaren paketatzeari buruz:** <https://yunohost.org/packaging_apps>
