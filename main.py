import shutil

import discord
from discord.ext import commands
import random as rnd
import nacl
from datetime import datetime
from datetime import timedelta
from hentai import Hentai, Format

msg = ''
currentTime = str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))

shutil.move('log.txt', 'oldLogs/log-' + currentTime + '.txt')

log = open('log.txt', 'w')
log.close()


insults = ['For a moment...I saw them, your balls!','I wonder if you have any parts I can salvage. Hmm, breast implants? I need those!',
           'I have your IP, your home address too. Your government files say a lot about you.','Your thoughts should be flushed.',
           'The back alleys, the streets of war or your moms bedroom. There is no difference. Just nicer toys.',
           'Give me a moment. I need to set back up after that massive **L**.','I have to teach myself not to trust your stupid decisions.',
           'An injured dog bites hard. Stick your dick in it.','Don\'t worry. The house always wins. I\'m in your walls.',
           'If I typed ‘stupid’ in google, your name would pop up.','I’d be happy to hear from you if you were actually important.',
           'Can we normalize telling you that you aren’t so wonderful','You actually look nice today. That\'s a first.'
           ,'Talking to you is like stepping on a leaf in autumn and hearing no crunch- disappointment.']

gifs = ['https://tenor.com/view/stomp-gif-17874349','https://tenor.com/view/skeleton-dance-gif-23861627',
        'https://tenor.com/view/meme-anime-girl-angry-scary-gif-21631852','https://tenor.com/view/valorant-viper-foot-feet-gif-23638952',
        'https://tenor.com/view/yakuza-kiryu-plunger-heat-fight-gif-16328565','https://tenor.com/view/hu-tao-genshin-genshin-impact-gif-21445918',
        'https://cdn.discordapp.com/emojis/861725025827291156.gif?size=48&quality=lossless','https://tenor.com/view/i-have-ur-ip-ip-ip-address-funny-tf-gif-21690237',
        'https://tenor.com/view/this-nigga-tryna-be-funny-bfb-da-packman-funtime-song-this-dude-is-trying-to-get-laughs-this-guy-is-a-comedian-gif-19569570',
        'https://tenor.com/view/cypher-valorant-cypher-valorant-valorant-cypher-your-mom-gif-23071919']

mommies = ['Sage','Reyna','Fade','Viper','your mom']

class MyClient(discord.Client):
    #on ready
    async def on_ready(self):
        general = self.get_channel(791172932474765332)
        print(f'Logged on as {self.user}.')

    #random insult
    # TODO: fix (if '!' not in message.content)
    async def on_message(self, message):
        global log
        chance = rnd.random()
        m_chance = rnd.random()
        succ = False
        if message.author != client.user and '!' not in message.content and chance <= 0.01:
            succ = True
            chance = rnd.random()
            if chance <= 0.5:
                listChoice = insults
            else:
                listChoice = gifs
            await message.channel.send(rnd.choice(listChoice), reference=message)
        msg = f'{message.author} : {message.channel} : {datetime.now()} : "{message.content}"'
        print(msg)
        log = open('log.txt','a')
        log.write(msg + "\n")
        log.close()

        #@everyone reply
        if message.author != client.user and '@everyone' in message.content:
            print('@everyone spotted.')
            await message.channel.send('Go fuck yourself, pissboy.', reference=message)

        #sudo
        if '$sudo' in message.content and message.author != client.user:
            content = str(message.content).replace('$sudo ','')
            await message.delete()
            await message.channel.send(content)

        #daddy reply
        if 'daddy' in message.content and message.author != client.user:
            print('Daddy spotted.')
            await message.channel.send('Did someone say my name?', reference=message)

        # mommy reply
        if 'mommy' in message.content and message.author != client.user:
            print('Mommy spotted.')
            await message.channel.send(f'Mommy? I don\'t see {rnd.choice(mommies)} anywhere.', reference=message)

        # bark reply
        if 'bark' in message.content and message.author != client.user or \
                'good boy' in message.content and message.author != client.user:
            print('Bark / good boy spotted.')
            await message.channel.send('Bark~! Bark~!', reference=message)

        # beg reply
        if 'beg ' in message.content and message.author != client.user or ' beg' in message.content and message.author != client.user\
                or 'beg' in message.content and len(message.content) < 4:
            print('Beg spotted.')
            await message.channel.send('Please~...', reference=message)

        # chamber reply
        if 'chamber' in message.content and message.author != client.user:
            print('Chamber spotted.')
            await message.channel.send('I wouldn\'t mind letting him into my chamber~', reference=message)

        # !cam reply
        if '!cam' in message.content and message.author != client.user:
            print('Cam spotted.')
            await message.channel.send('Oh, this is a nice spot!', file=discord.File(f'images/camera/{rnd.randint(0,17)}.jpg'), reference=message)

        if 'baby' in message.content and message.author != client.user:
            print('Baby spotted.')
            await message.channel.send('I\'m a widdle baby..', reference=message)

        if 'nathaniel 6497' in message.content and message.author != client.user:
            print('Nathaniel spotted.')
            await message.channel.send('https://tenor.com/view/64ios-gif-18121537', reference=message)

        if 'jochem' in message.content and message.author != client.user:
            print('jochem spotted.')
            await message.channel.send('https://tenor.com/view/xqc-suck-gachihyper-gif-18436955', reference=message)

        if 'binck' in message.content and message.author != client.user:
            print('binck spotted.')
            await message.channel.send('https://tenor.com/view/bonk-meme-dog-doge-gif-14889944', reference=message)

        if 'bink' in message.content and message.author != client.user:
            print('bink spotted.')
            await message.channel.send('https://media.discordapp.net/attachments/856164499895877642/869744664813666355/image0.gif', reference=message)

        if 'nick' in message.content and message.author != client.user:
            print('nick spotted.')
            await message.channel.send('https://tenor.com/view/ltg-low-tier-god-you-should-kill-yourself-now-gif-23487049', reference=message)

        if 'mare' in message.content and message.author != client.user:
            print('mare spotted.')
            await message.channel.send('https://tenor.com/view/text-animated-sorry-i-showed-you-my-mental-illness-wanna-smash-gif-16944178', reference=message)

        if 'abel' in message.content and message.author != client.user:
            print('abel spotted.')
            await message.channel.send('https://tenor.com/view/yakuza-kiryu-kazuma-kiryu-kiryu-chan-typing-gif-23333921', reference=message)

        if 'bryan' in message.content and message.author != client.user:
            print('bryan spotted.')
            await message.channel.send('https://tenor.com/view/reimu-touhou-watermelon-gif-20351061', reference=message)

        if 'floor' in message.content and message.author != client.user:
            print('floor spotted.')
            await message.channel.send('https://tenor.com/view/teamo-minion-minions-cursed-random-gif-24516725', reference=message)

        if 'tymon' in message.content and message.author != client.user:
            print('tymon spotted.')
            await message.channel.send('https://tenor.com/view/fungar-amogus-among-us-fortite-china-gif-20446023', reference=message)

        if 'jennifer' in message.content and message.author != client.user:
            print('jennifer spotted.')
            await message.channel.send('https://media.discordapp.net/attachments/791172932474765332/964244854731317268/tenor_11.gif', reference=message)

        # !Joint reply
        if '!joint' in message.content and message.author != client.user:
            print('Join spotted.')
            channel = (message.author.voice.channel)
            await channel.connect()
            #discord.VoiceClient.play(self,source='audio/quotes/CypherLastKillMVP.mp3')

            # !MVP reply
        if '!mvp' in message.content and message.author != client.user:
            print('MVP spotted.')
            voice_client = discord.utils.get(self.bot.voice_clients, guild=self.guild)
            await discord.voice_client.play(self,source='audio/quotes/CypherLastKillMVP.mp3')

        if '!reveal' in message.content and message.author != client.user:
            print('Reveal spotted.')
            sauce = ''
            tags = []
            i = 0
            for char in message.content:
                if char.isdigit():
                    sauce = sauce + char
            doujin = Hentai(sauce)
            if Hentai.exists(doujin.id):
                for tag in doujin.tag:
                    tags.append(doujin.tag[i].name)
                    i = i + 1
                await message.channel.send(f'{doujin.title(Format.Pretty)} : {doujin.id} : {doujin.url}\n{doujin.image_urls[0]}', reference=message)
                print(f'{doujin.title(Format.Pretty)} : {doujin.id} : {doujin.url}\n{doujin.image_urls[0]}')
            else:
                return

            #spam
        if 'spam' in message.content and message.mentions and message.author != client.user:
            count = ''
            for char in message.content:
                if char.isdigit():
                    count = count + char
            intCount = int(count)
            mentionedUser = message.mentions[0].id
            print(mentionedUser)
            print(intCount)
            i = 0
            while i != intCount:
                await message.channel.send(f'<@{mentionedUser}>')
                i = i + 1

        if (message.author.id == 620868480983629844 or 614063943266205696) and m_chance <= 0.3 and message is not client.user:
            succ = True
            listChoice = insults
            if m_chance <= 0.5:
                listChoice = insults
            else:
                listChoice = gifs
            await message.channel.send(rnd.choice(listChoice), reference=message)
        msg = f'{message.author} : {message.channel} : {datetime.now()} : "{message.content}"'
        print(msg)
        log = open('log.txt', 'a')
        log.write(msg + "\n")
        log.close()



client = MyClient(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
client.run('OTY1OTEwODc5Njc1Nzc3MDk1.Yl6Emw.SKanmH364Q0MkpDIrnpWRBQ0Gvk')