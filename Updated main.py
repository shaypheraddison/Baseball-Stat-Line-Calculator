stat_list = ["hits" , "at bats" , "walks" , "hit-by-pitches" , "sacrifice fly's" , "singles" , "doubles" , "triples" , "home runs"]
stat = 0
while stat < len(stat_list):
    stat_input = input("How many " + stat_list[stat] + "?: ").split()
    stat += 1


def average():
    return stat_list[0] / stat_list[1]
def on_base_percent():
    return stat_list[3] + stat_list[0] + stat_list[2] / stat_list[1] + stat_list[3] + stat_list[2] + stat_list[4]
def slugging():
    return stat_list[5] + (stat_list[6] * 2) + (stat_list[7] * 3) + (stat_list[8] * 4) / stat_list[1]
def on_base_plus_slugg():
    return on_base_percent() + slugging()


print(f"The final slash line is: {average():.3f}/{on_base_percent():.3f}/{slugging():.3f}/{on_base_percent():.3f}")




