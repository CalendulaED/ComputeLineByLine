import csv

def getlines(maxline):
    file = open('result.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows.pop(0)
    # print(rows)

    for i in range(len(rows)):
        temp = rows[i][0]
        rows[i][0] = rows[i][1]
        rows[i][1] = temp
    # print(rows) 

    rows.sort(reverse=True)
    # print(rows)

    resultLines = []
    for i in range(maxline):
        print(rows[i][1]) #print line number with highest suspicous scores to lowest

if __name__ == "__main__":
    maxline = 3
    getlines(maxline)