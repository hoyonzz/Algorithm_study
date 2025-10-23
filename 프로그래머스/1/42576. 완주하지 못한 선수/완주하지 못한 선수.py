from collections import defaultdict
def solution(participant, completion):
    runners = defaultdict(int)
    for runner in participant:
        runners[runner] += 1
    for runner in completion:
        runners[runner] -= 1
    for runner, i in runners.items():
        if runners[runner] == 1:
            return runner
