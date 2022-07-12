import csv

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
        return data

def run():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        month = str(row['month'])
        sales.append(sale)
        total = sum(sales)
        print('Total sales for {}: {}'.format(month, sale))
    print('Total sales for this year: {}'.format(total))

run()

## Use Netflix data file to create a program where the user can enter a year and a genre and receive a list of all relevant films and their IMDB ratings.

## 1. import packages/libraries

## 2. define function to get data from spreadsheet (titles.csv) using csv.DictReader() & append rows to the data dictionary - only 'MOVIE' type

## 3. ask user to choose a genre from a list (retrieved from the csv file ('genres' column)) - for films with multiple genres, pick the first genre from the list & store in variable

## 4. ask user for the year they want to search & store in variable

## 5. then retrieve title, imdb score, runtime & display in a list

## 6. once the user chooses a film, show them the description

