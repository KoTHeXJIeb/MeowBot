# Bot`s link: https://discord.com/api/oauth2/authorize?client_id=755445994120020119&permissions=1477966966&scope=bot

import discord
from discord.ext import commands
from config import settings
import json
import requests
import random
import praw
import wikipediaapi
import time
import typing

# Variables to work with discord module
bot = commands.Bot(command_prefix = settings['prefix']) # Prefix from the config file
client = discord.Client()

# Some variables
#wiki_wiki = wikipediaapi.Wikipedia('ru')
bad_wordz = ['блять', 'сука', 'пиздец', 'ебать', 'охуеть', 'пизда']

@bot.command()
async def hello(ctx):
    await ctx.message.delete()
    author = ctx.message.author

    await ctx.send(f'Приветики-пистолетики, {author.mention}!')



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
    https://github.com/CatProgrammerYT/discord_bot """)
    creditsEmbed.set_image(url='https://scontent.fhrk6-1.fna.fbcdn.net/v/t1.0-9/p960x960/118007530_935392656945902_1150181078772392727_o.jpg?_nc_cat=103&_nc_sid=9e2e56&_nc_ohc=0GN9YavYRe4AX8udgFe&_nc_ht=scontent.fhrk6-1.fna&tp=6&oh=661cf838e60097907bc95d89f4cee549&oe=5F80278C')
    await ctx.send(embed=creditsEmbed)


@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} влетел на сервер {0.joined_at}! Скажите ему привет! :raised_hand:'.format(member))


@bot.command()
async def slap(ctx, member : discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    slapEm = discord.Embed(
    colour = discord.Colour.purple())
    slapEm.add_field(name=f'ШЛЁП', value = f'{author.mention} шлёпнул {member.mention} :3')
    slapEm.set_image(url='https://steamuserimages-a.akamaihd.net/ugc/830202924015826450/50671C6E8B6BDCB9CC4190F1E66B73A560FBD2BE/')
    await ctx.send(embed=slapEm)


@bot.command()
async def pet(ctx, member: discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    petEm = discord.Embed(
    colour = discord.Color.gold())
    petEm.add_field(name = ':3', value=f'{author.mention} потискал {member.mention}')
    petEm.set_image(url='https://media.tenor.com/images/dc008a41a50a3e91a523ccb9a1533c40/tenor.gif')
    await ctx.send(embed=petEm)


@bot.command()
async def love(ctx, member : discord.Member):
    await ctx.message.delete()
    author = ctx.message.author
    loveEm = discord.Embed(
    colour = discord.Color.dark_purple())
    loveEm.add_field(name = 'Ех, любофф, любофф :3', value=f'{author.mention} признался в любви к {member.mention}! :heart:')
    loveEm.set_image(url='https://media1.tenor.com/images/31362a548dc7574f80d01a42a637bc93/tenor.gif')
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


@bot.command(pass_context = 1)
async def shutdown(ctx):
    await ctx.message.delete()
    emb = discord.Embed(description = ':exclamation: Бот переходит в спящий режим...', color = 0xffffff)
    emb.set_footer(text = 'Комманду вызвал: %s' % ctx.message.author.name)
    await ctx.send(embed = emb)
    await bot.logout()


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
    embed.add_field(name=',cat', value='Случайное фото кота :3', inline=False)
    embed.add_field(name=',hello', value='Поздоровайся с ботом, хам >:( ', inline=False)
    embed.add_field(name=',minds', value = 'Умные мысли, которые вдохновляют', inline=False)
    embed.add_field(name=',repeat *любой текст* ', value='Повторяет текст, написаный выше', inline=False)
    embed.add_field(name=',ping', value='Время задержки (в миллисекундах)', inline=False)
    embed.add_field(name=',love *@пользователь*', value = 'Покажи свою любовь :3', inline=False)
    embed.add_field(name = ',slap *@пользователь*', value = 'Шлёпни кого-то >:)', inline=False)
    embed.add_field(name = ',pet *@пользователь*', value='Погладь милашку :3', inline=False)
    embed.add_field(name='Это внизу Кэт (создатель бота), если шо ', value=':3', inline=False)
    embed.set_image(url='https://media1.tenor.com/images/b1568040b7983be6c7f8bce94caf8f21/tenor.gif')
    await ctx.send(embed=embed)

bot.run(settings['token'])