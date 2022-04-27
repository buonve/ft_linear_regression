import csv

def calc_price(mileage, intercept, slope):
    return mileage * slope + intercept

if __name__ == '__main__':
    f = open('output.csv', 'r')
    rows = csv.reader(f)
    data = []
    for row in rows:
        data = row
    try:
        y_intercept = float(data[0])
        slope = float(data[1])
    except:
        print("Error: corrupted data")
        f.close()
        exit()
    mileage = input("Enter the mileage: ")
    try:
        print(calc_price(float(mileage), y_intercept, slope), '$')
    except:
        print("Error: not a valid mileage")
        f.close()
        exit()
    f.close()
    
