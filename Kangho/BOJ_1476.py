e, s, m = map(int, input().split())
year = 1
earth, sun, moon = 1, 1, 1
while True:
    if e == earth and s == sun and m == moon:
        break
    earth += 1
    sun += 1
    moon += 1
    if earth > 15:
        earth = 1
    if sun > 28:
        sun = 1
    if moon > 19:
        moon = 1
    year += 1
print(year)
