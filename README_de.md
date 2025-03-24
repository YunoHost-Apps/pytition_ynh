<!--
N.B.: Diese README wurde automatisch von <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> generiert.
Sie darf NICHT von Hand bearbeitet werden.
-->

# Pytition für YunoHost

[![Integrations-Level](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Funktionsstatus](https://apps.yunohost.org/badge/state/pytition)
![Wartungsstatus](https://apps.yunohost.org/badge/maintained/pytition)

[![Pytition mit YunoHost installieren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Dieses README in anderen Sprachen lesen.](./ALL_README.md)*

> *Mit diesem Paket können Sie Pytition schnell und einfach auf einem YunoHost-Server installieren.*  
> *Wenn Sie YunoHost nicht haben, lesen Sie bitte [die Anleitung](https://yunohost.org/install), um zu erfahren, wie Sie es installieren.*

## Übersicht

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Ausgelieferte Version:** 2.8~ynh4

**Demo:** <https://demo.pytition.org>

## Bildschirmfotos

![Bildschirmfotos von Pytition](./doc/screenshots/stop_doing_teams.webp)

## Dokumentation und Ressourcen

- Offizielle Website der App: <https://pytition.org>
- Offizielle Verwaltungsdokumentation: <https://pytition.readthedocs.io/en/latest/>
- Upstream App Repository: <https://github.com/pytition/Pytition>
- YunoHost-Shop: <https://apps.yunohost.org/app/pytition>
- Einen Fehler melden: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Entwicklerinformationen

Bitte senden Sie Ihren Pull-Request an den [`testing` branch](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Um den `testing` Branch auszuprobieren, gehen Sie bitte wie folgt vor:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
oder
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Weitere Informationen zur App-Paketierung:** <https://yunohost.org/packaging_apps>
