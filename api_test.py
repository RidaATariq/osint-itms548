import twitch
import config

client = twitch.TwitchHelix(
    client_id=config.client_id,
    client_secret=config.client_secret,
    scopes=[twitch.constants.OAUTH_SCOPE_ANALYTICS_READ_EXTENSIONS])

client.get_oauth()
print(client.get_streams())
