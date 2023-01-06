from constants import sh_kom


def get_kicked():
    kick_sheet = sh_kom.get_worksheet(1).get("A1:A50")
    kick_players = []
    for player in kick_sheet:
        kick_players.append(player[0])
    return kick_players
