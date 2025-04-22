import sports

def retrieve_results(sport):
    return sports.get_sport(sport)

if __name__ == '__main__':
    # all_matches = retrieve_results(sports.BASKETBALL)
    # print(all_matches)
    sixers = sports.get_team_info(sports.BASKETBALL, '76ers')
    print(sixers.playoff_app)