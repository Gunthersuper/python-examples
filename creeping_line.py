import time

s = 'Without further interruption, lets celebrate and suck some dick!   '

while True:
    s = s + s[0]
    s = s[1:]
    print(s[0:20], end='\r')
    time.sleep(0.1)
