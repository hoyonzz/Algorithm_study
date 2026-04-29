from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    now_bridge = 0
    while bridge:
        time += 1
        now_bridge -= bridge.popleft()
        if truck_weights:
            if now_bridge + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                now_bridge += truck
                bridge.append(truck)
            else:
                bridge.append(0)
        
            
    return time