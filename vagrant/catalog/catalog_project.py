from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from catalog_database_setup import Base, Catalog, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalogitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Making an API Endpoint (GET Request)
@app.route('/catalogs/<int:catalog_id>/items/JSON')
def catalogItemsJSON(catalog_id):
    catalog = session.query(Catalog).filter_by(id = catalog_id).one()
    items = session.query(CatalogItem).filter_by(catalog_id = catalog_id).all()
    return jsonify(CatalogItems=[i.serialize for i in items])


@app.route('restaurants/<int:catalog_id>/items/<int:item_id>/JSON/')

# #Fake Catalogs
# catalog = {'name': 'The CRUDdy Crab', 'id': '1'}

# catalogs = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


# #Fake Menu Items
# items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99','id':'5'} ]
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99'}

# JSON APIs to view Catalog Information
# @app.route('/catalogs/JSON')
# def catalogsJSON():
# 	restaurants = session.query(Catalog).all()
# 	return jsonify(restaurants=[c.serialize for c in catalogs])


# @app.route('/catalog/<int:catalog_id>/item/JSON')
# def catalogItemJSON(catalog_id):
#     catalog = session.query(Catalog).filter_by(id=catalog_id).one()
#     items = session.query(CatalogItem).filter_by(
#         catalog_id=catalog_id).all()
#     return jsonify(CatalogItems=[i.serialize for i in items])


# @app.route('/catalog<int:catalog_id>/item/<int:item_id>/JSON')
# def catalogItemJSON(catalog_id, item_id):
#     Catalog_Item = session.query(CatalogItem).filter_by(id=catalog_id).one()
#     return jsonify(Catalog_Item=Menu_Item.serialize)


#Show all Catalogs
@app.route('/')
@app.route('/catalogs/')
def showCatalogs():
    catalogs = session.query(Catalog).all()
    #return "This page will show all my catalogs"
    return render_template('catalogs.html', catalogs=catalogs)


# @app.route('/catalogs/<int:catalog_id>/items')
# def CatalogItems(catalog_id):
#     catalog = session.query(Catalog).first()
#     items = session.query(CatalogItem).filter_by(catalog_id = catalog.id)
#     #return "This page will show all my catalogs"
#     # output = ''
#     # for i in items:
#     #     output += i.name
#     #     output += '</br>'
#     #     output += i.price
#     #     output += '</br>'
#     #     output += i.description
#     #     output += '</br>'
#     #     output += '</br>
#     # return output
#     return render_template('catalogs.html', catalog=catalog, items=items)


@app.route('/catalogs/new', 
           methods=['GET', 'POST'])
def newCatalog():
    if request.method == 'POST':
        newCatalog = Catalog(name=request.form['name'])
        session.add(newCatalog)
        session.commit()
        flash('New Catalog' + '"' + newCatalog.name + '"' + ' Successfully Created!')
        return redirect(url_for('showCatalogs'))
    #return "This page will be for making a new catalog"
    else:
    	return render_template('newCatalog.html')


@app.route('/catalogs/<int:catalog_id>/edit', 
           methods=['GET', 'POST'])
def editCatalog(catalog_id):
    editedCatalog = session.query(Catalog).filter_by(id=catalog_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCatalog.name = request.form['name']
        session.add(editedCatalog)
        session.commit()
        flash('Catalog name' + '"' + editedCatalog.name + '"' + ' Successfully Updated!')
        return redirect(url_for('showCatalogs'))
        	
    #return "This page will be for editing catalog %s" % catalog_id
    else:
        return render_template('editCatalog.html', catalog=editedCatalog)


@app.route('/catalogs/<int:catalog_id>/delete', 
           methods=['GET', 'POST'])
def deleteCatalog(catalog_id):
    catalogToDelete = session.query(Catalog).filter_by(id=catalog_id).one()
    if request.method == 'POST':
        session.delete(catalogToDelete)
        session.commit()
        flash('Catalog' + '"' + catalogToDelete.name + '"' + ' Successfully Deleted!')
    	return redirect(url_for('showCatalogs', catalog_id=catalog_id))
    else:
        return render_template('deleteCatalog.html', catalog=catalogToDelete)
    
    #return "This page will be for deleting catalog %s" % catalog_id
#     return render_template('deleteCatalog.html', catalog_id=catalog_id)


@app.route('/catalogs/<int:catalog_id>/item')
def showCatalogItems(catalog_id):
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    items = session.query(CatalogItem).filter_by(catalog_id=catalog_id).all()
    #return "This page is the items for catalog %s" % catalog_id
    return render_template('catalog_items.html', catalog=catalog, items=items, catalog_id=catalog_id)


@app.route('/catalogs/<int:catalog_id>/item/new', 
           methods=['GET', 'POST'])
def newCatalogItem(catalog_id):
    if request.method == 'POST':
        newItem = CatalogItem(name=request.form['name'].strip(), 
                           description=request.form['description'].strip(), 
                           price=request.form['price'].strip(), 
                           catalog_id=catalog_id)
        session.add(newItem)
        session.commit()
        flash('Catalog item' + '"' + newItem.name + '"' + ' created!')
        return redirect(url_for('showCatalogItems', catalog_id=catalog_id))
    else:
        return render_template('newcatalogitem.html', catalog_id=catalog_id)
        #return "This page is for making a new catalog item for catalog %s. Task 1 complete!" % catalog_id


@app.route('/catalogs/<int:catalog_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editCatalogItem(catalog_id, item_id):
    editedItem = session.query(CatalogItem).filter_by(id=item_id).one()
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
        #return "This page is for editing catalog item %s.  Task 2 complete!" % catalog_id



@app.route('/catalogs/<int:catalog_id>/item/<int:item_id>/delete', 
           methods=['GET', 'POST'])
def deleteCatalogItem(catalog_id, item_id):
    # catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    itemToDelete = session.query(CatalogItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('catalog item' + '"' + itemToDelete.name + '"' + ' Successfully Deleted!')
        return redirect(url_for('showCatalogItems', catalog_id=catalog_id))
    else:
        return render_template('deletecatalogitem.html', item=itemToDelete)
		#return "This page is for deleting catalog item %s.  Task 3 complete!" % catalog_id


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)