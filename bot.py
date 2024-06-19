import asyncio
import json
import aiohttp
from datetime import datetime
from chips import Chips
from consts import Consts
from netnavi import NetNavi
from element import Element
import interactions

guild_ids = [642081591371497472]

netNavi = NetNavi()

client = interactions.Client(token=Consts.TOKEN)

interactions.const.CLIENT_FEATURE_FLAGS["FOLLOWUP_INTERACTIONS_FOR_IMAGES"] = True

async def BuildEmbed(ctx, val, version):
    e = interactions.Embed()
    e.title= val['Name']
    e.description=val['Description']
    elementEmoji = Element.GetElementEmoji(val['Element'])
    if(val['Image_URL'] is not None):
        e.set_thumbnail(url=val['Image_URL'])
    e.color = interactions.BrandColors.BLURPLE 
    e.add_field(name="Damage", value=val['Damage'], inline=True)
    if(val['Element'] != "-"):
        e.add_field(name="Element", value=elementEmoji, inline=True)
    if(version == Consts.BN1):
        e.set_footer(text= f"Battle Network 1 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN2):
        if(val['Memory'] is not None):
            e.add_field(name="Memory", value=f"{val['Memory']} MB", inline=True)
        e.set_footer(text= f"Battle Network 2 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN3):
        if(val['Memory'] is not None):
            e.add_field(name="Memory", value=f"{val['Memory']} MB", inline=True)
        e.set_footer(text= f"Battle Network 3 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN4):
        if(val['Memory'] is not None):
            e.add_field(name="Memory", value=f"{val['Memory']} MB", inline=True)
        e.set_footer(text= f"Battle Network 4 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN5):
        if(val['Memory'] is not None):
            e.add_field(name="Memory", value=f"{val['Memory']} MB", inline=True)
        e.set_footer(text= f"Battle Network 5 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN6):
        if(val['Memory'] is not None):
            e.add_field(name="Memory", value=f"{val['Memory']} MB", inline=True)
        e.set_footer(text= f"Battle Network 6 - {val['Category']} Chip ({val['ID']})",icon_url=Consts.ICON_URL)   
    if(val['Category'] == "Program Advance"):
        e.add_field(name="Combinations", value=val['Codes'])
    else:
        e.add_field(name="Codes", value=val['Codes'])
    if(val['Locations'] is not None):
        e.add_field(name="Locations", value=val['Locations'])

    if(version != Consts.BN1):
        if(len(val['CommandCodes']) > 0):          
            cmdCode = ""  
            for code in val['CommandCodes']:
                if(code['Effect'] is not None):
                    cmdCode += f"{code['Command']} = {code['Effect']}\n"
                else:
                    cmdCode += f"{code['Command']}\n"
            e.add_field(name="Command Codes", value=cmdCode)
    return e

async def BuildCrustEmbed(ctx, val, version):
    e = interactions.Embed()
    e.title= val['Part']
    e.description=val['Effect']
    e.color = interactions.BrandColors.BLURPLE
    e.add_field(name="Bug", value=val['Bug'])
    if(val['Compression'] != "---" and val['Compression'] is not None):
        e.add_field(name="Compression", value=val['Compression'])
    if(version == Consts.BN3):
        e.set_footer(text= "Battle Network 3",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN4):
        e.set_footer(text= "Battle Network 4",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN5):
        e.set_footer(text= "Battle Network 5",icon_url=Consts.ICON_URL)   
    if(version == Consts.BN6):
        e.set_footer(text= "Battle Network 6",icon_url=Consts.ICON_URL)         
    if(val['Location'] is not None):
        e.add_field(name="Locations", value=val['Location'])
    return e

def GetChipsForVersion(version):
    if(version.lower() == Consts.BN1.lower()):
        return netNavi.chipDict[Consts.BN1]
    elif(version.lower() == Consts.BN2.lower()):
        return netNavi.chipDict[Consts.BN2]
    elif(version.lower() == Consts.BN3.lower()):
        return netNavi.chipDict[Consts.BN3]
    elif(version.lower() == Consts.BN4.lower()):
        return netNavi.chipDict[Consts.BN4]
    elif(version.lower() == Consts.BN5.lower()):
        return netNavi.chipDict[Consts.BN5]
    elif(version.lower() == Consts.BN6.lower()):
        return netNavi.chipDict[Consts.BN6]
    
    return netNavi.chipDict[Consts.BN1]

def GetCrustForVersion(version):
    if(version.lower() == Consts.BN3.lower()):
        return netNavi.crustDict[Consts.BN3]
    elif(version.lower() == Consts.BN4.lower()):
        return netNavi.crustDict[Consts.BN4]
    elif(version.lower() == Consts.BN5.lower()):
        return netNavi.crustDict[Consts.BN5]
    elif(version.lower() == Consts.BN6.lower()):
        return netNavi.crustDict[Consts.BN6]
    
    return netNavi.crustDict[Consts.BN3]

def GetPAForVersion(version):
    if(version.lower() == Consts.BN1.lower()):
        return netNavi.paDict[Consts.BN1]
    elif(version.lower() == Consts.BN2.lower()):
        return netNavi.paDict[Consts.BN2]
    elif(version.lower() == Consts.BN3.lower()):
        return netNavi.paDict[Consts.BN3]
    elif(version.lower() == Consts.BN4.lower()):
        return netNavi.paDict[Consts.BN4]
    elif(version.lower() == Consts.BN5.lower()):
        return netNavi.paDict[Consts.BN5]
    elif(version.lower() == Consts.BN6.lower()):
        return netNavi.paDict[Consts.BN6]
    
    return netNavi.paDict[Consts.BN1]

@interactions.slash_command(name="info",
            description="Get information about the bot")
async def PrintCommands(ctx):
    e = interactions.Embed()
    e.color = interactions.BrandColors.GREEN
    e.title = "Information!"
    e.description = "Thanks for using NetNavi.exe! If you'd like to support what I do please follow me on [Patreon](https://www.patreon.com/bePatron?u=34112337).\nHuge shoutout to the work done by the N1GP and The Rockman.exe Zone team. Check out [n1gp](https://wiki.n1gp.net/) and [Rockman.exe](https://www.therockmanexezone.com/wiki/The_Rockman_EXE_Zone_Wiki) for more detailed MMBN information!"
    e.set_author(name="NetNavi.exe",icon_url=Consts.LOGO_ADDRESS)
    e.set_thumbnail(url=Consts.ICON_URL)
    
    commands = "• `/chip_details`: Display details about a chip!\n"
    commands += "• `/navicust_part_details`: Display details about a NaviCust part!\n"  
    commands += "• `/program_advance_details`: Display details about a Program Advance!\n"
    
    e.add_field(name="Commands", value=commands, inline=False)
    e.set_footer(text="Created by Dillonzer and Powered by N1GP Data / The Rockman.exe Zone")

    await ctx.send(embeds = e, ephemeral=True)

@interactions.slash_command(name='chip_details',
        description="Shows the details about the chip.",
        options=[    
            interactions.SlashCommandOption(
                name="game_version",
                description="What game version",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                    interactions.SlashCommandChoice(
                        name="Battle Network One",
                        value=Consts.BN1
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Two",
                        value=Consts.BN2
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Three",
                        value=Consts.BN3
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Four",
                        value=Consts.BN4
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Five",
                        value=Consts.BN5
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Six",
                        value=Consts.BN6
                    )]
            ),
            interactions.SlashCommandOption(
                name="name",
                description="Name of the chip",
                type=interactions.OptionType.STRING,
                required=True,
                autocomplete=True
            )]
        )
async def GetSpecificChip(ctx, game_version, name):
    await ctx.defer()
    ALLCHIPS = GetChipsForVersion(game_version)  
    foundChip = False 

    for val in ALLCHIPS.chips:
        if(name.lower() == val['Name'].lower()):
            e = await BuildEmbed(ctx,val,game_version)
            foundChip = True

    if not foundChip:
        e = interactions.Embed()
        e.title= "Whoa! I can't find that chip!"
        e.color = interactions.BrandColors.RED


    await ctx.send(embeds = e)        
        
@GetSpecificChip.autocomplete("name")
async def autocomplete_chipname(ctx):
    try:
        choices = [
        interactions.SlashCommandChoice(name=item, value=item) for item in netNavi.chipDict[ctx.kwargs['game_version']].autocompleteNames if ctx.kwargs['name'].lower() in item.lower()
    ] 

        if(len(choices) > 25):
            choices = choices[0:25]

        await ctx.send(choices)
    except:
        pass

@interactions.slash_command(name='navicust_part_details',
        description="Shows the details about the NaviCust part.",
        options=[    
            interactions.SlashCommandOption(
                name="game_version",
                description="What game version",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                    interactions.SlashCommandChoice(
                        name="Battle Network Three",
                        value=Consts.BN3
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Four",
                        value=Consts.BN4
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Five",
                        value=Consts.BN5
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Six",
                        value=Consts.BN6
                    )]
            ),
            interactions.SlashCommandOption(
                name="part",
                description="NaviCrust Part Name",
                type=interactions.OptionType.STRING,
                required=True,
                autocomplete=True
            )]
        )
async def GetSpecificNaviCrustPart(ctx, game_version, part):
    await ctx.defer()
    ALLCHIPS = GetCrustForVersion(game_version)  
    foundChip = False 

    for val in ALLCHIPS.crust:
        if(part.lower() == val['Part'].lower()):
            e = await BuildCrustEmbed(ctx,val,game_version)
            foundChip = True

    if not foundChip:
        e = interactions.Embed()
        e.title= "Whoa! I can't find that NaviCrust Part!"
        e.color = interactions.BrandColors.RED


    await ctx.send(embeds = e)        
        
@GetSpecificNaviCrustPart.autocomplete("part")
async def autocomplete_navicrustName(ctx):
    try:
        choices = [
        interactions.SlashCommandChoice(name=item, value=item) for item in netNavi.crustDict[ctx.kwargs['game_version']].autocompleteNames if ctx.kwargs['Part'].lower() in item.lower()
    ] 

        if(len(choices) > 25):
            choices = choices[0:25]

        await ctx.send(choices)
    except:
        pass

@interactions.slash_command(name='program_advance_details',
        description="Shows the details about a specific Program Advance.",
        options=[    
            interactions.SlashCommandOption(
                name="game_version",
                description="What game version",
                type=interactions.OptionType.STRING,
                required=True,
                choices=[
                    interactions.SlashCommandChoice(
                        name="Battle Network One",
                        value=Consts.BN1
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Two",
                        value=Consts.BN2
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Three",
                        value=Consts.BN3
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Four",
                        value=Consts.BN4
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Five",
                        value=Consts.BN5
                    ),
                    interactions.SlashCommandChoice(
                        name="Battle Network Six",
                        value=Consts.BN6
                    )]
            ),
            interactions.SlashCommandOption(
                name="name",
                description="Name of the Program Advance",
                type=interactions.OptionType.STRING,
                required=True,
                autocomplete=True
            )]
        )
async def GetSpecificPA(ctx, game_version, name):
    await ctx.defer()
    ALLCHIPS = GetPAForVersion(game_version)  
    foundChip = False 

    for val in ALLCHIPS.pa:
        if(name.lower() == val['Name'].lower()):
            e = await BuildEmbed(ctx,val,game_version)
            foundChip = True

    if not foundChip:
        e = interactions.Embed()
        e.title= "Whoa! I can't find that Program Advance!"
        e.color = interactions.BrandColors.RED


    await ctx.send(embeds = e)        
        
@GetSpecificPA.autocomplete("name")
async def autocomplete_paname(ctx):
    try:
        choices = [
        interactions.SlashCommandChoice(name=item, value=item) for item in netNavi.paDict[ctx.kwargs['game_version']].autocompleteNames if ctx.kwargs['name'].lower() in item.lower()
    ] 

        if(len(choices) > 25):
            choices = choices[0:25]

        await ctx.send(choices)
    except:
        pass


@interactions.Task.create(interactions.IntervalTrigger(minutes=10))
async def ListServers():
    if(Consts.TOPGG_AUTHTOKEN is not None):
        async with aiohttp.ClientSession() as session:
            headers = {
                    'Content-Type': "application/json",
                    'Authorization': f"Bearer {Consts.TOPGG_AUTHTOKEN}",
                    'Accept': "*/*",
                    'Host': "top.gg",
                    }
            servercount = len(client.guilds)
            async with session.post(url="https://top.gg/api/bots/1093221391765098567/stats", json={'server_count': servercount}, headers=headers) as response:                
                print("List Server POST Status:", response.status)

@interactions.listen()
async def on_startup():
    await client.change_presence(activity="Busting Viruses!")
    ListServers.start()

client.start()
