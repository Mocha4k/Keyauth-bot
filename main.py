import discord
import os
import requests
import json

from requests import *
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# MADE BY MOCHA 


# // The Bot's Status & Events. 

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name}")

  synced_commands = await bot.tree.sync()
  print(f"Synced {len(synced_commands)} slash commands")

  for cmd in synced_commands:
      print("These Commands have been synced: " + str(cmd))

  while True:
      await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.playing, name="Made by Mocha!"))



# // input your User ID & Seller key | I Added a Fake one so Please Replace it.

allowed_user_ids = 123456789012345678 # can include more than one
seller_key = "6afza2vphemopj82ffu65gt9sh8g1n4s"



# // Generate Command, SLASH COMMAND
# // the Duration value is in Days!
@bot.tree.command(name="generate", description="Generate a Product key")
@app_commands.choices(
    product=[
        app_commands.Choice(name="Product 1", value="Product 1"),
        app_commands.Choice(name="Product 2", value="Product 2"),
        app_commands.Choice(name="Product 3", value="Product 3"),
    ],
    duration=[
        app_commands.Choice(name="1 Day", value="1"),
        app_commands.Choice(name="3 Days", value="3"),
        app_commands.Choice(name="1 Week", value="7"),
        app_commands.Choice(name="1 Month", value="30"),
        app_commands.Choice(name="Lifetime", value="9999")
    ]
)
async def generate(interaction: discord.Interaction, product: str, duration: str, user: discord.Member):
        await interaction.response.defer()

        if interaction.user.id not in allowed_user_ids:
            await interaction.followup.send("You do not have access to generate keys.")
            return

        url = f"https://keyauth.win/api/seller/?sellerkey={seller_key}&type=add&expiry={duration}&mask=1-PRODUCT-***-***-***&level=1&amount=1&format=text"
        response = requests.get(url)
        key = response.text.upper()

        embed = discord.Embed(title="Mocha | Key Generated", description=f"Your Key for `{product}` is:\n ```{key}```\n > Duration: `{duration}` Days\n > User: `{user.mention}`",
        color=0x00ff00)
        embed.set_footer(text="Made by Mocha!")

        # Send's the Generated key to the user and sends it in chat!

        await interaction.followup.send(embed=embed)
        await user.send(embed=embed)
    

# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  

# RESET COMMAND 
@bot.tree.command(name="reset-key", description="HWID resets a key!")
async def reset_key(interaction: discord.Interaction, key: str):
    await interaction.response.defer()

    if interaction.user.id not in allowed_user_ids:
        await interaction.followup.send("Access Denied.")
        return

    url = f"https://keyauth.win/api/seller/?sellerkey={seller_key}&type=resetuser&user={key}"
    hwid_response = requests.get(url)
    hwid_message = hwid_response.json()["message"]

    reset_embed = discord.Embed(
       title="Mocha Auth | Key Reset",
       description="Key Reset Successful...\n Process exit with Code 200"
   )
    reset_embed.set_footer(text="Made by Mocha!")

    await interaction.followup.send(embed=reset_embed)




# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  

# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  

# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  

# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  

# MADE BY MOCHA # MADE BY MOCHA  # MADE BY MOCHA  # MADE BY MOCHA  



# // Delete key.
@bot.tree.command(name="delete-key", description="Delete's a key.")
async def delete_key(interaction: discord.Interaction, key: str):
  await interaction.response.defer()

  if interaction.user.id not in allowed_user_ids:
    await interaction.followup.send("Access Denied.")
    return

  url = f"https://keyauth.win/api/seller/?sellerkey={seller_key}&type=del&key={key}"
  response = requests.get(url)
  message = response.json()["message"]

  await interaction.followup.send(embed=discord.Embed(
    title="Mocha Auth | Key Deleted",
    description=f"Key Deleted Successful...\n Process exit with Code 200"
  ))




bot.run("TOKEN") # // replace with the actuall bot token.