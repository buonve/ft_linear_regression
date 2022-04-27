import csv

def calc_price(mileage, intercept, slope):
    return mileage * slope + intercept

if __name__ == '__main__':
    f = open('output.csv', 'r')
    rows = csv.reader(f)
    data = []
    for row in rows:
        data = row
    y_intercept = float(data[0])
    slope = float(data[1]) 
    mileage = input("Enter the mileage: ")
    print(calc_price(float(mileage), y_intercept, slope), '$')
    f.close()
    
