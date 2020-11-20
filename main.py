# Bot`s link: https://discord.com/api/oauth2/authorize?client_id=755445994120020119&permissions=1477966966&scope=bot

import discord
from discord.ext import commands
from config import settings
import config
import json
import requests
import random
import praw
import asyncio
import typing
import time
import traceback


# Variables to work with discord module
bot = commands.Bot(command_prefix = settings['prefix']) # Prefix from the config file
client = discord.Client() # Client is a variable used by discord.py
currenttime = time.ctime() # Time variable used by time module

# Variables
opponenthp = 100
playerhp = 100
damage = random.randint( 1, 100 )


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))


@bot.command()
async def say( ctx, text):
    await ctx.message.delete()
    author = ctx.message.author
    sayEm = discord.Embed(
    colour = discord.Colour.teal())
    sayEm.set_author(name=f'{author} используя речевые функции MeowBot')
    sayEm.add_field(name='говорит:', value=f'{text}')
    await ctx.send(embed=sayEm)


@bot.command()
async def hello(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    await ctx.send(f'Приветики-пистолетики, {author.mention}!')


@bot.command()
async def fight(ctx, member: discord.Member):
    await ctx.message.delete()

    global opponenthp
    global playerhp
    global damage

    while opponenthp > 0 or playerhp > 0:
        attackOpponent()
        await ctx.send(f"Вы нанесли {damage} урона {member}")
        await ctx.send(f'Ваш текущий уровень здоровья: {playerhp}')
        attackPlayer()
        await ctx.send(f"Вам нанёс {damage} урона {member}")
        await ctx.send(f'Текущий уровень здоровья {member}: {opponenthp}')
        if opponenthp <= 0:
            await ctx.send("Вы победили")
            opponenthp = 100
            playerhp = 100
            damage = 0
            break
        elif playerhp <= 0:
            await ctx.send("Вы проиграли")
            opponenthp = 100
            playerhp = 100
            damage = 0
            break


@bot.command()
async def clear(ctx, amount = 10):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


def attackOpponent():
    global damage
    global opponenthp
    opponenthp -= damage
    if damage <= 0:
        damage = 5
        damage = random.randint( 1, 100 )
    if opponenthp > 100:
        opponenthp = 100
    if opponenthp < 0:
        opponenthp = 0


def attackPlayer():
    global damage
    global playerhp
    damage -= random.randint( 1, 100)
    playerhp -= damage
    if damage <= 0:
        damage = 5
        damage = random.randint( 1, 100 )
    if playerhp > 100:
        playerhp = 100
    if playerhp < 0:
        playerhp = 0
    

@bot.command()
async def report(ctx, member : discord.Member, reason = 'Не делай так :3'):
    author = ctx.message.author
    await ctx.send(f'{author.mention} пожаловался на {member.mention}, причина: {reason}!')


@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Случайное фото кота :3')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)


@bot.event
async def on_ready():
    print(f'Влетел на сервер как {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="звуки дождя..."), status=discord.Status.do_not_disturb)


@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    author = ctx.message.author
    number = random.randint(1, 20)
    if number == 1:
        await ctx.send(f'{author.mention}, лови шутейку:  – Доктор, как вы думаете, что будет после смерти? – Мы перестелем вашу койку и положим нового пациента.')
    if number == 2:
        await ctx.send(f'{author.mention}, лови шутейку:  Из выпуска новостей: – И, наконец, хорошая новость – на сегодня больше новостей нет.')
    if number == 3:
        await ctx.send(f'{author.mention}, лови шутейку:   Не утихает тысячелетняя битва: люди с кашей в голове против людей с промытыми мозгами…')
    if number == 4:
        await ctx.send(f' {author.mention}, лови шутейку: – Моня, как отразится на России уход Лукашенко в отставку? – Бензин подорожает. – А если не уйдёт? – Всё равно подорожает. ')
    if number == 5:
        await ctx.send(f'{author.mention}, лови шутейку:  Подорожало молоко на три рубля. Эти коровы вообще оборзели…')
    if number == 6:
        await ctx.send(f'{author.mention}, лови шутейку: Лукашенко не идёт на переговоры с протестующими, потому что не знает ни чешского, ни голландского языка.')
    if number == 7:
        await ctx.send(f'{author.mention}, лови шутейку: Он требовал форель на завтрак, но мать дала ему леща…')
    if number == 8:
        await ctx.send(f'{author.mention}, лови шутейку: “Целуется он так себе”, – решила лягушка и не стала превращаться в царевну.')
    if number == 9:
        await ctx.send(f'{author.mention}, лови шутейку:  Молодой проктолог Гера Левензон ещё стеснялся своей профессии и на дверях кабинета с максимальной деликатностью повесил табличку « Ремонт Очков»')
    if number == 10:
        await ctx.send(f'{author.mention}, лови шутейку: Невероятно, но факт. Только 10% людей вступают в дискуссии со своими котами, остальные 90%, слава богу, еще в здравом уме и просто прислушиваются к их советам.')
    if number == 11:
        await ctx.send(f'{author.mention}, лови шутейку: Астронавт Базз Олдрин так говорил, почему Алан Шепард стал первым американцем в космосе: «Вообще, — сказал он, — хотели послать обезьяну, но в НАСА пришла куча писем в защиту прав животных, а в защиту Шепарда не пришло ни одного письма. Вот он и полетел».')
    if number == 12:
        await ctx.send(f'{author.mention}, лови шутейку: Коррупция не знает границ: на конкурсе "Мисс Казахстан" победил 44-летний племянник главы местной администрации.')
    if number == 13:
        await ctx.send(f'{author.mention}, лови шутейку: В Москве нашли 119-летнюю пенсионерку. "Вот с@ка! " — прокомментировал Пенсионный фонд.')
    if number == 14:
        await ctx.send(f'{author.mention}, лови шутейку: Решила жена приготовить для мужа сюрприз. Купила мясо, накрутила фаршу. Заместила тесто и налепила пельменей. Сварила. Вот приходит муж с работы, она накормила и спрашивает. — Ну как пельмешки? — Та знаешь, ты больше такие не покупай.')
    if number == 15:
        await ctx.send(f'{author.mention}, лови шутейку: Дятел задумался и выпал с другой стороны дерева.')
    if number == 16:
        await ctx.send(f"""{author.mention}, лови шутейку: Муж звонит жене: — Милая, это я. Ты только, пожалуйста, не переживай. В общем, меня сбила машина, когда я выходил из офиса. Наташа помогла добраться до больницы. Врачи уже осмотрели меня, сделали рентген и анализ крови. Не обошлось без сотрясения мозга, но хотя бы череп не пробит. Сломана пара ребер, несколько глубоких ран, и возможно придется ампутировать правую ногу. Ответ жены: — Какая еще, на х***, Наташа?! """)
    if number == 17:
        await ctx.send(f'{author.mention}, лови шутейку: Тюрьма. В камеру заводят старенького дедушку. Его обступают блатные. — Ну че дед, за что посадили? — За шуточки. Шутить люблю. — А ну-ка, пошути. — Нет, вы меня потом бить будете. Старший: — Зуб даю, никто не тронет. — Ну, ладно. Дед берет веник, макает его в парашу, стучит в окошко. В окно заглядывает надзиратель. Дед мгновенно втирает веник ему в лицо. Окошко закрывается. Все в камере хохочут. Через минуту открывается дверь — на пороге толпа здоровенных надзирателей с дубинками. Осмотрели камеру взглядом: — А ну ка, старый, отойди в сторонку, сейчас мы с этими шутниками поговорим...')
    if number == 18:
        await ctx.send(f'{author.mention}, лови шутейку: Когда мой муж выходил с маленьким сыном (4 года) гулять, то вся детвора двора просто гроздьями на нем висела, он с ними бегал и раскручивал и на карусели катал, а наш детеныш предпочитал тихие игры в песочнице с формочками. Однажды нам в дверь позвонили, открываю, а там маленький мальчик стоит и спрашивает: — А Влад выйдет? Влад — имя моего мужа... (Причём тут Кэт?)')
    if number == 19:
        await ctx.send(f'{author.mention}, лови шутейку: Осень — это когда куришь, бухаешь, но обязательно в теплых носочках. Здоровье надо беречь.')
    if number == 20:
        await ctx.send(f'{author.mention}, лови шутейку: Объявление: "В ювелирный салон требуются уборщицы для вытирания слюны с пола и витрины".')

@bot.command()
async def credits(ctx):
    await ctx.message.delete()
    creditsEmbed = discord.Embed(
    colour = discord.Colour.red())
    creditsEmbed.set_author(name='Credits: краткая информация о создателе бота')
    creditsEmbed.add_field(name='Credits', value=""" 
    Бота разработал:
    Кэт
    CatProgrammer#3770
    GitHub репозиторий бота:
    https://github.com/CatProgrammerYT/MeowBot""")
    creditsEmbed.set_image(url='https://scontent.fhrk6-1.fna.fbcdn.net/v/t1.0-9/p960x960/118007530_935392656945902_1150181078772392727_o.jpg?_nc_cat=103&_nc_sid=9e2e56&_nc_ohc=0GN9YavYRe4AX8udgFe&_nc_ht=scontent.fhrk6-1.fna&tp=6&oh=661cf838e60097907bc95d89f4cee549&oe=5F80278C')
    await ctx.send(embed=creditsEmbed)


@bot.command()
async def slap(ctx, member : discord.Member):
    urlsList = ['https://media.giphy.com/media/rAKdqZ8nfiaZi/giphy.gif', 'https://media.giphy.com/media/l0HlEqutjbZOZwje0/giphy.gif', 'https://media.giphy.com/media/lYSvai8OdGpP2/giphy.gif',
    'https://media.giphy.com/media/XEVIYsQvFyt2THshE0/giphy.gif']
    await ctx.message.delete()
    author = ctx.message.author
    slapEm = discord.Embed(
    colour = discord.Colour.purple())
    slapEm.add_field(name=f'ШЛЁП', value = f'{author.mention} шлёпнул {member.mention} :3')
    slapEm.set_image(url=random.choice(urlsList))
    await ctx.send(embed=slapEm)

@bot.command()
async def today(ctx):
    await ctx.message.delete()

    timeEm = discord.Embed(
        colour = discord.Color.teal())
    timeEm.add_field(name = f'Текущее время и дата:', value = f'{currenttime}')
    timeEm.set_image(url='https://3.bp.blogspot.com/-vtTqhCHeMkc/WrexQCI6ZUI/AAAAAAAAAos/N8nT1gLTK4oNqMSnLKym080EvJH5LHVPwCLcBGAs/s1600/Date%2Band%2BTime.png')

    await ctx.send(embed=timeEm)

@bot.command()
async def pet(ctx, member: discord.Member):
    urlsList = ['https://media.giphy.com/media/P2IERnBfObaBW/giphy.gif', 'https://media.giphy.com/media/fpimaNarpyW88/giphy.gif', 'https://media.giphy.com/media/wsUtUtLR3A2XPvfLVs/giphy.gif',
    'https://media.giphy.com/media/lnIwMUsMt12UnY7edf/giphy.gif', 'https://media.giphy.com/media/Ul16jlcdV1B04/giphy.gif', 'https://media.giphy.com/media/iYXvjREKcHE0U/giphy.gif', 
    'https://media.giphy.com/media/3o85xJUQuHVCBnWGys/giphy.gif', 'https://media.giphy.com/media/yidUzl6SsJJEmRJuZq/giphy.gif']
    await ctx.message.delete()
    author = ctx.message.author
    petEm = discord.Embed(
    colour = discord.Color.gold())
    petEm.add_field(name = ':3', value=f'{author.mention} потискал {member.mention}')
    petEm.set_image(url=random.choice(urlsList))
    await ctx.send(embed=petEm)


@bot.command()
async def helloTo(ctx, member: discord.Member):
    urlsList = ['https://media.giphy.com/media/L2eThScfeqittTbpWI/giphy.gif', 'https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif', 'https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif',
    'https://media.giphy.com/media/JVmYAO3MkGNiM/giphy.gif', 'https://media.giphy.com/media/xUPGcigl4eOfc6hA5y/giphy.gif', 'https://media.giphy.com/media/3oKIPsx2VAYAgEHC12/giphy.gif']
    await ctx.message.delete()
    author = ctx.message.author
    helloEm = discord.Embed(
        colour = discord.Color.dark_red())
    helloEm.add_field(name='ПЕРЕВЕД', value=f'{author.mention} передаёт привет {member.mention}!')
    helloEm.set_image(url=random.choice(urlsList))
    await ctx.send(embed=helloEm)

@bot.command()
async def love(ctx, member : discord.Member):
    urlsList = ['https://media.giphy.com/media/l41JWw65TcBGjPpRK/giphy.gif', 'https://media.giphy.com/media/3og0ITQEoOUFUi5JcI/giphy.gif', 'https://media.giphy.com/media/xlNDtecvg6zLrXvOaa/giphy.gif',
    'https://media.giphy.com/media/3o7qDJKIO5rSeyHhvO/giphy.gif', 'https://media.giphy.com/media/yc2pHdAoxVOrJ2m5Ha/giphy.gif', 'https://media.giphy.com/media/hqTwf417EvUWeV0XcX/giphy.gif']
    await ctx.message.delete()
    author = ctx.message.author
    loveEm = discord.Embed(
    colour = discord.Color.dark_purple())
    loveEm.add_field(name = 'Ех, любофф, любофф :3', value=f'{author.mention} признался в любви к {member.mention}! :heart:')
    loveEm.set_image(url=random.choice(urlsList))
    await ctx.send(embed=loveEm)
        
    
@bot.command()
async def minds(ctx):
    await ctx.message.delete()
    i = random.randint(1, 5)
    author = ctx.message.author
    if i == 1:
        await ctx.send(f'{author.mention}, холостяки знают женщин лучше, чем женатые; в противном случае они бы тоже женились.— Генри Луис Менкен')
    if i == 2:
        await ctx.send(f'{author.mention}, пошлость, к примеру, то, что каждый недоволен своей участью, даже блестящей, зато доволен своим умом, даже весьма неблестящим.— Балтасар Грасиан')
    if i == 3:
        await ctx.send(f'{author.mention}, жизнь похожа на мыльный пузырь, правда? Они летают, подхваченные ветром. И не успеешь их заметить, как они исчезают… Ты думаешь, что они могут взлететь ещё выше в небо, но уже слишком поздно. ')
    if i == 4:
        await ctx.send(f'{author.mention}, не доверять друзьям позорнее, чем быть ими обманутым.— Франсуа де Ларошфуко')
    if i == 5:
        await ctx.send(f'{author.mention}, стареть - значит переходить от чувств к сочувствию.— Альбер Камю')


@bot.command()
async def facts(ctx):
    await ctx.message.delete()
    randNumber = random.randint(1, 10)
    author = ctx.message.author
    if randNumber == 1:
        await ctx.send(f"""{author.mention}, забавный факт: Сингапур имеет уровень убийств всего 0,2 на 100000 человек.""")
    if randNumber == 2:
        await ctx.send(f"""{author.mention}, забавный факт: Эверест, Непал (местное название Сагарматха) имеет высоту 8 848 метров. Первым на него поднялся сэр Эдмунд Хиллари с его шерпом Тенцингом Норгэем 29 мая 1953.""")
    if randNumber == 3:
        await ctx.send(f"""{author.mention}, забавный факт: яблоки на 25 процентов состоят из воздуха. """)
    if randNumber == 4:
        await ctx.send(f"""{author.mention}, забавный факт: во всех фруктах происходит процесс ферментации и брожения, поэтому все соки содержат определенное количество алкоголя. """)   
    if randNumber == 5:
        await ctx.send(f"""{author.mention}, забавный факт: атмосфера Земли весит 5 300 000 000 000 000 тонн. """)
    if randNumber == 6:
        await ctx.send(f"""{author.mention},забавный факт: в молодости во время крайней нужды Пабло Пикасо сжигал свои собственные творения, чтобы согреться. """)
    if randNumber == 7:
        await ctx.send(f"""{author.mention}, забавный факт: мозг не способен отличить движение по горизонтали от движения по вертикали. """)
    if randNumber == 8:
        await ctx.send(f"""{author.mention}, забавный факт: самая высокая пирамида в мире — Трансамериканская Прирамида в Сан Франциско, высотой 260 метров. """)
    if randNumber == 9:
        await ctx.send(f"""{author.mention}, забавный факт: чаще всего в английских библиотеках воруют Книгу рекордов Гиннесса. """)
    if randNumber == 10:
        await ctx.send(f"""{author.mention}, забавный факт: если вы решили поехать в Исландию, знайте: чаевые в этой стране являются оскорблением. """)


bot.remove_command("""help""")


@bot.command(pass_context = 1)
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("**Время задержки**")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content = "**Время задержки:** `%.2f миллисекунд`" % ping)


@bot.command()
async def repeat(ctx, args):
    await ctx.message.delete()
    await ctx.send(args)

@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        colour = discord.Colour.purple())
    embed.set_author(name='Help: доступные комманды и их описание')
    embed.add_field(name=',joke', value='Бот рассказывает шутку (да, просто рассказывает шутку)', inline=False)
    embed.add_field(name=',facts', value='Случайный факт', inline=False)
    embed.add_field(name=',credits', value='Бесполезная функция, на которую никто никогда не будет обращать внимание', inline=False)
    embed.add_field(name=',cat', value='Случайное фото кота :3')
    embed.add_field(name=',hello', value='Поздоровайся с ботом, хам >:( ')
    embed.add_field(name=',minds', value = 'Умные мысли, которые вдохновляют', inline=False)
    embed.add_field(name=',repeat *любой текст* ', value='Повторяет текст, написаный выше', inline=False)
    embed.add_field(name=',ping', value='Время задержки (в миллисекундах)', inline=False)
    embed.add_field(name=',love *@пользователь*', value = 'Покажи свою любовь :3', )
    embed.add_field(name = ',slap *@пользователь*', value = 'Шлёпни кого-то >:)')
    embed.add_field(name = ',pet *@пользователь*', value='Погладь милашку :3', inline=False)
    embed.add_field(name = ',today', value = 'Текущее время и дата выводятся в чат', inline=False)
    embed.add_field(name=',fight *@пользователь*', value='Давай выйдем раз на раз xD', inline=False)
    embed.add_field(name=',say *текст* (текст без пробелов)', value='Сказать что-то используя речевые функции MeowBot :D', inline=False)
    embed.add_field(name=',clear *количество удалённых сообщений*', value='Удаляет сообщения в количестве, которое вы указали!')
    embed.add_field(name='Это внизу Кэт (создатель бота), если шо ', value=':3', inline=False)
    embed.set_image(url='https://media1.tenor.com/images/b1568040b7983be6c7f8bce94caf8f21/tenor.gif')
    await ctx.send(embed=embed)

bot.run(settings['token'])