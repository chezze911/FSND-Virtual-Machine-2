from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_database_setup import Catalog, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogitemswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com", picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# course project items for full-stack nanodegree 
catalog1 = Catalog(user_id=1, name="Udacity Full-Stack Nanodegree")

session.add(catalog1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Movie Trailer Website Project 1", description="You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then use your code to generate a static web page allowing visitors to browse their movies and watch the trailers.",
                     price="$200", catalog=catalog1)

session.add(catalogItem1)
session.commit()


catalogItem2 = CatalogItem(user_id=1, name="Portfolio Project website Project 2", description="You will be provided a design mockup as a PDF-file, and you must replicate that design in HTML and CSS. You will develop a responsive website that will display images, descriptions and links to each of the portfolio projects you will complete through the course of your Nanodegree program.",
                     price="$200", catalog=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Logs Analysis Project 3", description="You will analyze data from the logs of a web service to answer questions such as What is the most popular page? and When was the error rate high? using advanced SQL queries.",
                     price="$200", catalog=catalog1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Item Catalog Project 4", description="You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.",
                     price="$200", catalog=catalog1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Neighborhood Map Project 5", description="You will develop a single-page application featuring a map of your neighborhood or a neighborhood you would like to visit. You will then add additional functionality to this application, including: map markers to identify popular locations or places you would like to visit, a search function to easily discover these locations, and a listview to support simple browsing of all locations. You will then research and implement third-party APIs that provide additional information about each of these locations (such as StreetView images, Wikipedia articles, Yelp reviews, etc).",
                     price="$200", catalog=catalog1)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Linux Server Configuration Project 6", description="You will take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.",
                     price="$200", catalog=catalog1)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Resume Review Project 7", description="In this project, you will update your resume according to the conventions that recruiters expect and get tips on how to best represent yourself to pass the 6 second screen. You will also make sure that your resume is appropriately targeted for the job you are applying for. We recommend all students update their resumes to show off their newly acquired skills regardless of whether you are looking for a new job soon.",
                     price="$200", catalog=catalog1)

session.add(catalogItem7)
session.commit()


# Courses for Udacity's intro to programming 
catalog2 = Catalog(user_id=1, name="Udacity Intro to Programming Nanodegree")

session.add(catalog2)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Learn to Code", description="It begins! Get oriented, learn the basics of HTML, write your first line of code, and receive your first review!",
                     price="$99", catalog=catalog2)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Make a Stylish Webpage", description="Add style to your HTML code with CSS (Cascading Style Sheets). Experiment with adjusting various style rules in CSS to make your website shine. Achieve the look and presentation you want for your own webpage.", 
                     price="$99", catalog=catalog2)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Python Programming Foundations", description="Explore fundamental programming concepts in Python like logic checks, data structures, and functions through interactive quizzes and practice on your own computer. Learn syntax, debugging techniques and basic problem-solving concepts.",
                     price="$99", catalog=catalog2)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Object-Oriented Programming with Python", description="Learn OOP through a series of mini-projects and exercises using a variety of Python libraries. Programmatically send text messages, decode secret messages, and draw images with Python.",
                     price="$99", catalog=catalog2)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Explore Programming Career Options", description="Develop an understanding of the important differences between Front-End, Back-End, iOS, Android, and Data Analysis. Learn from real-life examples of programmers in each field, so you can make informed decisions about your own path forward.",
                     price="$99", catalog=catalog2)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Experience a Career Path", description="Select one of the five available career-track programs, and complete a series of lessons from within that programs curriculum.",
                     price="$99", catalog=catalog2)

session.add(catalogItem6)
session.commit()


# course projects for IOS Nanodegree
catalog3 = Catalog(user_id=1, name="Udacity IOS Nanodegree")

session.add(catalog3)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Pitch Perfect Project 1", description="Ever wondered what you would sound like as a Chipmunk or Darth Vader? Wonder no more! In this first project, you will build an app that records a users voice and then plays the modulated audio through a variety of filters.",
                     price="$99", catalog=catalog3)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="MemeMe Project 2", description="Solidify your knowledge of iOS user interface concepts by building an app that creates memes from images! The project is split into two parts. In part 1, you will create an app that enables the user to take a picture, and add text at the top and bottom to form a meme, and share the meme with friends. In part 2, you will display sent memes in both a table and collection view.",
                     price="$99", catalog=catalog3)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="On the Map Project 3", description="By incorporating networking, apps truly become mobile -- interacting with interesting data using popular web services. In this project, you will build your first networked app that displays information posted by other Udacity students. You will create a map view with pins representing student locations, and by tapping a pin, the app will display a custom URL posted by a student.",
                     price="$99", catalog=catalog3)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Virtual Tourist Project 4", description="Tour the world without leaving the comforts of your couch! In this project, you will build an app that lets you tour the world from the comfort of your own couch. Users will be able to drop pins on a map, download pictures for the location, and save favorites to their device.",
                     price="$99", catalog=catalog3)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="You Decide! Project 5", description="Landing a job as an iOS Developer requires more than technical skills; it requires creativity and innovation. Drawing on everything you have learned so far in the Nanodegree, you will now dream up, design, and code your own custom app.",
                     price="$99", catalog=catalog3)

session.add(catalogItem5)
session.commit()


print "added catalog items!"