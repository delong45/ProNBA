import requests
import nba
import display

if __name__ == '__main__':
    
    url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
         'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
         'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
         'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
         'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&Plu'\
         'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
         'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
         'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
         'owZones=0'
    
    stats = nba.Stats(url)
    response = stats.request()
    headers = response.json()['resultSets'][0]['headers']
    shots = response.json()['resultSets'][0]['rowSet']

    df = display.Dataframe(shots, headers)
    df.display()
