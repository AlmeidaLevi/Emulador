ticks = 0

def start(devs, auto = True):
    global ticks
    success = True

    while success:
        if not auto:
            input()

        for dev in devs:
            success = success & dev.step()
        if success:
            ticks += 1