def handshakes(n):
    return n * (n - 1) // 2


test_cases = int(input())
for _ in range(test_cases):
    attendees = int(input())
    result = handshakes(attendees)
    print(result)
