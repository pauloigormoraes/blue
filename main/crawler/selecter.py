import csv
from io import StringIO

def main():

    reviews = csv.reader(open('C:/Projects/blueway/main/dataset/full_reviews/low/low_app_one.csv', "r", encoding="utf8"))
    arr_low = []

    for row in reviews:
        for i in range(0, len(row)):
            print(row[i:4])
        print()
            # if(int(row[2]) <= 2):
            #     print(row[3])
            #     arr_low.append(row)

if __name__ == "__main__":
    main()
