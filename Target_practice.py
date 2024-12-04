def calculate_points(t, test_cases):
   
    center_x, center_y = 4.5, 4.5

   
    ring_points = [5, 4, 3, 2, 1]

    results = []

    for case in test_cases:
        total_points = 0
        for i in range(10):
            for j in range(10):
                if case[i][j] == 'X': 
                    
                    distance = max(abs(i - center_x), abs(j - center_y))
                   
                    ring_index = int(distance)  
                    if ring_index < 5: 
                        total_points += ring_points[ring_index]
        results.append(total_points)

    return results



t = int(input()) 
test_cases = []
for _ in range(t):
    case = []
    for _ in range(10):
        case.append(input())
    test_cases.append(case)


results = calculate_points(t, test_cases)
for result in results:
    print(result)
