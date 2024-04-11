<!--
N.B.: This README was automatically generated by <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
It shall NOT be edited by hand.
-->

# Pytition for YunoHost

[![Integration level](https://dash.yunohost.org/integration/pytition.svg)](https://dash.yunohost.org/appci/app/pytition) ![Working status](https://ci-apps.yunohost.org/ci/badges/pytition.status.svg) ![Maintenance status](https://ci-apps.yunohost.org/ci/badges/pytition.maintain.svg)

[![Install Pytition with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Read this README in other languages.](./ALL_README.md)*

> *This package allows you to install Pytition quickly and simply on a YunoHost server.*  
> *If you don't have YunoHost, please consult [the guide](https://yunohost.org/install) to learn how to install it.*

## Overview

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Shipped version:** 2.8~ynh2

**Demo:** <https://demo.pytition.org>

## Screenshots

![Screenshot of Pytition](./doc/screenshots/stop_doing_teams.webp)

## Documentation and resources

- Official app website: <https://pytition.org>
- Official admin documentation: <https://pytition.readthedocs.io/en/latest/>
- Upstream app code repository: <https://github.com/pytition/Pytition>
- YunoHost Store: <https://apps.yunohost.org/app/pytition>
- Report a bug: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Developer info

Please send your pull request to the [`testing` branch](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

To try the `testing` branch, please proceed like that:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
or
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**More info regarding app packaging:** <https://yunohost.org/packaging_apps>
