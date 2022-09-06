def tournamentWinner(competitions, results):
    # Write your code here.
    dict1 = {}
    for i in range(len(competitions)):
        dict1[competitions[i][0]] = 0
        dict1[competitions[i][1]] = 0
    for i in range(len(results)):
        if results[i] == 0:
            dict1[competitions[i][1]] = dict1.get(competitions[i][1]) + 3
        if results[i] == 1:
            dict1[competitions[i][0]] = dict1.get(competitions[i][0]) + 3
    winner = max(dict1, key=dict1.get)
    return winner
