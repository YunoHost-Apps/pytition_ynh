<!--
N.B.: Questo README è stato automaticamente generato da <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NON DEVE essere modificato manualmente.
-->

# Pytition per YunoHost

[![Livello di integrazione](https://dash.yunohost.org/integration/pytition.svg)](https://dash.yunohost.org/appci/app/pytition) ![Stato di funzionamento](https://ci-apps.yunohost.org/ci/badges/pytition.status.svg) ![Stato di manutenzione](https://ci-apps.yunohost.org/ci/badges/pytition.maintain.svg)

[![Installa Pytition con YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Leggi questo README in altre lingue.](./ALL_README.md)*

> *Questo pacchetto ti permette di installare Pytition su un server YunoHost in modo semplice e veloce.*  
> *Se non hai YunoHost, consulta [la guida](https://yunohost.org/install) per imparare a installarlo.*

## Panoramica

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Versione pubblicata:** 2.8~ynh2

**Prova:** <https://demo.pytition.org>

## Screenshot

![Screenshot di Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentazione e risorse

- Sito web ufficiale dell’app: <https://pytition.org>
- Documentazione ufficiale per gli amministratori: <https://pytition.readthedocs.io/en/latest/>
- Repository upstream del codice dell’app: <https://github.com/pytition/Pytition>
- Store di YunoHost: <https://apps.yunohost.org/app/pytition>
- Segnala un problema: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Informazioni per sviluppatori

Si prega di inviare la tua pull request alla [branch di `testing`](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Per provare la branch di `testing`, si prega di procedere in questo modo:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
o
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Maggiori informazioni riguardo il pacchetto di quest’app:** <https://yunohost.org/packaging_apps>
