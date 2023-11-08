#This will show the batting average based on the information entered. The goal is to get a whole slash line printed out (avg/obp/slg/ops)
hit , ab = float(input("How many hits?: ")) , float(input("How many at-bats?: "))
calc_avg = hit / ab

hbp , bb , sf = float(input("How many hit-by-pitches?: ")) , float(input("How many walks?: ")) , float(input("How many sacrifice fly's?: "))
calc_obp = (hbp + hit + bb) / (ab + hbp + bb + sf)

single , double , triple , hr = float(input("How many singles?: ")) , float(input("How many doubles?: ")) , float(input("How many triples?: ")) , float(input("How many home runs?: "))
calc_slg = (single + (double * 2) + (triple * 3) + (hr * 4)) / ab

calc_ops = calc_obp + calc_slg

print(f"Here is the stat line for the batter: = {calc_avg:.3f}/{calc_obp:.3f}/{calc_slg:.3f}/{calc_ops:.3f}")
