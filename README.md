
# ft_linear_regression

This is a simple Machine Learning algorithm capable of predicting the price of cars according to some data provided to the learning algorithm.

The aim of this project is to understand the basics of machine learning through the linear regression statistical method.



## How to Run

The project cointains two python programs:

```
  ./training.py
  ./predict_price.py
```
The first program expect some csv data (in this example I'm using the car mileage and the prices at which these are sold).
Once the program is runned, if data is correct, a new file data.csv is created and the graph of the points and the linear regression is plotted.

The second program uses the data.csv file to estimate the price of a car once the milage is inserted.

```
  python3 predict_price.py
  Enter a mileage: 180000
  Estimated price: 4638.786203426802 $
```

## Calculation results

![Calculation results](https://i.ibb.co/5spkTsX/Screen-Shot-2022-04-27-at-17-26-02.png)

    
## Documentation

 - [How to calculate linear regression using least square method (statisticsfun video)](https://www.youtube.com/watch?v=JvS2triCgOY)


## Authors

- [@buonve](https://www.github.com/buonve)
