import twitch
import config

client = twitch.TwitchHelix(client_id=config.client_id,
                            client_secret=config.client_secret)

client.get_oauth()
print(client.get_streams())
