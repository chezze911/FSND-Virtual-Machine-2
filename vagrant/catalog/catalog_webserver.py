from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from catalog_database_setup import Base, Catalog, CatalogItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///catalogitem.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Objective 3 Step 2 - Create /catalogs/new page
            if self.path.endswith("/catalogs/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Catalog</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/catalogs/new'>"
                output += "<input name = 'newCatalogName' type = 'text' placeholder = 'New Catalog Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></html></body>"
                self.wfile.write(output)
                return
            if self.path.endswith("/edit"):
                catalogIDPath = self.path.split("/")[2]
                myCatalogQuery = session.query(Catalog).filter_by(
                    id=catalogIDPath).one()
                if myCatalogQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myCatalogQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/catalogs/%s/edit' >" % catalogIDPath
                    output += "<input name = 'newCatalogName' type='text' placeholder = '%s' >" % myCatalogQuery.name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
            
            if self.path.endswith("/delete"):
                catalogIDPath = self.path.split("/")[2]
                myCatalogQuery = session.query(Catalog).filter_by(
                    id=catalogIDPath).one()
                if myCatalogQuery:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output = "<html><body>"
                    output = "<h1>Are you sure you want to delete %s?" % myCatalogQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/catalogs/%s/delete' >" % catalogIDPath
                    output += "<input name = 'newCatalogName' type='text' placeholder = '%s' >" % myCatalogQuery.name
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/catalogs"):
                catalogs = session.query(Catalog).all()
                output = ""
                # Objective 3 Step 1 - Create a Link to create a new catalog item
                output += "<a href = '/catalogs/new' > Make a New Catalog Here </a></br></br>"

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for catalog in catalogs:
                    output += catalog.name
                    output += "</br>"
                    # Objective 2 -- Add Edit and Delete Links
                    # Objective 4 -- Replace Edit href
                    output += "<a href ='/catalogs/%s/edit' >Edit </a> " % catalog.id
                    output += "</br>"
                    # Objective 5 -- Replace Delete href
                    output += "<a href ='/catalogs/%s/delete'> Delete </a>" % catalog.id
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    # Objective 3 Step 3- Make POST method
    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
        
                catalogIDPath = self.path.split("/")[2]

                myCatalogQuery = session.query(Catalog).filter_by(
                    id=catalogIDPath).one()
                
                if myCatalogQuery:
                    session.delete(myCatalogQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/catalogs')
                    self.end_headers()
                        

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newCatalogName')
                    catalogIDPath = self.path.split("/")[2]

                    myCatalogQuery = session.query(Catalog).filter_by(
                        id=catalogIDPath).one()
                    if myCatalogQuery != []:
                        myCatalogQuery.name = messagecontent[0]
                        session.add(myCatalogQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/catalogs')
                        self.end_headers()

            if self.path.endswith("/catalogs/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newCatalogName')

                    # Create new Catalog Object
                    newCatalog = Catalog(name=messagecontent[0])
                    session.add(newCatalog)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/catalogs')
                    self.end_headers()

        except:
            pass


def main():
    try:
        server = HTTPServer(('', 5000), webServerHandler)
        print 'Web server running...open localhost:5000/catalogs in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()


if __name__ == '__main__':
    main()