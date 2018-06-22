import csv


# URL, Title, Selection, Folder
def main():
    with open('instapaper-export.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        columns = next(reader)
        minimums = [99999 for _ in range(len(columns))]
        maximums = [0 for _ in range(len(columns))]
        folders = set()
        for row in reader:
            for i, cell in enumerate(row):
                new_len = len(cell)
                minimums[i] = min(minimums[i], new_len)
                maximums[i] = max(maximums[i], new_len)
            folders.add(row[3])
    print(minimums, maximums, folders)


if __name__ == '__main__':
    main()
