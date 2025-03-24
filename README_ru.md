<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# Pytition для YunoHost

[![Уровень интеграции](https://apps.yunohost.org/badge/integration/pytition)](https://ci-apps.yunohost.org/ci/apps/pytition/)
![Состояние работы](https://apps.yunohost.org/badge/state/pytition)
![Состояние сопровождения](https://apps.yunohost.org/badge/maintained/pytition)

[![Установите Pytition с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить Pytition быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**Поставляемая версия:** 2.8~ynh4

**Демо-версия:** <https://demo.pytition.org>

## Снимки экрана

![Снимок экрана Pytition](./doc/screenshots/stop_doing_teams.webp)

## Документация и ресурсы

- Официальный веб-сайт приложения: <https://pytition.org>
- Официальная документация администратора: <https://pytition.readthedocs.io/en/latest/>
- Репозиторий кода главной ветки приложения: <https://github.com/pytition/Pytition>
- Магазин YunoHost: <https://apps.yunohost.org/app/pytition>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
или
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
