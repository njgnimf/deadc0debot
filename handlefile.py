def handle(msg, bot, reimport):
    import json
    import telepot
    import time
    botid = "@Deadc0deBot"
    botid = botid.lower()
    banamount = 10
    #print("reloaded")
    #print(msg)
    #json.dump(msg, open("dump" + str(time.clock()) + ".txt", "w"))
    def limit(derwert, daslimit):
        if(derwert >= daslimit):
            return daslimit
        else:
            return derwert
    
    try:
        users = json.load(open("users.json"))
    except:
        users = {"nobody" : "0"}
        print("fehler 1")
    try:
        print(msg["from"]["username"] + " : " + str(msg["from"]["id"]))
        if(not msg["from"]["username"] in users):
            users[msg["from"]["username"]] = msg["from"]["id"]
    except:
        print("fehler 2 (Er hat keinen Nutzernamen)")
    try:
        json.dump(users, open("users.json", "w"))
        id = msg["chat"]["id"]
    except:
        print("fehler 3")
    #id = msg["from"]["id"]
    realtext = msg["text"]
    command = msg["text"].lower().split(" ")[0]
    if("entities" in msg and msg["entities"][0]["type"] == "bot_command" and command[0] == "/"):
        if(True):
            if(command == "/help" or command == "/help" + botid):
                bot.sendMessage(id, """These are the commands, we actually have:
                /help - show this
                /reload - get the newest handling file
                /tutorial /needtutorial - learn hacking
                /source - show a Link to the source of the bot
                /web - show a Link to the Web page
                /gidf - You know what?
                /voteban @user - be evil and ban an evil user""")
            elif(command == "/reload" or command == "/reload" + botid):
                return reimport(id)
            elif(command == "/tutorial" or command == "/tutorial" + botid or command == "/needtutorial" or command == "/needtutorial" + botid):
                try:
                    bot.sendMessage(id, open("tutorial.txt").read())
                except:
                    print("fehler 4")
            elif(command == "/source" or command == "/source" + botid):
                bot.sendMessage(id, "https://github.com/De4dc0de/deadc0debot")
            elif(command == "/penis" or command == "/penis" + botid):
                try:
                    bot.sendMessage(id, "<" + "=" * limit(int(realtext.split(" ")[1]), 500) + "3")
                except:
                    bot.sendMessage(id, "<====3")
            elif(command == "/love" or command == "/love" + botid):
                bot.sendMessage(id, "<3")
            elif(command == "/web" or command == "/web" + botid):
                bot.sendMessage(id, "http://deadc0de.bplaced.net")
            elif(command == "/gidf" or command == "/gidf" + botid):
                bot.sendMessage(id, "http://gidf.de")
            elif(command == "/voteban" or command == "/voteban" + botid):
                try:
                    bandict = json.load(open("bandict.json"))
                except:
                    bandict = {"lastuser" : "nobody", "nobody" : 0}
                if(True): #Hier Ueberpruefung der einfachen Abstimmung einfuegen
                    try:
                        banuser = realtext.split(" ")[1].split("@")[1]
                        if(banuser in users):
                            #print(bot.getChat(id))
                            if(not banuser in bandict):
                                bandict[banuser] = 1
                            else:
                                bandict[banuser] = bandict[banuser] + 1
                            bandict["lastuser"] = banuser
                            bot.sendMessage(id, "Voteban " + banuser + " " + str(bandict[banuser]) + "/" + str(banamount))
                    except:
                        #print(bandict["lastuser"])
                        banuser = bandict["lastuser"]
                        bandict[banuser] = bandict[banuser] + 1
                        #print("debug2")
                        bot.sendMessage(id, "Voteban " + banuser + " " + str(bandict[banuser]) + "/" + str(banamount))
                        #print("debug3")
                    if(bandict[banuser] >= banamount):
                        try:
                            kickChatMember(id, user[banuser])
                        except:
                            bot.sendMessage(id, "Admin, verbanne @" + banuser + " aus diesem Chat! Dieser Bot ist kein Admin!")
                            bandict[banuser] = 0
                else:
                    bot.sendMessage(id, "Placeholda Contaent")
                json.dump(bandict, open("bandict.json", "w"))
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
            
    else:
        try:
            if("xD" in msg["text"]):
                bot.sendMessage(id, u'\U0001f606')
        except:
            pass
