dartResult = "1D2S#10S"
# 1,-2,10 -> 9
answer = 0
answer_points = []
ten_flag = 0
idx = -1
for char in dartResult:
    if char == "S" or char == "D" or char == "T":
        ten_flag = 0
        if char == "S":
            answer_points.append(temp_point)
        elif char == "D":
            answer_points.append(temp_point*temp_point)
        else:
            answer_points.append(temp_point * temp_point * temp_point)
    elif char == "*" or char == "#":
        ten_flag = 0
        if char == "*":
            if idx == 0:
                answer_points[0] = answer_points[0]*2
            else:
                answer_points[idx-1] = answer_points[idx-1]*2
                answer_points[idx] = answer_points[idx]*2
        else:
            answer_points[idx] = -answer_points[idx]
    else:
        temp_point = int(char)
        if char == "1":
            ten_flag = 1
        if ten_flag == 1 and char == "0":
            temp_point = 10
            idx -= 1
        idx += 1
answer = sum(answer_points)
print(answer)