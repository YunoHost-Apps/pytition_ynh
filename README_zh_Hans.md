<!--
注意：此 README 由 <https://github.com/YunoHost/apps/tree/master/tools/readme_generator> 自动生成
请勿手动编辑。
-->

# YunoHost 的 Pytition

[![集成程度](https://dash.yunohost.org/integration/pytition.svg)](https://dash.yunohost.org/appci/app/pytition) ![工作状态](https://ci-apps.yunohost.org/ci/badges/pytition.status.svg) ![维护状态](https://ci-apps.yunohost.org/ci/badges/pytition.maintain.svg)

[![使用 YunoHost 安装 Pytition](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=pytition)

*[阅读此 README 的其它语言版本。](./ALL_README.md)*

> *通过此软件包，您可以在 YunoHost 服务器上快速、简单地安装 Pytition。*  
> *如果您还没有 YunoHost，请参阅[指南](https://yunohost.org/install)了解如何安装它。*

## 概况

Pytition is an application for privacy-friendly online petitions you can host on your own server.

### Features

- Host petitions without compromising the privacy of your signatories.
- No tracking, ever: CSS, JS and all resources are self-hosted. Pytition does not use CDN.
- Responsive UI: works well on phones/tablets/laptops/desktops.
- Multi-lingual UI with i18n: English, French, Italian, Occitan, Spanish.
- You can pre-visualize petitions before publishing them.
- Easy to use: petition content is typed-in via TinyMCE editors (like WordPress).
- You can export signatures in CSV format.


**分发版本：** 2.8~ynh3

**演示：** <https://demo.pytition.org>

## 截图

![Pytition 的截图](./doc/screenshots/stop_doing_teams.webp)

## 文档与资源

- 官方应用网站： <https://pytition.org>
- 官方管理文档： <https://pytition.readthedocs.io/en/latest/>
- 上游应用代码库： <https://github.com/pytition/Pytition>
- YunoHost 商店： <https://apps.yunohost.org/app/pytition>
- 报告 bug： <https://github.com/YunoHost-Apps/pytition_ynh/issues>

## 开发者信息

请向 [`testing` 分支](https://github.com/YunoHost-Apps/pytition_ynh/tree/testing) 发送拉取请求。

如要尝试 `testing` 分支，请这样操作：

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
或
sudo yunohost app upgrade pytition -u https://github.com/YunoHost-Apps/pytition_ynh/tree/testing --debug
```

**有关应用打包的更多信息：** <https://yunohost.org/packaging_apps>
