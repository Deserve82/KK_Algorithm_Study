def solution(dartResult):
    points = []
    sq = ['S', 'D', 'T']
    num = ''
    for char in dartResult:
        if char in sq:
            p = int(num)
            if char == 'S':
                points.append(p)
            elif char == 'D':
                points.append(p * p)
            else:
                points.append(p*p*p)
            num = ''
        elif char == "*":
            if len(points) > 1:
                points[-1] *= 2
                points[-2] *= 2
            else:
                points[-1] *= 2
        elif char == '#':
            points[-1] *= -1
        else:
            num += char
    answer = sum(points)
    return answer
