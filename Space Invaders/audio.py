import stdaudio, stdarray, math, time

def tone(hz, duration):
    N = int(44100.0* duration)
    a = stdarray.create1D(N+1, 0.0)
    for i in range(0, N+1):
        a[i] = math.sin(2.0 * math.pi * i * hz / 44100.0)
    return a

def enemyDead():
    hz = 500
    for i in range(6):
        duration = (2)**(-i-2)
        hz -= i*20 
        a = tone(hz, duration)
        stdaudio.playSamples(a)
