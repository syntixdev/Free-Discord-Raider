import discord
import time
import random
import string
from discord.utils import get
from discord.ext import commands
import asyncio
import requests
from requests import post

inv=input("what is the invite link (just the string of letters or enter nothing if they are already in): ")

link = "https://discord.com/api/v6/invites/" + inv.split("/")[-1]
joined = 0
failed = 0
with open("tokens.txt", "r") as f:
    tokens = f.read().splitlines()
    for token in tokens:
        headers = {"Content-Type": "application/json", 
                   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                   "Authorization" : token}

        response = post(link, headers=headers).status_code
        if response > 199 and response < 300:
            joined += 1

        else:
            failed += 1

    print("Accounts that joined: "+str(joined))
    print("Accounts that could not join: "+str(failed))
    
print("-----")
    
messagecount=input("How many messages should each user send (must be integer): ")

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

time.sleep(2)
messagesend=input("Type what you want the bots to spam here: ")

with open("tokens.txt", "r") as f:
    tokens = f.read().splitlines()

class multibot(commands.Cog):
    def __init__(self, client):
        self.client=client
    
    @commands.command()
    async def r(self,ctx):
        x=0
        for x in range(0,int(messagecount)):
            asyncio.sleep(0.7)
            print("Sending message "+random.choice(string.ascii_letters))
            try:
                await ctx.send(messagesend)
            except:
                print("Message error")
                pass
            x=x+1
            
loop = asyncio.get_event_loop()
for i in range(len(tokens)):
    
    client = commands.Bot(command_prefix=".",fetch_offline_members=False,self_bot=False)
    client.add_cog(multibot(client))
    loop.create_task(client.start(tokens[i], bot=False))

loop.run_forever()