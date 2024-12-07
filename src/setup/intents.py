import discord

def getIntents():
	intents = discord.Intents.default()
	
	intents.message_content = True
	intents.messages = True
	intents.guilds = True
	return (intents)
