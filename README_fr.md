<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Pytition pour YunoHost

[![Niveau d’intégration](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Statut du fonctionnement](https://apps.yunohost.org/badge/state/pytition)
![Statut de maintenance](https://apps.yunohost.org/badge/maintained/pytition)

[![Installer Pytition avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Pytition rapidement et simplement sur un serveur YunoHost.*  
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

Pytition permet d'héberger des pétitions respectueuses de la vie privée sur votre propre serveur.

### Features

- Hébergez des pétitions sans compromettre l'identité de vos signataires
- Pas de tracking : CSS, JS et autres ressources sont auto-hébergées. Pas d'usage de CDN.
- Interface réactive : fonctione sur smartphones et tablettes autant que sur ordinateur.
- Interface traduite : anglais, français, italien, occitan, espagnol.
- Vous pouvez prévisualiser les pétitions avant publication.
- Simple à utiliser grâce à des éditeurs TinyMCE (comme Wordpress)
- Vous pouvez exporter les signatures via CSV.


**Version incluse :** 2.8~ynh4

**Démo :** <https://demo.pytition.org>

## Captures d’écran

![Capture d’écran de Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentations et ressources

- Site officiel de l’app : <https://pytition.org>
- Documentation officielle de l’admin : <https://pytition.readthedocs.io/en/latest/>
- Dépôt de code officiel de l’app : <https://github.com/pytition/Pytition>
- YunoHost Store : <https://apps.yunohost.org/app/pytition>
- Signaler un bug : <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
ou
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
