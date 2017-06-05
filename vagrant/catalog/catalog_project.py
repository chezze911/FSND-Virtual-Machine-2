from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from catalog_database_setup import Base, Catalog, CatalogItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('catalog_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog App"

engine = create_engine('sqlite:///catalogitemswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    #return "The current session state is %s" % login_session['state']
    #RENDER LOGIN TEMPLATE
    return render_template('catalog_login.html', STATE=state)



# @app.route('/fbconnect', methods=['POST'])
# def fbconnect():
#     if request.args.get('state') != login_session['state']:
#         response = make_response(json.dumps('Invalid state parameter.'), 401)
#         response.headers['Content-Type'] = 'application/json'
#         return response
#     access_token = request.data
#     print "access token received %s " % access_token

#     # app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
#     #     'web']['app_id']
#     # app_secret = json.loads(
#     #     open('fb_client_secrets.json', 'r').read())['web']['app_secret']
#     # url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
#     #     app_id, app_secret, access_token)
#     # h = httplib2.Http()
#     # result = h.request(url, 'GET')[1]

#     # # Use token to get user info from API
#     # userinfo_url = "https://graph.facebook.com/v2.4/me"
#     # # strip expire tag from access token
#     # token = result.split("&")[0]


#     # url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
#     # h = httplib2.Http()
#     # result = h.request(url, 'GET')[1]
#     # # print "url sent for API access:%s"% url
#     # # print "API JSON result: %s" % result
#     # data = json.loads(result)
#     # login_session['provider'] = 'facebook'
#     # login_session['username'] = data["name"]
#     # login_session['email'] = data["email"]
#     # login_session['facebook_id'] = data["id"]
    
#         # Exchange client token for long-lived server-side token
#     app_id = json.loads(
#         open('fb_client_secrets.json', 'r').read())['web']['app_id']
#     app_secret = json.loads(
#         open('fb_client_secrets.json', 'r').read())['web']['app_secret']
#     url = ('https://graph.facebook.com/v2.8/oauth/access_token?'
#            'grant_type=fb_exchange_token&client_id=%s&client_secret=%s'
#            '&fb_exchange_token=%s') % (app_id, app_secret, access_token)
#     http = httplib2.Http()
#     result = http.request(url, 'GET')[1]
#     data = json.loads(result)

#     # Extract the access token from response
#     token = 'access_token=' + data['access_token']

#     # Use token to get user info from API.
#     url = 'https://graph.facebook.com/v2.8/me?%s&fields=name,id,email' % token
#     http = httplib2.Http()
#     result = http.request(url, 'GET')[1]
#     data = json.loads(result)
#     login_session['provider'] = 'facebook'
#     login_session['username'] = data["name"]
#     login_session['email'] = data["email"]
#     login_session['facebook_id'] = data["id"]

#     # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
#     stored_token = token.split("=")[1]
#     login_session['access_token'] = stored_token

#     # Get user picture
#     url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token
#     h = httplib2.Http()
#     result = h.request(url, 'GET')[1]
#     data = json.loads(result)

#     login_session['picture'] = data["data"]["url"]

#     # see if user exists
#     user_id = getUserID(login_session['email'])
#     if not user_id:
#         user_id = createUser(login_session)
#     login_session['user_id'] = user_id

#     output = ''
#     output += '<h1>Welcome, '
#     output += login_session['username']

#     output += '!</h1>'
#     output += '<img src="'
#     output += login_session['picture']
#     output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

#     flash("Now logged in as %s" % login_session['username'])
#     return output


# @app.route('/fbdisconnect')
# def fbdisconnect():
#     facebook_id = login_session['facebook_id']
#     # The access token must me included to successfully logout
#     access_token = login_session['access_token']
#     url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
#     h = httplib2.Http()
#     result = h.request(url, 'DELETE')[1]
#     return "you have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('catalog_client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: ' 
    print login_session['username']
    if access_token is None:
      print 'Access Token is None'
      response = make_response(json.dumps('Current user not connected.'), 401)
      response.headers['Content-Type'] = 'application/json'
      return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
      del login_session['access_token'] 
      del login_session['gplus_id']
      del login_session['username']
      del login_session['email']
      del login_session['picture']
      response = make_response(json.dumps('Successfully disconnected.'), 200)
      response.headers['Content-Type'] = 'application/json'
      return response
    else:
  
      response = make_response(json.dumps('Failed to revoke token for given user.', 400))
      response.headers['Content-Type'] = 'application/json'
      return response

# JSON APIs to view Catalog Information
@app.route('/catalogs/JSON')
def catalogsJSON():
  catalogs = session.query(Catalog).all()
  return jsonify(catalogs=[c.serialize for c in catalogs])

#Making an API Endpoint (GET Request)
@app.route('/catalogs/<int:catalog_id>/items/JSON')
def catalogJSON(catalog_id):
    catalog = session.query(Catalog).filter_by(id = catalog_id).one()
    items = session.query(CatalogItem).filter_by(catalog_id = catalog_id).all()
    return jsonify(CatalogItems=[i.serialize for i in items])


@app.route('/catalogs/<int:catalog_id>/items/<int:item_id>/JSON/')
def catalogItemsJSON(catalog_id, item_id):
    catalogItem = session.query(CatalogItem).filter_by(id = item_id).one()
    return jsonify(CatalogItem = catalogItem.serialize)


#Show all Catalogs
@app.route('/')
@app.route('/catalogs/')
def showCatalogs():
    catalogs = session.query(Catalog).order_by(asc(Catalog.name))
    if 'username' not in login_session:
        return render_template('publiccatalogs.html', catalogs=catalogs)
    else:
        return render_template('catalogs.html', catalogs=catalogs)


# Add a new Catalog
@app.route('/catalogs/new', 
           methods=['GET', 'POST'])
def newCatalog():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCatalog = Catalog(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCatalog)
        session.commit()
        flash('New Catalog' + '"' + newCatalog.name + '"' + ' Successfully Created!')
        return redirect(url_for('showCatalogs'))
    else:
    	return render_template('newCatalog.html')


# Edit a Catalog
@app.route('/catalogs/<int:catalog_id>/edit', 
           methods=['GET', 'POST'])
def editCatalog(catalog_id):
    editedCatalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedCatalog.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this catalog.  Please create your own catalog in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedCatalog.name = request.form['name']
        session.add(editedCatalog)
        session.commit()
        flash('Catalog name' + '"' + editedCatalog.name + '"' + ' Successfully Updated!')
        return redirect(url_for('showCatalogs'))
        
    else:
        return render_template('editCatalog.html', catalog=editedCatalog)


# Delete a Catalog
@app.route('/catalogs/<int:catalog_id>/delete', 
           methods=['GET', 'POST'])
def deleteCatalog(catalog_id):
    catalogToDelete = session.query(Catalog).filter_by(id=catalog_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if catalogToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this catalog.  Please create your own catalog in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(catalogToDelete)
        session.commit()
        flash('Catalog' + '"' + catalogToDelete.name + '"' + ' Successfully Deleted!')
    	return redirect(url_for('showCatalogs', catalog_id=catalog_id))
    else:
        return render_template('deleteCatalog.html', catalog=catalogToDelete)
    


@app.route('/catalogs/<int:catalog_id>/item')
def showCatalogItems(catalog_id):
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    creator = getUserInfo(catalog.user_id)
    items = session.query(CatalogItem).filter_by(catalog_id=catalog_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publiccatalogitems.html', items=items, catalog=catalog, creator=creator)
    else:
        return render_template('catalog_items.html', catalog=catalog, items=items, creator=creator)


# Create a new catalog item
@app.route('/catalogs/<int:catalog_id>/item/new', methods=['GET', 'POST'])
def newCatalogItem(catalog_id):
    if 'username' not in login_session:
        return redirect('/login')
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if login_session['user_id'] != catalog.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add items to this catalog. Please create your own catalog in order to add items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        newItem = CatalogItem(name=request.form['name'].strip(), 
                           description=request.form['description'].strip(), 
                           price=request.form['price'].strip(), 
                           catalog_id=catalog_id, 
                           user_id=catalog.user_id)
        session.add(newItem)
        session.commit()
        flash('Catalog item' + '"' + newItem.name + '"' + ' created!')
        return redirect(url_for('showCatalogItems', catalog_id=catalog_id))
    else:
        return render_template('newcatalogitem.html', catalog_id=catalog_id)


# Edit a catalog item
@app.route('/catalogs/<int:catalog_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editCatalogItem(catalog_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(CatalogItem).filter_by(id=item_id).one()
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if login_session['user_id'] != catalog.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit items to this catalog. Please create your own catalog in order to edit items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('catalog item' + '"' + editedItem.name + '"' + ' Successfully Edited!')
        return redirect(url_for('showCatalogItems', catalog_id=catalog_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template(
            'editcatalogitem.html', catalog_id=catalog_id, item_id=item_id, item=editedItem)


# Delete a catalog item
@app.route('/catalogs/<int:catalog_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteCatalogItem(catalog_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    itemToDelete = session.query(CatalogItem).filter_by(id=item_id).one()
    if login_session['user_id'] != catalog.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete items to this catalog. Please create your own catalog in order to delete items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('catalog item' + '"' + itemToDelete.name + '"' + ' Successfully Deleted!')
        return redirect(url_for('showCatalogItems', catalog_id=catalog_id))
    else:
        return render_template('deletecatalogitem.html', item=itemToDelete)
		#return "This page is for deleting catalog item %s.  Task 3 complete!" % catalog_id


# Disconnect based on provider
# @app.route('/disconnect')
# def disconnect():
#     if 'provider' in login_session:
#         if login_session['provider'] == 'google':
#             gdisconnect()
#             del login_session['gplus_id']
#             del login_session['credentials']
#         if login_session['provider'] == 'facebook':
#             fbdisconnect()
#             del login_session['facebook_id']
#         del login_session['username']
#         del login_session['email']
#         del login_session['picture']
#         del login_session['user_id']
#         del login_session['provider']
#         flash("You have successfully been logged out.")
#         return redirect(url_for('showCatalogs'))
#     else:
#         flash("You were not logged in")
#         return redirect(url_for('showCatalogs'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)