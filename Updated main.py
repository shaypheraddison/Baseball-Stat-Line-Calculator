def avg(hit , ab):
    return hit/ab
calc_avg = avg(float(input("How many hits?:")) , float(input("How many at-bats?: ")))
print(f"The batting average is: = {calc_avg:.3f}")

