#FIRST BOT

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import random
import logging
import string
import time
import datetime

logging.basicConfig(level=logging.INFO)

print("Starting nexascain.py . . .")
bot = commands.Bot(command_prefix = "-")

#Game reference
#Word Guess
word = 0
#MasterMind
guessNum = 0
combo = 0
mmplayer = 0
#DiceLuck
totalplayers = 0
player1name = 0
player2name = 0
player3name = 0
starttestgame = 0
roll1 = 0
roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
keepRoll = 0
playersTurn = 0
currentRoll = 0
lastRoll = 0
currentTotal = 0
player1total = 0
player2total = 0
player3total = 0
numbOfDice = 5
diceluckGoal = 300

#TicTacToe
tttP1 = 0
tttP2 = 0
tttBlank = ":black_medium_square:"
ttt1 = tttBlank
ttt2 = tttBlank
ttt3 = tttBlank
ttt4 = tttBlank
ttt5 = tttBlank
ttt6 = tttBlank
ttt7 = tttBlank
ttt8 = tttBlank
ttt9 = tttBlank
tttWinner = 0
tttStart = 0
tttTimer = 0
tttTime = 0
tttTimerStop = 0
when_to_stop = 0

tttLayout = """
:one: :two: :three:
:four: :five: :six:
:seven: :eight: :nine:"""

diceluckInstructions = """
DiceLuck is a game where you roll dice, take chances, and gamble your points! First to %s or beyond wins!
When it's your turn, You can either take a chance with the dice the player before you kept (along with the score they earned), or start from scratch.
If the player before you looses their score, you cannot use their dice, and their score is lost!
If you don't score points on a roll, you loose your roll!
If you decide to keep what you have, you keep the points, and the next player can roll off of your recent score!
Good luck!"""%(str(diceluckGoal))
diceluckRules = """

To earn points in DiceLuck, you must roll one or a combination of the following:
1 1 1 = 100 points
2 2 2 = 20 points
3 3 3 = 30 points
4 4 4 = 40 points
5 5 5 = 50 points
6 6 6 = 60 points
5 = 5 points
1 = 10 points

When you roll these, the dice that gave you the points are held, and cannot be rolled.
However, if all five dice are held, you may roll all five dice again to have a chance to enhance your current score.
If you roll and get no points, your turn ends and you've lost all the points you gained on that turn. """


bothelpMessage = """**-bothelp**
(This command)

**__[Game Commands]__**
**__|WordGuess|__**
**-WordGuess**
(Starts the Word guess game or gives a new word)

**__|Mastermind|__**
**-Mastermind**
(Starts a game of Mastermind)

**-mm <3 digit number>**
(Used to submit a guess to the answer for Mastermind)

**__|TicTacToe|__**
**-ttt**
(Joins you to a game of TicTacToe if one isn't in progress)

**<Number 1-9>**
(Places your mark on that space)

**__|DiceLuck|__**
**-DiceLuck Help**
(Shows all commands for DiceLuck)

**__|Truth or Dare|__**
**-ToD**
(Asks the bot "Truth or Dare")

**-Truth**
(The bot will tell you the truth)

**-Dare**
(The bot will dare you... have fun!)

**__[Question Commands]__**
**-Why**
(Ask the bot a "Why..." question)

**-When**
(Ask the bot a "When..." question)

**-Will**
(Ask the bot a "Will..." question)

**__[Other Commands]__**
**-math <Math Expression>**
(Solves a math expression using Python supported opperations)
(type **-bhelp math** for more info)"""



words = [("GAMES", "games"),                    ("INSTAGRAM", "instagram"),             ("HELLO", "hello"),             ("FILE", "file"),
        ("MINECRAFT", "minecraft"),             ("SNAPCHAT", "snapchat"),               ("PIZZA", "pizza"),             ("STAMP", "stamp"),
        ("CHEESECAKE", "cheesecake"),           ("FACEBOOK", "facebook"),               ("DISK","disk"),                ("SWAP", "swap"),
        ("FALLOUT", "fallout"),                 ("METROID", "metroid"),                 ("PAPER", "paper"),             ("WASP", "wasp"),
        ("ENVOLOPE", "envolope"),               ("OBSIDIAN", "obsidian"),               ("PHONE", "phone"),             ("ANT", "ant"),
        ("ATOMIC", "atomic"),                   ("PYTHON", "python"),                   ("CHOICE", "choice"),           ("FUN", "fun"),
        ("RADIOACTIVE", "radioactive"),         ("DETECTIVE", "detective"),             ("START", "start"),             ("SUPER", "super"),
        ("GRANDFATHER", "grandfather"),         ("BATMAN", "batman"),                   ("POWER", "power"),             ("CHAIR", "chair"),
        ("MARVEL", "marvel"),                   ("TOASTER", "toaster"),                 ("TIME", "time"),               ("DESK", "desk"),
        ("DOMINO", "domino"),                   ("CHIMICHANGA", "chimichanga"),         ("PRINTER", "printer"),         ("BOOK", "book"),
        ("SPAMBOT", "spambot"),                 ("DRAGON", "dragon"),                   ("NIGHT", "night"),             ("HUNGER", "hunger"),
        ("MECHANICAL", "mechanical"),           ("TREATY", "treaty"),                   ("DAY", "day"),                 ("JAVA", "java"),
        ("HEADPHONES", "headphones"),           ("CHICKEN", "chicken"),                 ("MORNING", "morning"),         ("SCRIPT", "script"),
        ("HANDBAG", "handbag"),                 ("TAFFY", "taffy"),                     ("MOUSE", "mouse"),             ("FAN", "fan"),
        ("MULTIPLICATION", "multiplication"),   ("SLEEP", "sleep"),                     ("ZERO", "zero"),               ("SEVEN", "seven"),
        ("TEST", "test"),                       ("SUGGESTIONS", "suggestions"),         ("ONE", "one"),                 ("EIGHT", "eight"),
        ("GLOVES", "gloves"),                   ("BASKET", "basket"),                   ("TWO", "two"),                 ("NINE", "nine"),
        ("EDUCATED", "educated"),               ("HYDROGEN", "hydrogen"),               ("THREE", "three"),             ("TEN", "ten"),
        ("STRANGER", "stranger"),               ("PLUTONIUM", "plutonium"),             ("FOUR", "four"),               ("SEVENTEEN", "seventeen"),
        ("ARMADA", "armada"),                   ("TELEVISION", "television"),           ("FIVE", "five"),
        ("AWESOME", "awesome"),                 ("SYRUP", "syrup"),                     ("SIX", "six"),
        ("RAINSTORM", "rainstorm"),
        ("PANCAKE", "pancake"),
        ("UNKNOWN", "unknown"),
        ("SCIENTIFIC", "scientific"),
        ("SPARKLING", "sparkling"),
        ("EARTHQUAKE", "earthquake"),
        ("GUARANTEE", "guarantee"),
        ("EXERCISE", "exercise"),
        ("WINE", "wine"),
        ("WACKY", "wacky"),
        ("MAGENTA", "magenta"),
        ("COMMUNICATE", "communicate"),
        ("DEAR", "dear"),
        ("READ", "read"),
        ("READY", "ready"),
        ("CHESS", "chess"),
        ("SYSTEM", "system"),
        ("STRENGTHEN", "strengthen"),
        ("PROGRAM", "program"),
        ("IDIOTIC", "idiotic"),
        ("SUCCEED", "succeed"),
        ("PREPARE", "prepare"),
        ("AMERICA", "america")
        ]



async def embed_this(embTITLE, embDESCRIPTION, embCOLOUR, embAUTHOR):
    em = discord.Embed(title=embTITLE, description=embDESCRIPTION, colour=embCOLOUR)
    em.set_author(name=embAUTHOR)
    await bot.send_message(message.channel,content=None, embed=em)



class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.event
async def on_ready():
    print ("Ready to go Sire!")
    print ("I am rinning on " + bot.user.name)
    await bot.change_presence(game=discord.Game(name='-bothelp'))

@bot.event
async def on_member_join(member):
    new_members_channel = member.server.default_channel
    await bot.send_message(new_members_channel, "TEST")
    await bot.send_message(new_members_channel, "Welcome, " + member.name + ", to Nexas' bot testing server!")


@bot.event
async def on_message(message):
    #Rank giving command
    if message.content.startswith("-role"):
        team_list = ["Minecraft Player", "Roblox Player", "Fortnite Player"]
        entered_team = message.content[6:]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "403362388071415809",
            "403362453078933516",
            "403362486830628865",
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await bot.send_message(message.channel, "Game role either doesn't exist, or you're not allowed to self-assign it. Game roles that are allowed are `Minecraft Player`, `Fortnite Player`, and `Roblox Player`.")
            return
        elif role in message.author.roles:
            # If they already have the role
            await bot.send_message(message.channel, "You already have this role.")
        else:
            try:
                await bot.add_roles(message.author, role)
                await bot.send_message(message.channel, "Successfully added role " + role.name)
            except discord.Forbidden:
                await bot.send_message(message.channel, "I don't have perms to add roles.")

    if message.content.startswith("-unrole"):
        team_list = ["Minecraft Player", "Roblox Player", "Fortnite Player"]
        entered_team = message.content[8:]
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles
            "403362388071415809",
            "403362453078933516",
            "403362486830628865",
        ]
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await bot.send_message(message.channel, "Game role either doesn't exist, or you're not allowed to self-remove it. Game roles that are allowed are `Minecraft Player`, `Fortnite Player`, and `Roblox Player`.")
            return
        elif role in message.author.roles:
            try:
                await bot.remove_roles(message.author, role)
                await bot.send_message(message.channel, "Successfully removed role " + role.name)
            except discord.Forbidden:
                await bot.send_message(message.channel, "I don't have permission to remove roles.")
        else:
            await bot.send_message(message.channel, "You do not have this role, so I can't remove it.")




    #Ping
    if message.content.upper().startswith("-PING"):
        await bot.send_message(message.channel, ":ping_pong: Pong!")
    #Info
    if message.content.upper().startswith("-INFO"):
        #await bot.send_message(message.channel, "My name is " + bot.user.name)
        #await bot.send_message(message.channel, "I was created by Nexas Cain with the help of a meme (Rab), Plater, and the encouragement from Nexas' best friends. Nexas won't admit this, but he is very greatful for all who helped!")

        em = discord.Embed(title=None, description=":video_game: I was created by Nexas Cain with the help of a meme (Rab), Plater, and the encouragement from Nexas' best friends. Nexas won't admit this, but he is very greatful for all who helped! :space_invader:", colour=0xBCAD20)
        em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        em.set_footer(text="I'm watching you %s"%(message.author.name))
        em.set_image(url=bot.user.avatar_url)
        await bot.send_message(message.channel,content=None, embed=em)

        #await client.send_file(discord.AppInfo.icon)

    #User Info
    if message.content.upper().startswith("-USERINFO"):
        user_peep = message.content[10:]
        if user_peep != None:
            if user_peep in message.server.members.name:
                info_peep = user_peep
            else:
                info_peep = message.author
        elif user_peep == None:
            info_peep = message.author
        await bot.send_message(message.channel, user_peep)
        em = discord.Embed(title="Userinfo of %s"%(info_peep.name), description="", colour=0xBCAD20)
        em.set_author(name=info_peep.name, icon_url=info_peep.avatar_url)
        em.set_image(url=info_peep.avatar_url)
        await bot.send_message(message.channel, content=None, embed=em)

    #Will
    if message.content.upper().startswith("-WILL"):
        ball_options = ["Yes", "No", "Maybe", "I don't know", "Not today", "Never", "Always", "Ask Nexas instead"]
        ball = random.choice(ball_options)
        await bot.send_message(message.channel, ball)

    #When
    if message.content.upper().startswith("-WHEN"):
        ball_options = ["What do I look like, a fortune teller? Someone who sees the future? Ask again...", "Now", "Already happened", "Today", "Not today", "Soon", "Tomorrow", "Next week", "Next month", "Next year", "In a few days", "In a couple weeks", "In a few months", "Several months from now", "In a couple years", "Many years from now", "Likely never", "Certainly never", "All the time"]
        ball = random.choice(ball_options)
        await bot.send_message(message.channel, ball)

    #Why
    if message.content.upper().startswith("-WHY"):
        ball_options = ["Why not?",
                        "Just because",
                        "I say so",
                        "Nexas says so",
                        "I read it in your mind",
                        "You know the answer",
                        "It's in my grimoire.",
                        "Because war... war never changes",
                        "It is possible I'm lying",
                        ". . . oh, you wanted me to respond?",
                        "Sorry, I'm not here right now",
                        "I watched a video about that"]
        ball = random.choice(ball_options)
        await bot.send_message(message.channel, ball)

    #Kill Nex
    if message.content.upper().startswith("-KILLNEX"):
        await bot.send_message(message.channel, "No, it's not my time! I need mor- ")
    if message.content.upper().startswith("NO, IT'S NOT MY TIME"):
        await bot.add_reaction(message, '\N{Pistol}')
        await bot.add_reaction(message, '\N{Dagger Knife}')
        await bot.add_reaction(message, '\N{Bomb}')
        await bot.add_reaction(message, '\N{Hocho}')
        await bot.add_reaction(message, '\N{Skull}')
        await bot.add_reaction(message, '\N{Coffin}')
        #await bot.send_message(message.channel, "TEST")

    #Math
    if message.content.upper().startswith("-MATH"):
        eq1 = message.content[6:]
        def less_dangerous_eval(equation):
            if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
                return eval(equation)
            else:
                bot.send_message(message.channel, "illegal character")
                return None

        evaled = less_dangerous_eval(eq1)
        await bot.send_message(message.channel, evaled)


    if message.content.upper().startswith("-BHELP MATH"):
        await bot.send_message(message.channel, """```
[-Math Help]
|Supported opperations|
+   (Addition)

-   (Subtraction)

*   (Multiplication)

/   (Division)

()  (Parenthases)

**  (Exponents)```""")

    #Hello
    if message.content.upper().startswith("-HELLO"):
        greetings = ["Hey there!",
                    "Hi!",
                    "Heyo!",
                    "What's up?",
                    "Yo"]
        greet = random.choice(greetings)
        await bot.send_message(message.channel, greet)

    #ToD
    if message.content.upper().startswith("-TOD"):
        options = ["Truth", "Dare"]
        opt = random.choice(options)
        await bot.send_message(message.channel, opt)

    #Truth
    if message.content.upper().startswith("-TRUTH"):
        options = ["I was originally a game concept",
                    "My creator is adopted",
                    "I don't like this game, can we play something different?"]
        opt = random.choice(options)
        await bot.send_message(message.channel, opt)

    #Dare
    if message.content.upper().startswith("-DARE"):
        options = ["Give suggestions for dares!",
                    "This is a work in progress, sorry!",
                    "Beep Nexas and tell him to finish this game!"]
        opt = random.choice(options)
        await bot.send_message(message.channel, opt)

    #BEEP
    if message.content.upper().startswith("-BEEP"):
        if message.author.id == '329058795026382849':
            peeps = message.server.members
            peep = random.choice(list(peeps))
            await bot.send_message(message.channel, "<@%s>" %(peep.id))
        else:
            await bot.send_message(message.channel, "You do not have permission to use this command")




    if message.content.upper().startswith("-DICELUCK HELP"):
        await bot.send_message(message.channel, """```
DICELUCK Help

-DiceLuck Rules
(Tells the rules and instructions for DiceLuck)

-DiceLuck Join
(Joins you to a game of DiceLuck)

-DL Goal <number>
(Use to set a custom goal before the game, default goal is 300)

-DL Leave
(Removes you from the DiceLuck game que)

-DL Start
(Starts the game)

-DL Roll
(Rolls the dice if it's your turn, and rolls off of someone elses if another player's turn just ended)

-DL No
(Starts your turn from scratch)

-DL Score
(Shows the scores of the current game)

-DL Reset
(Resets the DiceLuck game)
(Only those with permission can use this command!)```""")


    if message.content.upper().startswith("-DICELUCK RULES"):
        await bot.send_message(message.channel, diceluckInstructions)
        await bot.send_message(message.channel, diceluckRules)

    if message.content.upper().startswith("-DICELUCK JOIN") or message.content.upper().startswith("-DL JOIN"):
        global player1name
        global player2name
        global player3name
        global totalplayers
        global starttestgame
        global playersTurn
        global roll1
        global roll2
        global roll3
        global roll4
        global roll5
        global currentTotal
        global player1total
        global player2total
        global player3total
        global numbOfDice
        global diceluckGoal
        if starttestgame == 1:
            await bot.send_message(message.channel, "Please wait for the current game to finish.")
        elif player1name == 0:
            if message.author.nick != None:
                player1name = message.author.nick
            else:
                player1name = message.author.name
            totalplayers += 1
            await bot.send_message(message.channel, "**" + player1name + "** has joined, and is player one!")
        elif player2name == 0:
            if message.author.nick != None:
                player2name = message.author.nick
            else:
                player2name = message.author.name
            totalplayers += 1
            await bot.send_message(message.channel, "**" + player2name + "** has joined, and is player two!")
        elif player3name == 0:
            if message.author.nick != None:
                player3name = message.author.nick
            else:
                player3name = message.author.name
            totalplayers += 1
            await bot.send_message(message.channel, "**" + player3name + "** has joined, and is player three!")
        else:
            await bot.send_message(message.channel, "Sorry, but no more players can join at this time.")

        await bot.send_message(message.channel, "You can set a goal between 100 and 1000 with `-DL Goal <number>`, and the current goal is **" + str(diceluckGoal) + "**")

        if totalplayers == 1:
            await bot.send_message(message.channel, "You need at least one more player to start!")
        if totalplayers == 2:
            await bot.send_message(message.channel, "If you two are the only players who want to play, type `-DL Start`")
        if totalplayers == 3:
            await bot.send_message(message.channel, "No more players can join, please type `-DL Start`")

    if message.content.upper().startswith("-DL LEAVE"):
        if message.author.nick != None:
            leaver = message.author.nick
        else:
            leaver = message.author.name
        if leaver == player1name:
            await bot.send_message(message.channel, "**" + leaver + "** has left the game.")
            player1name = 0
            totalplayers -= 1
            if totalplayers == 1:
                starttestgame = 0
                if player2name != 0:
                    await bot.send_message(message.channel, "**" + player2name + "** wins by default. A new game is ready to be played!")
                    player2name = 0
                elif player3name != 0:
                    await bot.send_message(message.channel, "**" + player3name + "** wins by default. A new game is ready to be played!")
                    player3name = 0

            else:
                if player2name != 0:
                    playersTurn = player2name
                    await bot.send_message(message.channel, "**" + player2name + "** may take their turn now.")
                elif player3name != 0:
                    playersTurn = player3name
                    await bot.send_message(message.channel, "**" + player3name + "** may take their turn now.")

        elif leaver == player2name:
            await bot.send_message(message.channel, "**" + leaver + "** has left the game.")
            player2name = 0
            totalplayers -= 1
            if totalplayers == 1:
                starttestgame = 0
                if player1name != 0:
                    await bot.send_message(message.channel, "**" + player1name + "** wins by default. A new game is ready to be played!")
                    player1name = 0
                elif player3name != 0:
                    await bot.send_message(message.channel, "**" + player3name + "** wins by default. A new game is ready to be played!")
                    player3name = 0

            else:
                if player3name != 0:
                    playersTurn = player3name
                    await bot.send_message(message.channel, "**" + player3name + "** may take their turn now.")
                elif player1name != 0:
                    playersTurn = player1name
                    await bot.send_message(message.channel, "**" + player1name + "** may take their turn now.")

        elif leaver == player3name:
            await bot.send_message(message.channel, "**" + leaver + "** has left the game.")
            player3name = 0
            totalplayers -= 1
            if totalplayers == 1:
                starttestgame = 0
                if player2name != 0:
                    await bot.send_message(message.channel, "**" + player2name + "** wins by default. A new game is ready to be played!")
                    player2name = 0
                elif player1name != 0:
                    await bot.send_message(message.channel, "**" + player1name + "** wins by default. A new game is ready to be played!")
                    player1name = 0

            else:
                if player1name != 0:
                    playersTurn = player1name
                    await bot.send_message(message.channel, "**" + player1name + "** may take their turn now.")
                elif player2name != 0:
                    playersTurn = player2name
                    await bot.send_message(message.channel, "**" + player2name + "** may take their turn now.")

        else:
            await bot.send_message(message.channel, "You are not in this game **" + leaver + "**")

    if message.content.upper().startswith("-DL RESET"):
        resetterRoles = message.author.roles
        for role in resetterRoles:
            if role.id == "390624920360714240":
                if message.author.nick != None:
                    resetter = message.author.nick
                else:
                    resetter = message.author.name
                await bot.send_message(message.channel, "Authorized. Reseting DiceLuck. . .")
                player1name = 0
                player2name = 0
                player3name = 0
                starttestgame = 0
                totalplayers = 0
                roll1 = 0
                roll2 = 0
                roll3 = 0
                roll4 = 0
                roll5 = 0
                keepRole = 0
                playersTurn = 0
                keepRoll = 0
                player1total = 0
                player2total = 0
                player3total = 0
                numbOfDice = 5
                diceluckGoal = 300
                await bot.send_message(message.channel, "DiceLuck has been reset **" + resetter + "**!")


    if message.content.upper().startswith("-DL START"):
        if starttestgame == 1:
            await bot.send_message(message.channel, "A game is already in progress. Please wait for this game to finish before starting a new game.")
        elif totalplayers >= 2:
            starttestgame = 1
            await bot.send_message(message.channel, "Welcome to DiceLuck!")
            await bot.send_message(message.channel, diceluckInstructions + diceluckRules)
            playersTurn = player1name
            await bot.send_message(message.channel, "**" + playersTurn + "** may begin. use the command `-DL Roll` to take your turn.")
        else:
            await bot.send_message(message.channel, "You need at lease two players to play this game!")

    if message.content.upper().startswith("-DL TEST"):
        await bot.send_message(message.channel, playersTurn)


    if message.content.upper().startswith("-DL ROLL"):
        if message.author.nick != None:
            roller = message.author.nick
        else:
            roller = message.author.name
        if roller == playersTurn:
            global currentRoll
            global lastRoll
            dicesides = [(1,":one:"), (2,":two:"), (3,":three:"), (4,":four:"), (5,":five:"), (6,":six:")]
            if numbOfDice == 0:
                numbOfDice == 5
            if numbOfDice >= 1:
                roll1 = random.choice(dicesides)
                if numbOfDice >= 2:
                    roll2 = random.choice(dicesides)
                    if numbOfDice >= 3:
                        roll3 = random.choice(dicesides)
                        if numbOfDice >= 4:
                            roll4 = random.choice(dicesides)
                            if numbOfDice == 5:
                                roll5 = random.choice(dicesides)
                            else:
                                roll5 = (0, ":record_button:")
                        else:
                            roll4 = (0, ":record_button:")
                            roll5 = (0, ":record_button:")
                    else:
                        roll3 = (0, ":record_button:")
                        roll4 = (0, ":record_button:")
                        roll5 = (0, ":record_button:")
                else:
                    roll2 = (0, ":record_button:")
                    roll3 = (0, ":record_button:")
                    roll4 = (0, ":record_button:")
                    roll5 = (0, ":record_button:")


            await bot.send_message(message.channel, roll1[1] + roll2[1] + roll3[1] + roll4[1] + roll5[1])
            rolledNumbs = [roll1[0],roll2[0],roll3[0],roll4[0],roll5[0]]

            numbOfZeros = 0
            numbOfOnes = 0
            numbOfTwos = 0
            numbOfThrees = 0
            numbOfFours = 0
            numbOfFives = 0
            numbOfSixs = 0
            for number in rolledNumbs:
                if number == 0:
                    numbOfZeros += 1
                if number == 1:
                    numbOfOnes += 1
                if number == 2:
                    numbOfTwos += 1
                if number == 3:
                    numbOfThrees += 1
                if number == 4:
                    numbOfFours += 1
                if number == 5:
                    numbOfFives += 1
                if number == 6:
                    numbOfSixs += 1

            if numbOfOnes >= 3:
                currentTotal += 100
                numbOfOnes -= 3
                numbOfDice -= 3
            if numbOfTwos >= 3:
                currentTotal += 20
                numbOfTwos -= 3
                numbOfDice -= 3
            if numbOfThrees >= 3:
                currentTotal += 30
                numbOfThrees -= 3
                numbOfDice -= 3
            if numbOfFours >= 3:
                currentTotal += 40
                numbOfFours -= 3
                numbOfDice -= 3
            if numbOfFives >= 3:
                currentTotal += 50
                numbOfFives -= 3
                numbOfDice -= 3
            if numbOfSixs >= 3:
                currentTotal += 60
                numbOfSixs -= 3
                numbOfDice -= 3
            if numbOfOnes == 1:
                currentTotal += 10
                numbOfOnes -= 1
                numbOfDice -= 1
            if numbOfOnes == 2:
                currentTotal += 20
                numbOfOnes -= 2
                numbOfDice -= 2
            if numbOfFives == 1:
                currentTotal += 5
                numbOfFives -= 1
                numbOfDice -= 1
            if numbOfFives == 2:
                currentTotal += 10
                numbOfFives -= 2
                numbOfDice -= 2
            if numbOfDice == 0:
                numbOfDice += 5


            numbOfZeros = 0
            numbOfOnes = 0
            numbOfTwos = 0
            numbOfThrees = 0
            numbOfFours = 0
            numbOfFives = 0
            numbOfSixs = 0

            if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                if player1total >= diceluckGoal:
                    dlwinTotal = player1total
                    dlWinner = player1name
                elif player2total >= diceluckGoal:
                    dlwinTotal = player2total
                    dlWinner = player2name
                elif player3total >= diceluckGoal:
                    dlwinTotal = player3total
                    dlWinner = player3name
                await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                totalplayers = 0
                player1name = 0
                player2name = 0
                player3name = 0
                starttestgame = 0
                roll1 = 0
                roll2 = 0
                roll3 = 0
                roll4 = 0
                roll5 = 0
                keepRoll = 0
                playersTurn = 0
                currentRoll = 0
                lastRoll = 0
                currentTotal = 0
                player1total = 0
                player2total = 0
                player3total = 0
                numbOfDice = 5
                diceluckGoal = 300

            elif lastRoll == currentTotal:
                currentTotal = 0
                lastRoll = 0
                numbOfDice = 5
                if roller == player1name:
                    if player2name != 0:
                        playersTurn = player2name
                    else:
                        playersTurn = player3name

                elif roller == player2name:
                    if player3name != 0:
                        playersTurn = player3name
                    else:
                        playersTurn = player1name

                elif roller == player3name:
                    if player1name != 0:
                        playersTurn = player1name
                    else:
                        playersTurn = player2name

                await bot.send_message(message.channel, "Sorry, you lost this roll! Next up, **" + playersTurn + "**. Use `-DL Roll` to begin your turn!")
            else:
                lastRoll = currentTotal
                if playersTurn == player1name:
                    possibleTotal = player1total + currentTotal
                elif playersTurn == player2name:
                    possibleTotal = player2total + currentTotal
                elif playersTurn == player3name:
                    possibleTotal = player3total + currentTotal
                await bot.send_message(message.channel, "Your score for this turn: **" + str(currentTotal) + "**")
                await bot.send_message(message.channel, "If you do `-DL Keep`: **" + str(possibleTotal) + "**")
                await bot.send_message(message.channel, "Dice you can roll on your next turn: **" + str(numbOfDice) + "**")
                await bot.send_message(message.channel, "Would you like to keep your score, or roll again for more? Use `-DL Keep` or `-DL Roll`")




        else:
            await bot.send_message(message.channel, "Please wait your turn if you are playing, and if you aren't, don't try to mess with the game in progress or start a new game if one isn't being played.")


    if message.content.upper().startswith("-DL KEEP"):
        if message.author.nick != None:
            keeper = message.author.nick
        else:
            keeper = message.author.name
        if keeper == playersTurn:
            if playersTurn == player1name or playersTurn == player2name or playersTurn == player3name:
                if playersTurn == player1name:
                    player1total += currentTotal
                    if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                        if player1total >= diceluckGoal:
                            dlwinTotal = player1total
                            dlWinner = player1name
                        if player2total >= diceluckGoal:
                            dlwinTotal = player2total
                            dlWinner = player2name
                        if player3total >= diceluckGoal:
                            dlwinTotal = player3total
                            dlWinner = player3name
                        await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                    if player2name != 0:
                        playersTurn = player2name
                    else:
                        playersTurn = player3name
                    await bot.send_message(message.channel, "Your score is now **" + str(player1total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")

                elif playersTurn == player2name:
                    player2total += currentTotal
                    if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                        if player1total >= diceluckGoal:
                            dlwinTotal = player1total
                            dlWinner = player1name
                        if player2total >= diceluckGoal:
                            dlwinTotal = player2total
                            dlWinner = player2name
                        if player3total >= diceluckGoal:
                            dlwinTotal = player3total
                            dlWinner = player3name
                        await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                    if player3name != 0:
                        playersTurn = player3name
                    else:
                        playersTurn = player1name
                    await bot.send_message(message.channel, "Your score is now **" + str(player2total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")

                elif playersTurn == player3name:
                    player3total += currentTotal
                    if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                        if player1total >= diceluckGoal:
                            dlwinTotal = player1total
                            dlWinner = player1name
                        if player2total >= diceluckGoal:
                            dlwinTotal = player2total
                            dlWinner = player2name
                        if player3total >= diceluckGoal:
                            dlwinTotal = player3total
                            dlWinner = player3name
                        await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                    if player1name != 0:
                        playersTurn = player1name
                    else:
                        playersTurn = player2name
                    await bot.send_message(message.channel, "Your score is now **" + str(player3total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")


                else:
                    await bot.send_message(message.channel, "Are you even in a game **" + message.author.name + "**?")


        else:
            await bot.send_message(message.channel, "If it isn't your turn or you aren't in this game, please don't try to interfere.")

    if message.content.upper().startswith("-DL NO"):
        if message.author.nick != None:
            nextRoller = message.author.nick
        else:
            nextRoller = message.author.name
        if nextRoller == playersTurn:
            numbOfDice = 5
            currentTotal = 0
            await bot.send_message(message.channel, "Use `-DL Roll` to take your turn now.")
        else:
            await bot.send_message(message.channel, "If it isn't your turn or you aren't in this game, please don't try to interfere.")

    if message.content.upper().startswith("-DL GOAL"):
        if message.author.nick != None:
            goaler = message.author.nick
        else:
            goaler = message.author.name
        dlArgs = message.content.split(" ")
        goalArg = int(dlArgs[2])
        if starttestgame == 0:
            if goaler == player1name or goaler == player2name or goaler == player3name:
                if 100 <= goalArg <= 1000:
                    diceluckGoal = goalArg
                    await bot.send_message(message.channel, "The goal for this game has been set to **" + str(diceluckGoal) + "** by **" + goaler + "**!")
                else:
                    await bot.send_message(message.channel, "Please set a reasonable goal between 100 and 1000")
            else:
                await bot.send_message(message.channel, "You are not qued in the game.")
        else:
            await bot.send_message(message.channel, "The game is already in progress, the goal cannot be changed.")

    if message.content.upper().startswith("-DL SCORE"):
        if starttestgame == 1:
            if player1name == 0:
                await bot.send_message(message.channel, "**" + player2name + "** has " + str(player2total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
            if player2name == 0:
                await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
            if player3name == 0:
                await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
            else:
                await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points, **" + player2name + "** has " + str(player2total) + " points, and **" + player3name + "** has " + str(player3total) + " points!")
        else:
            await bot.send_message(message.channel, "There is no game in progress.")


    #MASTERMIND GAME!!!
    if message.content.upper().startswith("-MASTERMIND"):
        global combo
        global mmplayer
        if mmplayer != 0:
            await bot.send_message(message.channel, "Please wait until the current game is finished")
        else:
            if message.author.nick != 0:
                mmplayer = message.author.nick
            elif message.author.nick == 0:
                mmplayer = message.author.name
            numbs = ["1", "2", "3", "4", "5", "6"]
            n1 = random.choice(numbs)
            n2 = random.choice(numbs)
            n3 = random.choice(numbs)
            combo = n1 + n2 + n3
            await bot.send_message(message.channel, "Guess the three numbers in the correct order. You have six attempts, and the numbers range from one to six. Good luck!")
            await bot.send_message(message.channel, "The following symbols indicate whether you have a correct number in the correct position, a correct number in the incorrect position, and/or an incorrect number.")
            await bot.send_message(message.channel, """:black_large_square: : Incorrect Number
:white_square_button: : Correct Number, Wrong position
:white_large_square: : Correct Number, Correct Position""")
            await bot.send_message(message.channel, "NOTE: The order of the bot's responces to your guesses do not line up to show you which numbers ar correct. They only show you if any of them are correct in no specific order!")

    if message.content.upper().startswith("-MM"):
        if message.author.nick != 0:
            mmMessager = message.author.nick
        elif message.author.nick == 0:
            mmMessager = message.author.name
        if combo == 0:
            await bot.send_message(message.channel, "Please start a new game with -MasterMind")
        else:
            if mmMessager == mmplayer:
                global guessNum
                guessNum += 1
                args = message.content.split(" ")
                newargs = str(args[1])
                if newargs == combo:
                    await bot.send_message(message.channel, ":white_large_square:" * 3)
                    await bot.send_message(message.channel, "You win! The answer was %s"%(combo))
                    if guessNum == 1:
                        resp = "1 guess!"
                    else:
                        resp = "%s guesses!"%(str(guessNum))
                    await bot.send_message(message.channel, "It took you %s"%(resp))
                    guessNum = 0
                    combo = 0
                    mmplayer = 0

                sepnum = list(newargs)
                setnumbs = list(combo)

                    #Calculate the matching numbers AND positions using THIS thing: calcMatches()
                n1 = setnumbs[0]
                n2 = setnumbs[1]
                n3 = setnumbs[2]
                m1 = sepnum[0]
                m2 = sepnum[1]
                m3 = sepnum[2]



                totalExactMatches = 0
                totalMatches = 0
                nonMatches = 0

                    #Check if ANY numbers are equal first

                if n1 == m1 or n1 == m2 or n1 == m3:
                    if n1 == m1:
                        totalExactMatches += 1
                    else:
                        totalMatches += 1
                else:
                    nonMatches += 1

                if n2 == m1 or n2 == m2 or n2 == m3:
                    if n2 == m2:
                        totalExactMatches += 1
                    else:
                        totalMatches += 1
                else:
                    nonMatches += 1

                if n3 == m1 or n3 == m2 or n3 == m3:
                    if n3 == m3:
                        totalExactMatches += 1
                    else:
                        totalMatches += 1
                else:
                    nonMatches += 1


                await bot.send_message(message.channel, ":white_large_square:" * totalExactMatches + ":white_square_button:" * totalMatches + ":black_large_square:" * nonMatches)


                await bot.send_message(message.channel, "You have " + str(6 - int(guessNum)) + " guesses left!")
                if guessNum == 6:
                    await bot.send_message(message.channel, "Sorry, you're out of guesses! The answer was %s"%(combo))
                    guessNum = 0
                    combo = 0
                    mmplayer = 0




            else:
                await bot.send_message(message.channel, "You are not the current player. Please wait until **" + mmplayer + "** finishes his/her game.")

    if message.content.upper().startswith("-BOTHELP"):
        em = discord.Embed(title="BotHelp", description=bothelpMessage, colour=0xBCAD20)
        em.set_author(name=bot.user, icon_url=bot.user.avatar_url)
        await bot.send_message(message.author,content=None, embed=em)
        await bot.add_reaction(message, "\N{Eyes}")

        #await bot.send_message(message.channel, """``````""")




    if message.content.upper().startswith("-TTT") or message.content.upper().startswith("-TICTACTOE"):
        global tttP1
        global tttP2
        global ttt1
        global ttt2
        global ttt3
        global ttt4
        global ttt5
        global ttt6
        global ttt7
        global ttt8
        global ttt9
        global tttStart
        global tttPTurn
        global tttRow1
        global tttRow2
        global tttRow3
        global tttBoard
        global tttTimer
        global tttTimerStop
        global when_to_stop

        resetTTT = message.content.upper()[5:10]

        if resetTTT == "RESET":
            tttP1 = 0
            tttP2 = 0
            ttt1 = tttBlank
            ttt2 = tttBlank
            ttt3 = tttBlank
            ttt4 = tttBlank
            ttt5 = tttBlank
            ttt6 = tttBlank
            ttt7 = tttBlank
            ttt8 = tttBlank
            ttt9 = tttBlank
            tttWinner = 0
            tttStart = 0
            await bot.send_message(message.channel, "The game has been reset!")
        else:
            if message.author.nick == None:
                tttJoiner = message.author.name
            else:
                tttJoiner = message.author.nick
            if tttP1 == 0:
                if tttJoiner != tttP2:
                    tttP1 = tttJoiner
                    tttTimer = 0
                    tttTime = 0
                    tttTimer = 1
                    await bot.send_message(message.channel, "Welcome to TicTacToe **" + tttP1 + "**!")

            elif tttP2 == 0:
                if tttJoiner != tttP1:
                    tttP2 = tttJoiner
                    tttTimer = 0
                    tttTime = 0
                    tttTimerStop = 1
                    when_to_stop = 0
                    await bot.send_message(message.channel, "Welcome to TicTacToe **" + tttP2 + "**!")

            else:
                await bot.send_message(message.channel, "Please wait for the current game to finish.")

            #if tttTimer == 0:
            #    tttTimer = 1
            #    time.time()




            if tttP1 != 0 and tttP2 != 0:
                tttStart = 1
                await bot.send_message(message.channel, "Let's begin **" + tttP1 + "** and **" + tttP2 + "**!")
                tttPlayers = [tttP1,tttP2]
                tttPTurn = random.choice(tttPlayers)
                await bot.send_message(message.channel, "**" + tttPTurn + "** may begin! Remember, use the numbers **1-9** to mark a position!" + tttLayout)
                #SHOW THE BLANK BOARD HERE!!!


#    if message.content.upper().startswith("-TIME"):
#        #global tttTimer
#        tttTimer = 1
#        #Time = time.time()
#        #tttTimer = 0
#        await bot.send_message(message.channel, "TEST TIME")
#        when_to_stop = 10
#        while when_to_stop > 0:
#            if message.content.upper().startswith("-STOP"):
#                when_to_stop = 0
#            #await bot.send_message(message.channel, str(when_to_stop))
#            when_to_stop -= 1

    if tttTimer == 1:
        if tttTime == 0:
            #Time = time.sleep(5)



            when_to_stop = 30
            time_left_msg = await bot.send_message(message.channel, "Time left for another player to join: " + str(when_to_stop))

            while when_to_stop > 0:
                if tttTimerStop == 0:
                    await bot.edit_message(time_left_msg, new_content="Time left for another player to join: " + str(when_to_stop))
                    when_to_stop -= 1
                    time.sleep(1)
                else:
                    pass

            if tttTimerStop == 0:
                tttTimer = 0
                tttP1 = 0
                tttP2 = 0
                ttt1 = tttBlank
                ttt2 = tttBlank
                ttt3 = tttBlank
                ttt4 = tttBlank
                ttt5 = tttBlank
                ttt6 = tttBlank
                ttt7 = tttBlank
                ttt8 = tttBlank
                ttt9 = tttBlank
                tttWinner = 0
                tttStart = 0
                await bot.edit_message(time_left_msg, "TicTacToe que has timed out!")


    if message.content.upper().startswith("1") or message.content.upper().startswith("2") or message.content.upper().startswith("3") or message.content.upper().startswith("4") or message.content.upper().startswith("5") or message.content.upper().startswith("6") or message.content.upper().startswith("7") or message.content.upper().startswith("8") or message.content.upper().startswith("9"):
        x1 = ":regional_indicator_x:"
        o1 = ":regional_indicator_o:"
        if tttStart == 1:
            #await bot.send_message(message.channel, "TEST")
            if message.author.nick == None:
                tttmessager = message.author.name
            else:
                tttmessager = message.author.nick

            if tttmessager == tttPTurn:
                tttNumber = str(message.content[0])
                #await bot.send_message(message.channel, tttNumber)
                if tttNumber == "1":
                    if ttt1 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt1 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt1 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "2":
                    if ttt2 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt2 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt2 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "3":
                    if ttt3 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt3 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt3 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "4":
                    if ttt4 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt4 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt4 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "5":
                    if ttt5 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt5 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt5 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "6":
                    if ttt6 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt6 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt6 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "7":
                    if ttt7 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt7 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt7 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "8":
                    if ttt8 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt8 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt8 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                elif tttNumber == "9":
                    if ttt9 == tttBlank:
                        if tttPTurn == tttP1:
                            ttt9 = x1
                            tttTurnComplete = 1
                        elif tttPTurn == tttP2:
                            ttt9 = o1
                            tttTurnComplete = 1
                    else:
                        await bot.send_message(message.channel, "Please choose an available space")
                else:
                    await bot.send_message(message.channel, "Didn't work: " + tttNumber + "-" + x1 + o1 + ttt1)


                if ttt1 == ttt2 == ttt3 == x1 or ttt1 == ttt2 == ttt3 == o1 or ttt4 == ttt5 == ttt6 == x1 or ttt4 == ttt5 == ttt6 == o1 or ttt7 == ttt8 == ttt9 == x1 or ttt7 == ttt8 == ttt9 == o1 or ttt1 == ttt4 == ttt7 == x1 or ttt1 == ttt4 == ttt7 == o1 or ttt2 == ttt5 == ttt8 == x1 or ttt2 == ttt5 == ttt8 == o1 or ttt3 == ttt6 == ttt9 == x1 or ttt3 == ttt6 == ttt9 == o1 or ttt1 == ttt5 == ttt9 == x1 or ttt1 == ttt5 == ttt9 == o1 or ttt3 == ttt5 == ttt7 == x1 or ttt3 == ttt5 == ttt7 == o1:
                    tttWinner = tttPTurn
                elif ttt1 != tttBlank and ttt2 != tttBlank and ttt3 != tttBlank and ttt4 != tttBlank and ttt5 != tttBlank and ttt6 != tttBlank and ttt7 != tttBlank and ttt8 != tttBlank and ttt9 != tttBlank:
                    tttWinner = "No one"


                if tttTurnComplete == 1:
                    if tttPTurn == tttP1:
                        tttPTurn = tttP2
                    elif tttPTurn == tttP2:
                        tttPTurn = tttP1
                tttTurnComplete = 0

                tttRow1 = ttt1+ttt2+ttt3
                tttRow2 = ttt4+ttt5+ttt6
                tttRow3 = ttt7+ttt8+ttt9
                tttBoard = tttRow1 + """
""" + tttRow2 + """
""" + tttRow3

                em = discord.Embed(title="TicTacToe", description=tttBoard,colour=0xBCAD20)
                em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await bot.send_message(message.channel, content=None, embed=em)

                if tttWinner != 0:
                    await bot.send_message(message.channel, "**%s** wins! Another game is ready to be played!"%(tttWinner))
                    tttP1 = 0
                    tttP2 = 0
                    ttt1 = tttBlank
                    ttt2 = tttBlank
                    ttt3 = tttBlank
                    ttt4 = tttBlank
                    ttt5 = tttBlank
                    ttt6 = tttBlank
                    ttt7 = tttBlank
                    ttt8 = tttBlank
                    ttt9 = tttBlank
                    tttWinner = 0
                    tttStart = 0
                    tttTime = 0
                    tttTimer = 0
                    tttTimerStop = 0





    #WordGuess
    if message.content.upper().startswith("-WORDGUESS"):
        opt = random.choice(words)
        global word
        word = opt[0]
        jumble = ""
        unscram = opt[1]
        def scrambled(unscram):
            l = list(unscram)
            random.shuffle(l)
            return ''.join(l)

        await bot.send_message(message.channel, scrambled(unscram))

    if message.content.upper().startswith(word):
        if message.author.name != bot.user.name:
            await bot.send_message(message.channel, "You win! the word was " + (word))
            opt = random.choice(words)
            word = opt[0]
            jumble = ""
            unscram = opt[1]
            def scrambled(unscram):
                l = list(unscram)
                random.shuffle(l)
                return ''.join(l)

            await bot.send_message(message.channel, scrambled(unscram))






    await bot.process_commands(message)


#@bot.command(pass_context=True)
#async def ping(ctx):
#    await bot.say(":ping_pong: Pong!")


@bot.command(pass_context=True)
#The command -userinfo needs a mentioned user.
#FIX WHEN NO NAME IS ENTERED
async def userinfo(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    await bot.say("This user's username is {}".format(user.name))
    if user.nick != None:
        await bot.say(user.name + "'s nickname here is {}".format(user.nick))
    await bot.say("Status: {}".format(user.status))
    await bot.say("Highest role: {}".format(user.top_role))
    await bot.say("Joined: {}".format(user.joined_at))
    if user.game == None:
        await bot.say(user.name + " isn't playing anything... how sad")
    elif user.game != None:
        await bot.say('"Playing {}"'.format(user.game))
        await bot.say("Mind if I join you?")


#@bot.command(pass_context=True)
##This will be used for bringing the bot to a voice channel.
#async def summon(ctx):
#    await bot.say("I will join you when you let me")
#    join_voice_channel(General)



@bot.command(pass_context=True)
async def joined(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await bot.say('{0} joined at {0.joined_at}'.format(member))








bot.run("TOKEN")

print("nexascain.exe has started successfully!")
