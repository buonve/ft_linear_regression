import csv

def calc_price(mileage, intercept, slope):
    return mileage * slope + intercept

if __name__ == '__main__':
    try:
        f = open('output.csv', 'r')
    except:
        print("Error: missing data")
        exit()
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
        print('Predicted price:', calc_price(float(mileage), y_intercept, slope), '$')
    except:
        print("Error: not a valid mileage")
        f.close()
        exit()
    f.close()
    
