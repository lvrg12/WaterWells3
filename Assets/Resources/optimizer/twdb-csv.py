import csv

def main():
    with open('WaterLevelsCombination.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("|") for line in stripped if line)
        with open('WaterLevelsCombination.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

if __name__ == "__main__":
    main()