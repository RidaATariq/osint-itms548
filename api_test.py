import twitch
import xconfig

client = twitch.TwitchHelix(client_id=xconfig.client_id,
                            client_secret=xconfig.client_secret)

client.get_oauth()
print(client.get_streams())
