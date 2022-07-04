# owrpcconfig.py | Overwatch RPC Client Configuration
# https://www.github.com/maxicc/owrpc

class configs():
    """
    Configurations relating to the program itself.
    Should not be changed by users.
    """

    client = 993216825611518112
    ver = "2.0.0.beta"
class maps():
    """
    Map-related configurations. Must be updated as new maps come out!
    Should not be changed by users.

    The formatting for modes is as follows:
    "short-mode-name": ["Full Mode Name","mapset"]

    The formatting for maps is as follows:
    "short-map-name": ["Full Map Name","type","discord-key"]
    """
    modes = {
        #"competitive": ["Competitive","standard"],
        "quick": ["Quick Play","standard"],
        #"arcade": ["Arcade","any"],
        "custom": ["Custom Game","any"]
    }

    # [Second] OW 2 Beta maps
    # TODO: Add back all available maps so this works for OW 1
    standard = {
        # Control
        "busan": ["Busan","Control","https://static.wikia.nocookie.net/overwatch_gamepedia/images/0/09/Overwatch_Busan.jpg/revision/latest/scale-to-width-down/1024?cb=20190412043201"],
        "ilios": ["Ilios","Control","https://static.wikia.nocookie.net/overwatch_gamepedia/images/4/45/Ilios.jpg/revision/latest/scale-to-width-down/1024?cb=20180520062425"],
        "lijiang": ["Lijiang Tower","Control","https://static.wikia.nocookie.net/overwatch_gamepedia/images/9/9b/Lijiang_Tower_loading_screen.jpg/revision/latest/scale-to-width-down/1024?cb=20180520062020"],
        "nepal": ["Nepal","Control","https://static.wikia.nocookie.net/overwatch_gamepedia/images/f/f3/Nepal_loading_screen.jpg/revision/latest/scale-to-width-down/1024?cb=20190412043102"],
        "oasis": ["Oasis","Control","https://static.wikia.nocookie.net/overwatch_gamepedia/images/f/fc/Oasis.jpg/revision/latest/scale-to-width-down/1024?cb=20180520062749"],
        # Escort
        "circuitroyal": ["Circuit Royal", "Escort", "https://static.wikia.nocookie.net/overwatch_gamepedia/images/1/10/Monte_Carlo.jpg/revision/latest/scale-to-width-down/1024?cb=20191101204803"],
        "dorado": ["Dorado","Escort","https://static.wikia.nocookie.net/overwatch_gamepedia/images/e/ec/Dorado-streets2.jpg/revision/latest/scale-to-width-down/1024?cb=20180520045217"],
        "junkertown": ["Junkertown","Escort","https://static.wikia.nocookie.net/overwatch_gamepedia/images/e/e3/Junkertown.jpg/revision/latest/scale-to-width-down/1024?cb=20170822090741"],
        "route66": ["Route 66","Escort","https://static.wikia.nocookie.net/overwatch_gamepedia/images/a/a6/Route_66.jpg/revision/latest/scale-to-width-down/1024?cb=20180520050707"],
        "watchpoint": ["Watchpoint: Gibraltar","Escort","https://static.wikia.nocookie.net/overwatch_gamepedia/images/8/8b/Gibraltar.jpg/revision/latest/scale-to-width-down/1024?cb=20180520050120"],
        "gibraltar": ["Watchpoint: Gibraltar","Escort","https://static.wikia.nocookie.net/overwatch_gamepedia/images/8/8b/Gibraltar.jpg/revision/latest/scale-to-width-down/1024?cb=20180520050120"],
        # Hybrid
        "eichenwalde": ["Eichenwalde","Hybrid","https://static.wikia.nocookie.net/overwatch_gamepedia/images/a/aa/Eichenwalde.png/revision/latest/scale-to-width-down/1024?cb=20190412043329"],
        "hollywood": ["Hollywood","Hybrid","https://static.wikia.nocookie.net/overwatch_gamepedia/images/2/26/Hollywood-set.jpg/revision/latest/scale-to-width-down/1024?cb=20190506201443"],
        "kingsrow": ["King's Row","Hybrid","https://static.wikia.nocookie.net/overwatch_gamepedia/images/1/1b/King%27s_Row_concept.jpg/revision/latest/scale-to-width-down/1024?cb=20180520052818"],
        "midtown": ["Midtown","Hybrid","https://static.wikia.nocookie.net/overwatch_gamepedia/images/4/4e/N18S6DCTDPG81613669123002.png/revision/latest/scale-to-width-down/1024?cb=20210221175110"],
        "paraiso": ["Paraíso","Hybrid","https://static.wikia.nocookie.net/overwatch_gamepedia/images/9/90/Para%C3%ADso_pvp.jpg/revision/latest/scale-to-width-down/1024?cb=20220630025520"],
        # Push
        "colosseo": ["Colosseo","Push","https://static.wikia.nocookie.net/overwatch_gamepedia/images/1/1e/Blizzconline_rome_01.png/revision/latest/scale-to-width-down/1024?cb=20210220013006"],
        "newqueenstreet": ["New Queen Street","Push","https://static.wikia.nocookie.net/overwatch_gamepedia/images/9/91/Toronto.jpg/revision/latest/scale-to-width-down/1024?cb=20191101212447"]
    }

    arcade = {
        "blackforest": ["Black Forest","Arcade","black-forest"],
        "castillo": ["Castillo","Arcade","castillo"],
        "antarctica": ["Ecopoint: Antarctica","Arcade","ecopoint-antarctica"],
        "necropolis": ["Necropolis","Arcade","necropolis"],
        "chateau": ["Château Guillard","Arcade","chateau"],
        "petra": ["Petra","Arcade","petra"],
        "ayutthaya": ["Ayutthaya","Arcade","ayutthaya"],
        "seasonal": ["Seasonal Event","Seasonal","overwatch"]
    }

    roles = {
        "tank": ["Tank","https://i.imgur.com/QHyTbTb.png"],
        "heal": ["Support","https://i.imgur.com/aQTklud.png"],
        "dps": ["DPS","https://i.imgur.com/SwqWWHC.png"],
        "open": ["Open Queue", "https://i.imgur.com/ngkat9U.png"]
    }
