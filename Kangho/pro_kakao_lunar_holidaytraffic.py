from datetime import datetime, timedelta


def solution(lines):
    answer = 0
    times = []
    for line in lines:
        first_start = line[:23]
        first_end = line[24:-1]
        value = timedelta(seconds=float(first_end))
        line_end = datetime.strptime(first_start, '%Y-%m-%d %H:%M:%S.%f')
        line_start = line_end - value + timedelta(seconds=0.001)
        times.append([line_start, line_end])

    for time in times:
        max_number_start = 0
        max_number_end = 0
        number_of_session = len(times)
        start = time[0] + timedelta(seconds=1)
        end = time[1] + timedelta(seconds=1)
        print(start)
        for i in range(number_of_session):
            if times[i][0] < start and start - timedelta(seconds=1) <= times[i][1]:
                max_number_start += 1
            if times[i][0] < end and end - timedelta(seconds=1) <= times[i][1]:
                max_number_end += 1
        if max_number_start > answer:
            answer = max_number_start
        if max_number_end > answer:
            answer = max_number_end
    return answer