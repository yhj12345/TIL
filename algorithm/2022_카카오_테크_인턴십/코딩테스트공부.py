def solution(alp, cop, problems):
    answer = 0
    goal_alp = 0
    goal_cop = 0
    for problem in problems:
        goal_alp = max(goal_alp, problem[0])
        goal_cop = max(goal_cop, problem[1])
        
    INF = 1000000
    dp = [[INF for _ in range(goal_cop+1)] for _ in range(goal_alp+1)]
    alp = min(alp, goal_alp)
    cop = min(cop, goal_cop)
    dp[alp][cop] = 0
    

    for i in range(alp, goal_alp+1):
        for j in range(cop, goal_cop+1):
            if i+1 <= goal_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j+1 <= goal_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:
                    next_alp = min(goal_alp, i + problem[2])
                    next_cop = min(goal_cop, j + problem[3])
                    dp[next_alp][next_cop] = min(dp[i][j] + problem[4], dp[next_alp][next_cop])
    answer = dp[goal_alp][goal_cop]

    return answer

print(solution(1, 1, [[20,18,6,3,2],[10,15,5,3,4],[1,1,1,1,1]]))