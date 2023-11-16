def get_user_input():
    stats = {}
    stats["hits"] = int(input("Enter the number of hits: "))
    stats["at_bats"] = int(input("Enter the number of at-bats: "))
    stats["walks"] = int(input("Enter the number of walks: "))
    stats["hit_by_pitch"] = int(input("Enter the number of hit-by-pitches: "))
    stats["sacrifice_flies"] = int(input("Enter the number of sacrifice fly's: "))
    stats["singles"] = int(input("Enter the number of singles: "))
    stats["doubles"] = int(input("Enter the number of doubles: "))
    stats["triples"] = int(input("Enter the number of triples: "))
    stats["home_runs"] = int(input("Enter the number of home runs: "))
    return stats

def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    else:
        return hits / at_bats

def calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats, sacrifice_flies):
    number = at_bats + walks + hit_by_pitch + sacrifice_flies
    if number == 0:
        return 0.0
    else:
        return (hits + walks + hit_by_pitch) / number

def calculate_slugging_percentage(singles, doubles, triples, home_runs, at_bats):
    total_bases = singles + 2 * doubles + 3 * triples + 4 * home_runs
    if at_bats == 0:
        return 0.0
    else:
        return total_bases / at_bats

def calculate_ops(hits, walks, hit_by_pitch, at_bats, sacrifice_flies, singles, doubles, triples, home_runs):
    obp = calculate_on_base_percentage(hits, walks, hit_by_pitch, at_bats, sacrifice_flies)
    slg = calculate_slugging_percentage(singles, doubles, triples, home_runs, at_bats)
    return obp + slg

def calculate_stats(stats):
    batting_average = calculate_batting_average(stats["hits"], stats["at_bats"])
    on_base_percentage = calculate_on_base_percentage(
        stats["hits"], stats["walks"], stats["hit_by_pitch"], stats["at_bats"], stats["sacrifice_flies"]
    )
    slugging_percentage = calculate_slugging_percentage(
        stats["singles"], stats["doubles"], stats["triples"], stats["home_runs"], stats["at_bats"]
    )
    ops = calculate_ops(
        stats["hits"], stats["walks"], stats["hit_by_pitch"], stats["at_bats"],
        stats["sacrifice_flies"], stats["singles"], stats["doubles"], stats["triples"], stats["home_runs"]
    )

    return {
        'Batting Average': batting_average,
        'On-Base Percentage': on_base_percentage,
        'Slugging Percentage': slugging_percentage,
        'OPS': ops
    }

def display_stats(stats):
    print(f"Batting Average: {stats['Batting Average']:.3f}")
    print(f"On-Base Percentage: {stats['On-Base Percentage']:.3f}")
    print(f"Slugging Percentage: {stats['Slugging Percentage']:.3f}")
    print(f"OPS: {stats['OPS']:.3f}")
    print(f"The final slash line is: {stats['Batting Average']:.3f}/{stats['On-Base Percentage']:.3f}/{stats['Slugging Percentage']:.3f}/{stats['OPS']:.3f}")

user_stats = get_user_input()

calculated_stats = calculate_stats(user_stats)

display_stats(calculated_stats)
