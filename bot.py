import discord, json, requests, datetime, random
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = '$')
client.remove_command('help')
member_id = (461367534348795904)

status = ['Ark Bot for trash ark tribe']

@client.event
async def on_ready():
  print('ark bot is Online')



@client.command(aliases=['bob'])
async def bobtest(ctx, *, member):
  responses = ['1%',
              '2%',
              '3%',
              '4%',
              '5%',
              '6%',
              '7%',
              '8%',
              '9%',
              '10%',
              '11%',
              '12%',
              '13%',
              '14%',
              '15%',
              '16%',
              '17%',
              '18%',
              '19%',
              '20%',
              '21%',
              '22%',
              '23%',
              '24%',
              '25%',
              '26%',
              '27%',
              '28%',
              '29%',
              '30%',
              '31%',
              '32%',
              '33%',
              '34%',
              '35%',
              '36%',
              '37%',
              '38%',
              '39%',
              '40%',
              '41%',
              '42%',
              '43%',
              '44%',
              '45%',
              '46%',
              '47%',
              '48%',
              '49%',
              '50%',
              '51%',
              '52%',
              '53%',
              '54%',
              '55%',
              '56%',
              '57%',
              '58%',
              '59%',
              '60%',
              '61%',
              '62%',
              '63%',
              '64%',
              '65%',
              '66%',
              '67%',
              '68%',
              '69%',
              '80%',
              '81%',
              '82%',
              '83%',
              '84%',
              '85%',
              '86%',
              '87%',
              '88%',
              '89%',
              '90%',
              '91%',
              '92%',
              '93%',
              '94%',
              '95%',
              '96%',
              '97%',
              '98%',
              '99%',
              '100%',
              '10000%']
  await ctx.send(f'{member} is {random.choice(responses)} BOB')
  channel = client.get_channel(862041658760364043)
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command BobTest on {member}')
  embed.set_footer(text=f'made by Envx | Ark Bot Logs')
  await channel.send(embed=embed)

@client.command()
async def help(ctx):
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Commands', description='**Ark Bot Commands**\n$bobtest <user>\n $geo <host>\n $userinfo <user>\n $bot <id>\n $bothelp\n $ping\n $lockdown\n $unlock\n $idlookup\n $embed\n\n **Bobs Gone Wild Rules**\n $mod\n $names\n $server\n $report\n $punish\n $wipe\n $meshing\n $bases\n $spam\n $tames\n $items')
  embed.set_footer(text=f'made by Envx | Command used by {ctx.message.author} | Ark bot')
  await ctx.send(embed=embed)
  channel = client.get_channel(862041658760364043)
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot', description=f'{ctx.message.author} has used the command Help')
  embed.set_footer(text=f'made by Envx | Command used by {ctx.message.author}')
  await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Purge and deleted {amount} of messages')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot', description=f'{ctx.message.author} deleted {amount} Messages')
    embed.set_footer(text=f'made by Envx | Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
    print (f'{amount} messages cleared')


  
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**U Do Not Have Permission To Use This Command**')
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Color.green(), title='•Error', description='Forgot the amount of messages to be cleared')
        embed.set_footer(text='Made by Envx | Ark Bot Error')
        await ctx.send(embed=embed)


@client.command(aliases=['ms'])
async def ping(ctx):
    em = discord.Embed(title="Ping", description=f"The bot's ping is currently `{round(client.latency * 1000)}ms`", color=discord.Colour.green())
    await ctx.send(embed=em)
    print('Ping/ms command has executed')
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Ping')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def lockdown(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  await ctx.send( ctx.channel.mention + ' **is now in lockdown**')
  channel = client.get_channel(862041658760364043)
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Lockdown')
  embed.set_footer(text=f'made by Envx | Ark Bot Logs')
  await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def unlock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  await ctx.send( ctx.channel.mention + ' **has been unlocked**')
  channel = client.get_channel(862041658760364043)
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Unlock')
  embed.set_footer(text=f'made by Envx | Ark Bot Logs')
  await channel.send(embed=embed)

@client.command()
async def userinfo(ctx, user: discord.User = None):

    if user is None:
        await ctx.send('**@ a user u fucking idiot**')
        return

    embed = discord.Embed(timestamp=ctx.message.created_at, description = f'Here is info about this nigga {user.name}', colour = discord.Colour.green())

    embed.add_field(name = user, value = f' - User\'s name: {user}\n- User\'s ID: {user.id}\n- User\'s discrim: {user.discriminator}\n- User\'s is a bot: {user.bot}\n- User\'s Display Name: {user.display_name}\n- User\'s Top Role: {user.top_role.mention}')
    embed.set_footer(text=f"Discord bot made by Envx")
    await ctx.send(embed=embed)
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command UserInfo')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)

@client.command()
async def geo(ctx, host):
    start = datetime.datetime.now()
    r = requests.get(f"http://ipwhois.app/json/{host}")
    geo = r.json()
    embed = discord.Embed(
    colour=discord.Colour.green()
    )
    embed.set_author(name='Made bye Envx')
    embed.set_footer(text='Discord bot made by Envx')
    embed.add_field(name='IP', value= geo['ip'], inline=True)
    embed.add_field(name='Type', value= geo['type'], inline=True)
    embed.add_field(name='Continent', value= geo['continent'],  inline=True)
    embed.add_field(name='Country', value= geo['country'],  inline=True)
    embed.add_field(name='Region', value= geo['region'],  inline=True)
    embed.add_field(name='City', value= geo['city'], inline=True)
    embed.add_field(name='ISP', value= geo['isp'], inline=True)
    embed.add_field(name='Org', value= geo['org'], inline=True)
    embed.add_field(name='ASN', value= geo['asn'], inline=True)
    embed.add_field(name='Timezone', value= geo['timezone_name'], inline=True)
    embed.add_field(name='Latitute', value= geo['latitude'], inline=True)
    embed.add_field(name='Longitude', value= geo['longitude'], inline=True)
    await ctx.send(embed=embed)
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Geo on IP: {host}')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)


@geo.error
async def geo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=discord.Color.green(), title='•Error', description='Forgot the IP Address')
        embed.set_footer(text='Made by Envx | Ark Bot Error')
        await ctx.send(embed=embed)


@client.command()
async def idlookup(ctx):
    await ctx.send(f'https://discord.id/')
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command idlookup')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)


@client.command()
async def bot(ctx, id):
  await ctx.send(f'```https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot```')
  channel = client.get_channel(862041658760364043)
  embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Bot Lookup on {id}')
  embed.set_footer(text=f'made by Envx | Ark Bot Logs')
  await channel.send(embed=embed)


@client.command()
async def bothelp(ctx):
    embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot')
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='How to use bot command', value='to use the command bot turn on devolper mode in discord settings go to a Discord Bot, right click, then press copy the ID then use the command _bot ID', inline=True)
    await ctx.send(embed=embed)
    channel = client.get_channel(862041658760364043)
    embed = discord.Embed(colour=discord.Color.green(), title='•Ark Bot | Logs', description=f'{ctx.author.display_name} has used the command Bot Help')
    embed.set_footer(text=f'made by Envx | Ark Bot Logs')
    await channel.send(embed=embed)

@client.command()
async def wipe(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot', description='Wipe is in Augest no date yet')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild')
  await ctx.send(embed=embed)


@client.command()
async def names(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Tribe/Player/Dino Names', description='-Human\n -Bob/Generic Common\n -Numbers\n -Emoji\n -Barcode\n -IlIlIlIl,llllllll,IIIIIIII\n __This is not allowed as a character name ever.__\n **1**- Not suggest illegal activity such as aimbot, mesh, or doss.\n **2**- Not be racist, homophobic or discriminatory.\n **3**- Not use slashes. If it has to use a slash it is probably wrong.')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)


@client.command()
async def mod(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Moderation', description='**1**- We do NOT moderate Xbox live parties or messages.\n **2**- We will NOT get involed in insiding/blue tagging or trading/scamming issues. On Public Maps\n **3**- Insiding on a Private Map is a bannable offence\n **4**- Do NOT buy/sell dinos for money other than from the admin shop on discord.\n **5**- If you are banned from one map within the cluster, you are banned from all of them\n **6**- If you are caught on another map on an alt or otherwise you will be permanently banned and not subject to an appeal.\n **7**- Use of external mods on PC or Xbox such as aimbot, autoclicker etc are not permitted\n ```Warnings are a courtesy, not a requirement. Do not break the rules expecting to get by with a warning```')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)

@client.command()
async def server(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Server Rules', description='```Meshing is not allowed.```\n Intentional Mesh such of any structure to prevent raiding is punishable by structure wipe and up to a ban. This means if an admin is required to remove it chances are it was intentional. Listed below are simple examples but not all:\n -behometh gates in pearl\n -foundations under multiple layers of mesh\n -pillars behind invisible walls\n Bases in the mesh are not allowed and will result in a structure wipe up to a tribe ban.\n\n If the dino cannot fit by walking it there, it is not permitted. Blocking entrances with tames does not fall under this rule as long as they do not overlap (i.e. stand side by side)\n __Mesh hitting such as a giga head through a wall, theri smacking at a crouch point, reaper tail spin through the wall, etc is not allowed__\n If you base requires you to knock yourself out, be dragged in, teleport, use a bed, use a tame or otherwise having to glitch inside, this is meshing and will result in a tribe wipe and ban. Your base needs to be able to walked/crouched/crawled into naturally without aid.\n\n Mesh defenses are allowed but must only be made of turrets, platforms and foundations.\n -Meshed turrets can not shoot from the mesh.\n -Clean up any structures/dinos used for mesh defenses\n immediately.\n __Caging is NOT allowed BUT You CAN cage illegal names indefinitely__\n\n -Cannon Raiding is NOT allowed.\n -Raft Raiding is NOT allowed.\n Any infraction of the above rules can result in anything from a structure wipe, individual ban up to a tribe ban.\n ```Rules subject to change at any time```')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)

@client.command()
async def report(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Reporting', description='If you need to report any of the above please use **admin support**, provide us only the information requested, you will need to include the below evidence\n\n -Threats to Doss or Mesh: **In game screen shots of global**\n\n -Aimbot/Meshing/Mesh hits: **Clip it clearly, without a clip we cannot assist.**\n\n -Meshed structures and/or Tames: **Pictures and GPS Coords GPS Coords are needed in every situation, please keep these handy**\n\n -Illegal language/names in general: **Clear pictures of the general chat**\n\n -Private messages, guilded servers, discord messaged, etc are all not take as sufficient evidence.')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)

@client.command()
async def punish(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Punishments', description='-Player/Tribe Related = Ban\n -Structure Related = Structure Wipe\n -Dino Related = Dino Wipe\n ```Warnings are a courtesy, not a requirement. Do not break the rules expecting to get by with a warning```')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)

@client.command()
async def meshing(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Meshing', description="**1** -Meshing is not allowed and will result in a tribe wipe and ban.\n\n **2** -Mesh biting/hitting is prohibited and will result in a dino wipe This also includes crouch points. **If the dino does not fit, it is not allowed E.G Theri at Pearl Cave, Reaper at Bear Cave**\n\n **3** -If your base requires you to knock yourself out and be dragged in, teleport using a bed, or otherwise having to glitch to get inside, this is meshing and will result in a tribe wipe and ban.\n\n **4** -Mesh defenses are allowed but must only be made of turrets, platforms and foundations. Meshed turrets can not shoot from the mesh. Clean up any structures/dinos used for mesh defenses immediately.\n\n**5** -Meshing on purpose will result in a structure wipe up to a ban.\n**Reporting**\nIf you need to report any of the above please use **admin-support** include the below evidence\n -Threats to Mesh: In game screen shots of global\n -Meshing/Mesh hits: Clip it clearly, without a clip we cannot assist.\n -Base has been meshed or think it has been: Tribe log all the way back to first structure, photos the more the better\n -Mesh Defense Assistance: If you need help, make a mesh ticket using the support bot. If you can do it yourself, you are best off doing it yourself.")
  embed.set_footer(text=f"made by Envx | Bobs Gone Wild | command used by {ctx.message.author}")
  await ctx.send(embed=embed)

@client.command()
async def bases(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Bases', description='Players are only allowed two bases per map. This does not include fobs. A fob should be left with basic items such as\n -Beds\n -Teleporter\n -Turrets\n This does not mean you can not have other items there, but it should be limited to the basics outside a raid\n\n ```If the base spot requires you to knock yourself out, log out, be dragged in, use a tame, use a bed or any other type of glitch to get in, it is not allowed and will be wiped with no warning.```\n\n -If the rat hole/ base spot allows you to enter the mesh by any means it is illegal and you will be wiped with no warning.\n\n A main base in the open can be a decent size, an area of around 120 foundations. at the edge of that is where the spam will start.\n -Spam is not to go past 60 foundations from the edge of the base (**outside of a raid**).\n A main base in a cave can own the entire cave (i.e Island Ice Cave).\n -Spam is not to go past 60 foundations from the entrance of the cave (**outside of a raid**).\n Turret towers must be built within this spam area (**outside of a raid**)\n -Towers can include vault dropped walls.\n -Do not overlap vaults.\n\n We measure with cliff/ tree plats as they are 10 foundations end to end. So if you are unsure of how far out your spam is use this for your own measurement\n If bases violate these rules we determine the level of rule break and we clear accordingly. This could mean we use redgun, AOE command, or a complete base wipe.\n\n Surface, Underworld or Ab entrances can not be blocked or built in. This will result in a area wipe up to a complete structure wipe.\n **DO NOT BUILD ON SPAWN POINTS**\n **DO NOT BUILD ON OBS**\n -Green ob on Val is the only exception\n -Do not build fobs on the pvp zones to preserve the foot pvp and tame pvp integrity. This can lead to an area wipe up to a structure wipe depending on severity\n Spam is a major part of defense but not all spam types are allowed. Accepted spam styles\n -Square/ Triangle Foundations (**checkerboard, cannot be carpeted**)\n -Turrets\n -Gates in a straight line\n -Spikes and Billboards are allowed on the Perimeter but not throughout the 60 foundation spam\n -Double doorframes can be used as C-spin protection in crouch spaces\n -Sink foundations (not under mesh) for basi protection near crouch entrances\n ```Remember to keep it clean like you have OCD.```\n**Acceptable Spam**\n This acceptable spam photo shows accepted oil cave spam length at 60 down the platform.')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  embed.set_image(url='https://images-ext-1.discordapp.net/external/RqR6FCf1-ahuVa2mOx8ppeXCSvORAQcLNUv6u6RHfvY/https/i.imgur.com/V0uXFbR.png?width=931&height=645')
  await ctx.send(embed=embed)

@client.command()
async def spam(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Illegal Spam', description='Illegal spam is anything not listed above as allowed. Listed below are some examples of what not to do\n -Vaults being spammed throughout the 60 foundations\n -Vaults being spammed at cave entrances or crouch points\n - Turrets being spammed in one area to cap the turret amount and stop the enemy tribe from placing any turrets\n -Transmitters being spammed\n -Cliff Plat Spam\n -Pulsing generators \n -Pipes or wires being spammed\n -Criss-cross gates\n -Fence foundations\n -Overlapping bubble spam\n These are all just examples and do not include every instance of what could happen. Use good judgement or ask an admin for clarity.\n\n **unAcceptable Spam**\n Clear Examples of spam that may warrant a structure wipe or no warning admin cleanup')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  embed.set_image(url='https://images-ext-1.discordapp.net/external/nt3JUSmfj47SEMBmo0DSzim-rzhXqOwOlYShpEsUXBo/https/i.imgur.com/nlB2f7e.jpg?width=808&height=646')
  await ctx.send(embed=embed)


@client.command()
async def tames(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Illegal tames', description='-AB Beelzebufo\n -AB Carno\n -AB Dodo\n -AB Scorpian\n -ANKY (**including variants**)\n -ARANEO (**including variants**)\n -Bronto\n -Dilophosaur (**including variants**)\n -Doedicurus (**including variants**)\n -Gallimimus\n -Hyaenodon\n -Ichthyornis\n -Ichthyosaurus\n -Iguanodon (**including variants**)\n -LLystrosaurus (**including variants**)\n -Manta\n -Meganeura\n -Oviraptor\n -Pegomastax\n -Procoptodon (**aka Kangaroo**)\n -Terror Bird\n -Titanosaur')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)

@client.command()
async def items(ctx):
  embed = discord.Embed(colour=discord.Colour.green(), title='•Ark Bot | Illegal Items', description='-Beer/Beer Barrel\n -Saddles for Illegal/Untamable Creatures\n -Climbing Pick\n -Cluster Grenades\n -Flare Gun\n -Glow Stick\n -Handcuffs\n -Metal Fence Support\n -Metal Ocean Platform\n -Motorboat\n -TEK ATV\n -TEK Light\n -TEK Skiff\n -Waterskin\n -Wood Elevator\n -Wood Ocean Platform\n -Cage\n -Chair\n -Wood Fence Foundations/Supports\n -Rafts\n -Ziplines')
  embed.set_footer(text=f'made by Envx | Bobs Gone Wild | command used by {ctx.message.author}')
  await ctx.send(embed=embed)


@client.command()
async def suggestion(ctx, description):
    await ctx.message.delete()
    embed=discord.Embed(colour=discord.Colour.green(), title=f'Suggestion', description=f'{description}')
    await ctx.send(embed=embed)

@client.command()
async def embed(ctx, title, *, description):
    await ctx.message.delete()
    embed=discord.Embed(colour=discord.Colour.green(), title=f'{title}', description=f'{description}')
    await ctx.send(embed=embed)



client.run('ODYxODM3MTcyNzU4NTQ0Mzk0.YOPmag.ayhgCUUyjG0rUNBXj2yu19OwHBg')
