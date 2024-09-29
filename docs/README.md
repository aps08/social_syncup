# social_syncup

![banner](banner.jpg)

Sync your message on discord, twitter(*write only*) and telegram. Currently supported for text messages and image.
<p align="left">
    <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="vscode">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
    <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
</p>

## How to use
Fork the project and follow the commands below for quick setup:

```
git clone https://github.com/{your_github_username}/social_syncup.git
cd social_syncup
python -m venv venv
venv\Scripts\activate (This is for windows, google and get your OS command for activating the virtual environment in python)
pip install -r requirements.txt
python setup.py
# Follow the steps in order to setup things
```
 - If working with Telegram you will be asked for telegram registered number. `social_syncup.session` and `social_syncup.session-journal` file will be generated which should not be deleted.
 - Setup the repository secret which will be printed at the end. (You can also store these in `.env` file to test locally)
 - Make project private if working with telegram, and don't forget to push `social_syncup.session` and `social_syncup.session-journal` to your repository. 

## How to get the secrets
1. Create write access secrets for twitter from [here](https://developer.twitter.com/).
2. Create discord bot with read write access from [here](https://discord.com/developers/applications).
3. Get telegram secrets from [here](https://my.telegram.org/auth).

## Secrets List

```
TELEGRAM_API_HASH               = <TELEGRAM_API_HASH>
TELEGRAM_API_ID                 = <TELEGRAM_API_ID>
TELEGRAM_GROUP_NAME             = <TELEGRAM_GROUP_NAME>
TWITTER_API_KEY                 = <TWITTER_API_KEY>
TWITTER_API_KEY_SECRET          = <TWITTER_API_KEY_SECRET>
TWITTER_BEARER_TOKEN            = <TWITTER_BEARER_TOKEN>
TWITTER_ACCESS_TOKEN            = <TWITTER_ACCESS_TOKEN>
TWITTER_ACCESS_TOKEN_SECRET     = <TWITTER_ACCESS_TOKEN_SECRET>
DISCORD_CHANNEL_ID              = <DISCORD_CHANNEL_ID>
DISCORD_SERVER_ID               = <DISCORD_SERVER_ID>
DISCORD_TOKEN                   = <DISCORD_TOKEN>
SOURCE                          = <SOURCE> (Where you will be writing. "telegram" or "discord")
TARGET                          = <TARGET> (Where this automation will writing. "telegram", "discord" or "X (formely Twitter)")
```

All these secrets need to be setup in the [respository secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions). So that the gihub actions can use these values to run the scripts.

## Quick Tips

- This repository will only on worklfow dispatch. In order to run for every hour, uncomment line number 5 and 6 given in `.github/workflows/perform-syncup.yml`.
- To customize the time when this repository runs change the cron notation give on line number 5 and 6 given in `.github/workflows/perform-syncup.yml`.
- Create your custom cron notaton [here](https://crontab.guru)
- Need customization is this code ? Reach out to me on [twitter](https://twitter.com/aps08__) and I might be able to help you.
- You only need secret from platforms you are using. Example: If working only with twiiter and discord, only those secrets are needed, and telegram can be ignored.

-----------------------------------------------------------------------------------------------------------------

<p align="center" style="text"><strong>If you liked something about this repository, do give it a 🌟. It will motivate me come up with more such project. You can reach out to me on my social media given below.</strong></p>
<p align="center">
 <a href="https://twitter.com/aps08__"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"></a>
 <a href="https://medium.com/@aps08"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"></a>
 <a href="https://www.linkedin.com/in/aps08"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
 <a href="https://github.com/aps08"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
 <a href="https://www.youtube.com/channel/UC8biJQnoqm1s2FZ8LK90baA"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
 <a href="mailto:anoopprsingh@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
 <a href="https://t.me/aps080"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"></a>
</p>