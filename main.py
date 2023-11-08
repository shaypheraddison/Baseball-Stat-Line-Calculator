#This will show the batting average based on the information entered. The goal is to get a whole slash line printed out.
hit , ab = float(input("How many hits?: ")) , float(input("How many at-bats?: "))
calc_avg = hit / ab
print(f"The batting average is: = {calc_avg:.3f}")

hbp , bb , sf = float(input("How many hit-by-pitches?:")) , float(input("How many walks?: ")) , float(input("How many sacrifice fly's?:"))
calc_obp = (hbp + hit + bb) / (ab + hbp + bb + sf)
print(f"The on-base percentage is: = {calc_obp:.3f}")

