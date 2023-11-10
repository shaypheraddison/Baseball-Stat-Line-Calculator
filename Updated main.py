def get_input(stat):
    return float(input("How many " + stat))

hits = get_input("hits?: ")
ab = get_input("at-bats?: ")
bb = get_input("walks?: ")
hbp = get_input("hit-by-pitches?: ")
sac_fly = get_input("sacrifice fly's?: ")
single = get_input("singles?: ")
double = get_input("doubles?: ")
triple = get_input("triples?: ")
home_run = get_input("home runs?: ")

def avg():
    return hits/ab
def obp():
    return (hbp + hits + bb) / (ab + hbp + bb + sac_fly)
def slg():
    return (single + (double * 2) + (triple * 3) + (home_run * 4)) / ab
def ops():
    return obp() + slg()
print(f"The batting average is: = {avg():.3f}")
print(f"The on-base percentage is: = {obp():.3f}")
print(f"The slugging percentage is: = {slg():.3f}")
print(f"The on-base + slugging percentage is: = {ops():.3f}")
print(f"The final slash line is: = {avg():.3f}/{obp():.3f}/{slg():.3f}/{ops():.3f}")




