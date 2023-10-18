from webserver import keep_alive
import requests

channelID = 1086450980704489554
headers = {
    "authorization":
    "MTA5NjczMzEyNTEyOTgwMTgzMA.G8abGD.D9O9hY51qzKVQWl-ia82iax1OPERhP_lteyRT8"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
