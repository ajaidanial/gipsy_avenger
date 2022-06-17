# Setup Slack Tokens

The Slack `CHANNEL_ID` and `BOT_ACCESS_TOKEN` are required to notify about the upgrade/downgrade
events on slack. Please follow the below steps to get the necessary tokens. If the tokens
are not configured, no notifications will be sent.

## Getting `CHANNEL_ID`

The provided channel with the `CHANNEL_ID` will be used for notifications. Make sure to
create a separate channel if needed.

1. Open your Slack app, click on the channel that you wish to notify.
2. Go to `Get Channel Details`, go to the `About` section.
3. Scroll to the bottom and you will see the `Channel ID`.

You can also follow this [link](https://help.socialintents.com/article/148-how-to-find-your-slack-team-id-and-slack-channel-id).

## Getting `BOT_ACCESS_TOKEN`

A bot is necessary to send notifications, follow to below steps to configure the bot.

1. Go to [Your Apps](https://api.slack.com/apps) section.
2. Click on `Create New App`, select `From scratch` option.
3. Provide the necessary name and which workspace you want to add it to(your Slack workspace).
4. On the created app's manage page, on the left sidebar under `Features` click on `OAuth & Permissions`.
5. Scroll to the `Scopes` section, and click on `Add an OAuth Scope`.
6. Make sure to select the following permissions: `chat:write` & `chat:write.public`.
7. Once done, go to the `Basic Information` under the `Settings` section.
8. Click on `Install your app` and make sure to allow access to your workspace.
9. Once done, go back to the `OAuth & Permissions` section.
10. Go to the `OAuth Tokens for Your Workspace` and copy the provided `BOT_ACCESS_TOKEN`.

References: https://api.slack.com/authentication/basics
