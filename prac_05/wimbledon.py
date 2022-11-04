"""
Wimbledon
Estimate: 45 minutes
Actual: 37 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_win, countries = process_records(records)
    display_results(champion_to_win, countries)


def process_records(records):
    champion_to_win = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_win[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_win[record[INDEX_CHAMPION]] = 1
    return champion_to_win, countries


def display_results(champion_to_win, countries):
    print("Wimbledon Champions: ")
    for name, win in champion_to_win.items():
        print(name, win)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def get_records(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
