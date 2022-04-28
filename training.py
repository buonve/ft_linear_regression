import csv
import matplotlib.pyplot as plt

def learn_from_data(data):
    # calculate the mean of the xes and ys
    x_mean = 0
    row_counter = len(data)
    try:
        for row in data:
            x_mean += float(row[0])
        x_mean = x_mean / row_counter
        y_mean = 0
        for row in data:
            y_mean += float(row[1])
        y_mean = y_mean / row_counter
        # calculate the errors for each x and y
        x_errors = []
        for row in data:
            x_errors.append(float(row[0]) - x_mean)
        y_errors = []
        for row in data:
            y_errors.append(float(row[1]) - y_mean)
        # calculate the square of the x errors
        x_squared_errors = []
        for error in x_errors:
            x_squared_errors.append(error * error)

        # calculate the product of the x errors and y errors
        x_y_product = []
        for i in range(len(x_errors)):
            x_y_product.append(x_errors[i] * y_errors[i])
            
        
        
        # calculate the slope of the line
        slope = sum(x_y_product) / sum(x_squared_errors)

        # calculate the y-intercept of the line
        y_intercept = y_mean - (slope * x_mean)
    except:
        print("Error: corrupted data")
        return None

    return ([y_intercept, slope])

def plotData(data, y_intercept, slope):
    
    plt.xlabel('Mileage')
    plt.ylabel('Car Prices')
    x_values = []
    y_values = []
    for row in data:
        x_values.append(float(row[0]))
        y_values.append(float(row[1]))
    plt.plot(x_values, y_values, 'ro')
    plt.plot(x_values, [y_intercept + slope * x for x in x_values])
    plt.show()


if __name__ == '__main__':
    # read the data from the csv file
    try:
        file = open('data.csv', 'r')
    except:
        print("Error: missing data")
        exit()
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)
    intercept_slope = learn_from_data(data)
    if(intercept_slope == None):
        file.close()
        exit()
    file.close()
    # write the data to a new csv file
    output = open('output.csv', 'w')
    writer = csv.writer(output)
    writer.writerow(intercept_slope)
    output.close()

    print('Learning complete')
    # plot the data
    plotData(data, intercept_slope[0], intercept_slope[1])







