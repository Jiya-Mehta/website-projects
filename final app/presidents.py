from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)

# create a list of dicts
cars_list = convert_to_dict("CARS.csv")

# first route

@app.route('/')
def void():
    return render_template('new.htm', the_title = "Main Menu")


@app.route('/1')
def petrol():
    ids_list = []
    name_list = []
    # fill one list with the number of each car and
    # fill the other with the name of each car Brand name
    for cars in cars_list:
        if (cars['Engine Type']=='Petrol'):
            ids_list.append(cars['Car models'])
            name_list.append(cars['Brand'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('petrol.htm', pairs=pairs_list, the_title="LIST OF CARS WITH FUEL TYPE PETROL")
    
@app.route('/2')
def diesel():
    ids_list = []
    name_list = []
    # fill one list with the number of each car and
    # fill the other with the name of each car Brand name
    for cars in cars_list:
        if (cars['Engine Type']=='Diesel'):
            ids_list.append(cars['Car models'])
            name_list.append(cars['Brand'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('diesel.htm', pairs=pairs_list, the_title="LIST OF CARS WITH FUEL TYPE DIESEL")

@app.route('/3')
def gasoline():
    ids_list = []
    name_list = []
    # fill one list with the number of each car and
    # fill the other with the name of each car Brand name
    for cars in cars_list:
        if (cars['Engine Type']=='Gasoline'):
            ids_list.append(cars['Car models'])
            name_list.append(cars['Brand'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('gasoline.htm', pairs=pairs_list, the_title="LIST OF CARS WITH FUEL TYPE GASOLINE")
    
@app.route('/4')
def index():
    ids_list = []
    name_list = []
    # fill one list with the number of each car and
    # fill the other with the name of each car Brand name
    for cars in cars_list:
        ids_list.append(cars['Car models'])
        name_list.append(cars['Brand'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(ids_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('index.html', pairs=pairs_list, the_title="cars Index")

# second route

@app.route('/cars/<num>')
def detail(num):
    for cars in cars_list:
        if cars['Car models'] == num:
            cars_dict =cars
            break
    # a little bonus function, imported
    ord = make_ordinal( int(num) )
    return render_template('president.html', cars=cars_dict, ord=ord, the_title=cars_dict['Car models'])


# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
