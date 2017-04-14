from flask import Flask
app = Flask(__name__)

#Show all restaurants
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return "This page will show all my my restaurants"
    # return render_template('restaurants.html', restaurants=restaurants)
    

@app.route('/restaurant/new')
def newRestaurant():
    return "This page will be for making a new restaurant"


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page will be for editing restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page will be for deleting restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page is the menu for restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return "This page is for making a new menu item for restaurant %s" % restaurant_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page is for editing menu item %s" % menu_id


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
	return "This page is for deleting menu item %s" % menu_id



# def restaurantMenu(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
#     output = ''
#     for i in items:
#         output += i.name
#         output += '</br>'
#         output += i.price
#         output += '</br>'
#         output += i.description
#         output += '</br>'
#         output += '</br>'
#     return output

# # Task 1: Create route for newMenuItem function here


# def newMenuItem(restaurant_id):
#     return "page to create a new menu item. Task 1 complete!"

# # Task 2: Create route for editMenuItem function here


# def editMenuItem(restaurant_id, menu_id):
#     return "page to edit a menu item. Task 2 complete!"

# # Task 3: Create a route for deleteMenuItem function here


# def deleteMenuItem(restaurant_id, menu_id):
#     return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)