# owrpc.py | Overwatch RPC Client
# https://www.github.com/maxicc/owrpc
try:
    ### - IMPORTS AND MAIN SETUP - ###

    # Importing default Python modules
    import time
    import sys
    import random
    import os
    import platform

    try:
        # Importing custom project-specific modules
        import requests
        from owrpcconfig import configs as x
        from owrpcconfig import maps as m
        # Importing pypresence
        from pypresence import Presence

    # If imports didn't work...
    except Exception as e:
        # Warn the user that the modules can't be imported then exit with error code 1
        print("[!] Error! Couldn't import a module. Did you download the dependencies (requests and pypresence)?")
        print("[!] Check the instructions at git.io/owrpc and make sure, then try running again.")
        print("[!] If you need more help, join the Discord at discord.gg/keErGbZ and show this to maxic:")
        print(str(e))
        sys.exit(1)

    os.chdir(os.path.dirname(sys.argv[0]))

    # If there is a file in this directory called ".nocol"
    if os.path.isfile(".nocol") or os.path.isfile(".NOCOL"):
        # Import a different version of the prefixes module that removes the ANSI colours
        from mansi import nocolours as c
    else:
        # Import the normal colours module
        if platform.platform() == "Windows":
            print("[!] It looks like you're using Windows, but you didn't disable ANSI colours!")
            print("[!] If the text below looks weird, create a file called .NOCOL in the same directory as owrpc.py to stop this.")
            print("[!] If it doesn't look weird to you, congratulations on not using the Windows terminal.")
        from mansi import colours as c

    # Initialise the Discord Presence using pypresence then connect to Discord
    dp = Presence(x.client)
    dp.connect()

    # Define the status class

    class status():
        ingame = 0
        devmode = False
        currmap = ''
        currmode = ''
        presets = {
            "example":["details","state","overwatch","large_text","overwatch-dark","small_text"],
            "inmenus":["In Menus",None,"overwatch","owrpc v" + x.ver + " by maxic#9999! git.io/owrpc",None,None],
            "inqueue":["In Queue",None,"overwatch","owrpc v" + x.ver + " by maxic#9999! git.io/owrpc",None,None],
            "inqueue-comp":["Competitive: In Queue",None,"overwatch","owrpc v" + x.ver + " by maxic#9999! git.io/owrpc",None,None],
            "inqueue-quick":["Quick Play: In Queue",None,"overwatch","owrpc v" + x.ver + " by maxic#9999! git.io/owrpc",None,None],
            "inqueue-arcade":["Arcade: In Queue",None,"overwatch","owrpc v" + x.ver + " by maxic#9999! git.io/owrpc",None,None],
            "devmode":["Overwatch RPC Client","I'm being programmed!","maxic","Created by maxic#9999","overwatch","Under development!"]
        }

    ### - DEFINE FUNCTIONS - ###

    def buildList(source):
        list = ''
        for x in source.keys():
            if list == '':
                list = "'" + x + "'"
            else:
                list = list + ", '" + x + "'"
        return list

    def clearPresence():
        try:
            dp.clear()
        except Exception as e:
            print(c.fail + "Couldn't clear your presence! :(")
            print(c.fail + "The error message from pypresence is: " + str(e))
            sys.exit(1)
        print(c.success + "Your presence has been cleared! Discord may take a few seconds to update.")

    def devMode():
        """
        This function will toggle the value of status.devmode when called.
        status.devmode starts as False.
        """
        status.devmode = not status.devmode

        if status.devmode == True:
            print(c.success + "Enabled development mode. Be afraid!")
            clearPresence()
        else:
            print(c.success + "Disabled development mode... you can relax now.")
            clearPresence()

    def showGreeting():
        print(c.smile + "Overwatch RPC Client v" + x.ver + " by github.com/maxicc (maxic#9999)")
        onlver = requests.get("https://maxicc.github.io/owrpc/VERSION.txt").text.rstrip()
        if x.ver != onlver:
            print(c.warn + "You're out-of-date! The latest version on GitHub is " + str(onlver) + " and you're on " + x.ver + ".")
            print(c.warn + "Time to update! Clone the git repo again or redownload the files from git.io/owrpc.")
        else:
            print(c.success + "You're up-to-date! Thanks for using the latest version.")
        print(c.info + "Need help? Want a new feature? Join the Discord at discord.gg/keErGbZ")
        print(c.info + "...or open an issue on the GitHub page at git.io/owrpc!")
        print(c.blank + random.choice(owquotes))

    def setupGame():
        modes = buildList(m.modes)
        print(c.info + "What gamemode are you playing?")
        print(c.info + "Your options are: " + modes)
        user = input(c.ask)
        mode = ["","",""]
        while mode == ["","",""]:
            if user not in modes:
                print(c.fail + "That's not a valid mode. Your options are: " + modes)
                user = input(c.ask)
            else:
                mode[0] = user # Config file key
                mode[1] = m.modes[user][0] # Friendly mode name
                mode[2] = m.modes[user][1] # Map set used
                print(str(mode))

        if mode[2] == "standard":
            maps = buildList(m.standard)
        elif mode[2] == "any":
            maps = buildList(m.standard) + ", " + buildList(m.arcade)
        else:
            print(c.fail + "Something unexpected went wrong! Please report this at git.io/owrpc or discord.gg/keErGbZ and say you hit point 1.")
            print(c.info + "If you try and do whatever you were trying to do again, it should work. Hopefully. Sorry about that.")

        print(c.info + "What map are you playing on?")
        print(c.info + "Your options are: " + maps)
        user = input(c.ask)
        map = ["","","",""]
        while map == ["","","",""]:
            if (mode[2] == "standard" and user not in m.standard) or (mode[2] == "any" and user not in m.standard and user not in m.arcade):
                print(c.fail + "That's not a valid map. Please try again!")
                user = input(c.ask)
            elif (mode[2] == "standard" and user in m.standard) or (mode[2] == "any" and user in m.standard):
                map[0] = user # Config file key
                map[1] = m.standard[user][0] # Friendly map name
                map[2] = m.standard[user][1] # Map mode
                map[3] = m.standard[user][2] # Image key
                print(str(map))
            elif mode[2] == "any" and user in m.arcade:
                map[0] = user # Config file key
                map[1] = m.arcade[user][0] # Friendly map name
                map[2] = m.arcade[user][1] # Map mode
                map[3] = m.arcade[user][2] # Image key
                print(str(map))
            else:
                print(c.fail + "Something unexpected went wrong! Please report this at git.io/owrpc or discord.gg/keErGbZ and say you hit point 2.")
                print(c.info + "If you try and do whatever you were trying to do again, it should work. Hopefully. Sorry about that.")

        if mode[0] == "competitive":
            print(c.info + "What is your skill rating (SR)?")
            user = input(c.ask)
            sr = [0,""]
            while sr == [0,""]:
                try:
                    if user == "<500":
                        sr = [user,"bronze"]
                    else:
                        user = int(user)
                        if user < 1 or user > 5000:
                            raise ValueError
                        elif user < 1500:
                            if user < 500:
                                sr = ["<500","bronze"]
                            else:
                                sr = [user,"bronze"]
                        elif user < 2000:
                            sr = [user,"silver"]
                        elif user < 2500:
                            sr = [user,"gold"]
                        elif user < 3000:
                            sr = [user,"platinum"]
                        elif user < 3500:
                            sr = [user,"diamond"]
                        elif user < 4000:
                            sr = [user,"masters"]
                        else:
                            sr = [user,"grandmaster"]
                except Exception as e:
                    print(c.fail + "The SR you entered is invalid, so I'm going to set your SR to Bronze. You probably belong there anyway.")
                    sr = [-1,"bronze"]
                    print(str(e))

                setPresence(None,details=mode[1] + ': In Game',state=map[2] + ' on ' + map[1],large_image=map[3],large_text=map[1],small_image=sr[1],small_text=str(sr[0]) + ' SR')
        else:
            setPresence(None,details=mode[1] + ': In Game',state=map[2] + ' on ' + map[1],large_image=map[3],large_text=map[1],small_image="maxic",small_text="owrpc v" + x.ver + " by maxic#9999! git.io/owrpc")

    def setPresence(preset,details='',state='',large_image='',large_text='',small_image='',small_text=''):
        """
        This function sets the Discord Rich Presence.
        [details,state,large_image,large_text,small_image,small_text]
        """
        silent = 0
        if preset != None:
            if preset.endswith("_silent"):
                preset = preset[:-7]
                silent = 1

            details = status.presets.get(preset)[0]
            state = status.presets.get(preset)[1]
            large_image = status.presets.get(preset)[2]
            large_text = status.presets.get(preset)[3]
            small_image = status.presets.get(preset)[4]
            small_text = status.presets.get(preset)[5]

        if status.devmode == True:
            details = "DEV MODE | " + str(details)
        try:
            # Update the presence using the details provided when calling the function
            dp.update(details=details,state=state,large_image=large_image,large_text=large_text,small_image=small_image,small_text=small_text,start=int(time.time()))
        except Exception as e:
            # If there is an exception, inform the user then exit with error code 1
            print(c.fail + "Couldn't set your presence properly! :(")
            print(c.fail + "The error message from pypresence is: " + str(e))
            sys.exit(1)
        if silent == 0:
            print(c.success + "Your presence has been updated! Discord may take a few seconds to update.")
        else:
            pass

    def setupCustom():
        print(c.warn + "Here be dragons!")
        print(c.warn + "This is a more advanced version of the presence selector. The normal one (accessed through !game) should be easier for you.")
        print(c.warn + "To ignore a line, just hit Enter immediately and leave it blank.")
        print(c.blank)

        options = {
            "details":'',
            "state":'',
            "large_image":'',
            "large_text":'',
            "small_image":'',
            "small_text":''
        }
        print(c.info + '' + "Please enter your top line.")
        options["details"] = input(c.ask)
        print(c.info + '' + "Please enter your bottom line.")
        options["state"] = input(c.ask)
        print(c.info + "Please enter your large image key.")
        options["large_image"] = '' + input(c.ask)
        print(c.info + "Please enter your large image text.")
        options["large_text"] = '' + input(c.ask)
        print(c.info + "Please enter your small image key.")
        options["small_image"] = '' + input(c.ask)
        print(c.info + "Please enter your small image text.")
        options["small_text"] = '' + input(c.ask)

        for option in options:
            if options[option] == '':
                options[option] = None

        if options["large_image"] == None:
            options["large_image"] = "overwatch"

        setPresence(None,details=options["details"],state=options["state"],large_image=options["large_image"],large_text=options["large_text"],small_image=options["small_image"],small_text=options["small_text"])

    owquotes = ["Cheers, love! The cavalry's here!","¡Apagando las luces!","Look out world, Tracer's here!","Nerf this!","Fire in the hole!","Die, die, die!","Justice rains from above!","I will be your shield!","All systems buzzing!","What is that melody?","Your guardian angel.","Do you even lift?","Gotcha something!","This... is my will."]

    showGreeting()
    setPresence("inmenus_silent")

    while True:
        if status.devmode == True:
            print(c.warn + "Development mode is enabled. Remember to disable it when you're done!")
        command = input(c.cmd)

        if command.startswith("!dev"):
            devMode()

        elif command.startswith("!help"):
            showGreeting()
            print(c.warn + "MAINTENANCE COMMANDS")
            print(c.info + "!dev - Toggle development mode on or off.")
            print(c.info + "!help - View this help document.")
            print(c.info + "!quit - Close the program.")
            print(c.blank)
            print(c.warn + "PRESENCE COMMANDS")
            print(c.info + "!game - Start set up for a game.")
            print(c.info + "!custom - Set up a custom presence.")
            print(c.info + "!menus - Set your presence to In Menus.")
            print(c.info + "!queue [a/c/q] - Set your presence to In Queue for [a]rcade, [c]ompetitive or [q]uickplay.")
            print(c.info + "!clear - Remove your presence from Discord.")

        elif command.startswith("!quit"):
            sys.exit(0)

        elif command.startswith("!game"):
            setupGame()

        elif command.startswith("!custom"):
            setupCustom()

        elif command.startswith("!menus"):
            setPresence("inmenus")

        elif command.startswith("!queue"):
            params = command.split()
            try:
                params[1]
            except:
                setPresence("inqueue")
                continue

            if params[1].lower().startswith("c"):
                setPresence("inqueue-comp")
            elif params[1].lower().startswith("q"):
                setPresence("inqueue-quick")
            elif params[1].lower().startswith("a"):
                setPresence("inqueue-arcade")
            else:
                setPresence("inqueue")

        elif command.startswith("!clear"):
            clearPresence()

        else:
            print(c.fail + "Couldn't find that command! Do !help if you need a refresher, or check out the documentation at git.io/owrpc. Need help? Ask at discord.gg/keErGbZ.")
        pass
except KeyboardInterrupt:
    print()
    print(c.fail + "Got your CTRL+C! Exiting...")
    sys.exit(0)
