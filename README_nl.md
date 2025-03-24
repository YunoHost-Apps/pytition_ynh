<!--
NB: Deze README is automatisch gegenereerd door <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Hij mag NIET handmatig aangepast worden.
-->

# Pytition voor Yunohost

[![Integratieniveau](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Mate van functioneren](https://apps.yunohost.org/badge/state/pytition)
![Onderhoudsstatus](https://apps.yunohost.org/badge/maintained/pytition)

[![Pytition met Yunohost installeren](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Deze README in een andere taal lezen.](./ALL_README.md)*

> *Met dit pakket kun je Pytition snel en eenvoudig op een YunoHost-server installeren.*  
> *Als je nog geen YunoHost hebt, lees dan [de installatiehandleiding](https://yunohost.org/install), om te zien hoe je 'm installeert.*

## Overzicht

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Geleverde versie:** 2.8~ynh4

**Demo:** <https://demo.pytition.org>

## Schermafdrukken

![Schermafdrukken van Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentatie en bronnen

- Officiele website van de app: <https://pytition.org>
- Officiele beheerdersdocumentatie: <https://pytition.readthedocs.io/en/latest/>
- Upstream app codedepot: <https://github.com/pytition/Pytition>
- YunoHost-store: <https://apps.yunohost.org/app/pytition>
- Meld een bug: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Ontwikkelaarsinformatie

Stuur je pull request alsjeblieft naar de [`testing`-branch](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Om de `testing`-branch uit te proberen, ga als volgt te werk:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
of
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Verdere informatie over app-packaging:** <https://yunohost.org/packaging_apps>
