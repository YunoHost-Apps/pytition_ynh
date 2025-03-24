<!--
Este archivo README esta generado automaticamente<https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
No se debe editar a mano.
-->

# Pytition para YunoHost

[![Nivel de integración](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Estado funcional](https://apps.yunohost.org/badge/state/pytition)
![Estado En Mantención](https://apps.yunohost.org/badge/maintained/pytition)

[![Instalar Pytition con Yunhost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Leer este README en otros idiomas.](./ALL_README.md)*

> *Este paquete le permite instalarPytition rapidamente y simplement en un servidor YunoHost.*  
> *Si no tiene YunoHost, visita [the guide](https://yunohost.org/install) para aprender como instalarla.*

## Descripción general

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Versión actual:** 2.8~ynh4

**Demo:** <https://demo.pytition.org>

## Capturas

![Captura de Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentaciones y recursos

- Sitio web oficial: <https://pytition.org>
- Documentación administrador oficial: <https://pytition.readthedocs.io/en/latest/>
- Repositorio del código fuente oficial de la aplicación : <https://github.com/pytition/Pytition>
- Catálogo YunoHost: <https://apps.yunohost.org/app/pytition>
- Reportar un error: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Información para desarrolladores

Por favor enviar sus correcciones a la [rama `testing`](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Para probar la rama `testing`, sigue asÍ:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
o
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Mas informaciones sobre el empaquetado de aplicaciones:** <https://yunohost.org/packaging_apps>
