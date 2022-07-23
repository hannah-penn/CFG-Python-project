from ast import literal_eval
import csv

## Use Netflix data file to create a program where the user can enter a year and a genre and receive a list of all relevant films and their IMDB ratings.

## DONE 1. import packages/libraries

## DONE 2. define function to get data from spreadsheet (titles.csv) using csv.DictReader() & append rows to the data dictionary - only 'MOVIE' type

## DONE 3. ask user to choose a genre from a list (retrieved from the csv file ('genres' column)) - STRETCH for films with multiple genres, pick the first genre from the list & store in variable

## DONE 4. ask user for the year they want to search & store in variable

## DONE 5. then retrieve title, imdb score, runtime & display in a list

## DONE 6. once the user chooses a film, show them the description

print('\nHello! Time to choose a film.\n')

def read_all_data(): 
    data = []
    with open('titles.csv', 'r') as titles_csv:
        spreadsheet = csv.DictReader(titles_csv)
        for row in spreadsheet:
            data.append(row)
        return data

 
all_genres = ['action', 'animation', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'family', 'horror', 'music', 'romance', 'thriller']

selected_genre = raw_input('Please choose a genre from: action, animation, comedy, crime, documentary, drama, fantasy, family, horror, music, romance, thriller\n')

selected_year = input('Choose a year from 1960 - 2021.\n')

selected_movies = []

def get_movies():
    print('Searching for ' + selected_genre + ' films from ' + str(selected_year) + '.\n')
    all_movies = read_all_data()
    for row in all_movies:
        title = str(row['title'])
        type = str(row['type'])
        # description = str(row['description'])
        release_year = int(row['release_year'])
        runtime = int(row['runtime'])
        all_genres = literal_eval(row['genres'])
        imdb_score = str(row['imdb_score'])
        if type == 'MOVIE' and int(selected_year) == release_year and selected_genre in all_genres:
            selected_movies.append(row)
    return selected_movies

get_movies()

def show_movies():
    print('The following films were found:\n')
    for movie in selected_movies:
        print('Title: ' + movie['title'])
        print('Runtime: ' + movie['runtime'] + ' minutes')
        print('IMDB score: ' + movie['imdb_score'] + '\n')

show_movies()

selected_movie = raw_input('Choose one of the films above to see the description. Please make sure to get the title exact.\n\n')

print('\nYou chose "' + str(selected_movie) + '". The description of that film is: \n')

def show_description():
    for movie in selected_movies:
        if selected_movie == movie['title']:
            print(movie['description'] + '\n\n')

show_description()

print('Enjoy the film!\n')

