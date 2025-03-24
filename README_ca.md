<!--
N.B.: Aquest README ha estat generat automàticament per <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
NO s'ha de modificar manualment.
-->

# Pytition per YunoHost

[![Nivell d'integració](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Estat de funcionament](https://apps.yunohost.org/badge/state/pytition)
![Estat de manteniment](https://apps.yunohost.org/badge/maintained/pytition)

[![Instal·la Pytition amb YunoHosth](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Llegeix aquest README en altres idiomes.](./ALL_README.md)*

> *Aquest paquet et permet instal·lar Pytition de forma ràpida i senzilla en un servidor YunoHost.*  
> *Si no tens YunoHost, consulta [la guia](https://yunohost.org/install) per saber com instal·lar-lo.*

## Visió general

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Versió inclosa:** 2.8~ynh4

**Demo:** <https://demo.pytition.org>

## Captures de pantalla

![Captures de pantalla de Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentació i recursos

- Lloc web oficial de l'aplicació: <https://pytition.org>
- Documentació oficial per l'administrador: <https://pytition.readthedocs.io/en/latest/>
- Repositori oficial del codi de l'aplicació: <https://github.com/pytition/Pytition>
- Botiga YunoHost: <https://apps.yunohost.org/app/pytition>
- Reportar un error: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Informació per a desenvolupadors

Envieu les pull request a la [branca `testing`](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Per provar la branca `testing`, procedir com descrit a continuació:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
o
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Més informació sobre l'empaquetatge d'aplicacions:** <https://yunohost.org/packaging_apps>
