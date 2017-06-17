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





# Courses for Udacity's intro to programming 
catalog1 = Catalog(user_id=1, name="Intro to Programming")

session.add(catalog1)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Learn to Code", description="It begins! Get oriented, learn the basics of HTML, write your first line of code, and receive your first review!",
                     price="$99", catalog=catalog1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Make a Stylish Webpage", description="Add style to your HTML code with CSS (Cascading Style Sheets). Experiment with adjusting various style rules in CSS to make your website shine. Achieve the look and presentation you want for your own webpage.", 
                     price="$99", catalog=catalog1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Python Programming Foundations", description="Explore fundamental programming concepts in Python like logic checks, data structures, and functions through interactive quizzes and practice on your own computer. Learn syntax, debugging techniques and basic problem-solving concepts.",
                     price="$99", catalog=catalog1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Object-Oriented Programming with Python", description="Learn OOP through a series of mini-projects and exercises using a variety of Python libraries. Programmatically send text messages, decode secret messages, and draw images with Python.",
                     price="$99", catalog=catalog1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Explore Programming Career Options", description="Develop an understanding of the important differences between Front-End, Back-End, iOS, Android, and Data Analysis. Learn from real-life examples of programmers in each field, so you can make informed decisions about your own path forward.",
                     price="$99", catalog=catalog1)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Experience a Career Path", description="Select one of the five available career-track programs, and complete a series of lessons from within that programs curriculum.",
                     price="$99", catalog=catalog1)

session.add(catalogItem6)
session.commit()





# course project items for VR Developer nanodegree 
catalog2 = Catalog(user_id=1, name="VR Developer")

session.add(catalog2)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 0: What is the Code?", description="This project lets you experience multiple 3D environments from the Udacity VR program. You will download the Udacity VR app and run it inside of your Cardboard headset. When you put on the headset, you will walkaround an apartment and island from the VR Nanodegree and see demonstrations of various VR techniques you will soon learn.",
                     price="$200", catalog=catalog2)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 1: Udacity Carnival", description="Customize and build a VR carnival game! When you begin, you will have three carnival games that are out of order. It is your job to fix them. Using Unity, you will fix each game by correctly wiring up the event system.  After that, you will customize each game with your own images and text. When you finish, you will play the three games and send us your score. You will win points, have fun, and learn a lot about event-based programming and art customization inside of Unity.",
                     price="$200", catalog=catalog2)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 2: Build an Apartment", description="Become a VR architect and design an apartment! Start off by creating some walls. Next, add some couches, chairs, tables, and rugs. Do not forget to add a kitchen! Once you have finished decorating, be sure to add some nice mood lighting. Then, deploy it to your Cardboard headset.",
                     price="$200", catalog=catalog2)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 3: A Maze", description="Place the walls, add lights and materials, and then code a fully functional VR maze game using Unity and the Google VR SDK, where the user explores a maze environment to demonstrate working knowledge of 2D and 3D UI, waypoint based navigation, procedural animation, interactive objects, spatial audio, particle effects, and persistent storage of session data. Players will navigate the maze, collect coins along the way, then find a key that opens a gate to secret treasure.",
                     price="$200", catalog=catalog2)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 4: Puzzler", description="You will apply design techniques to iterate, document, and write a public write-up for a well-designed and user-tested mobile VR application that asks users to solve a familiar Simon-says-like puzzle in a new way. This writeup will be graded as your course project.",
                     price="$200", catalog=catalog2)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 5: Night at the Museum", description="For this project, you will construct a virtual reality exhibit about a cutting-edge VR company or technology of your choice. After conducting your research, you will create a mobile virtual reality experience with information booths that include both visual and audio feedback for users. These booths will need to showcase your findings the goal here is to inform other people about the topic at hand in a fun and creative way through a series of at least five display points. Users should be able to travel back and forth between display areas inside the space. Note: This is not a VR slideshow, it is a VR space which contains information about your research. This project showcases locomotion, VR scene design, interactivity, as well as an informed understanding of the industry.",
                     price="$200", catalog=catalog2)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 6: Tic-Tac-Toe", description="In this project, you will play detective and put your optimization skills to use by speeding up a poorly optimized VR game. The game is Tic-Tac-Toe, played against a friendly AI Robot. While fun and attractive, the only problem is that the experience is completely unoptimized for mobile VR. Your task is to use what you have learned to optimize this project to run at 60 frames per second on your phone.",
                     price="$200", catalog=catalog2)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Project 7: The Protagonist's Journey", description="In this project, you will do everything you need to prepare for a 360 shoot. You will write the script, produce the storyboard, and then finally plan the logistics surrounding the shoot. By the end, you will be prepared to make a great 360 film.",
                     price="$200", catalog=catalog2)

session.add(catalogItem8)
session.commit()

catalogItem9 = CatalogItem(user_id=1, name="Project 8: The Storytellers Revenge", description="In this project, you will stitch together your own footage (or footage provided). Then, you will correct the color and edit the raw footage into a story. Finally, you will build a custom 360 video player in Unity and add controls, particles, titles, credits, and at least one interaction (like a button and trigger pull, or a gaze-based interaction). The interaction should trigger a different video, branch the story, or allow for replayability.",
                     price="$200", catalog=catalog2)

session.add(catalogItem9)
session.commit()

catalogItem10 = CatalogItem(user_id=1, name="Project 9: Rube Goldberg Challenge", description="This project is a chance for you to create your first fully-functional high-immersion VR game. You will create a Rube Goldberg game that challenges players to create contraptions that solve physics puzzles. First you will import SteamVR and set up your scene environment. Then you will add locomotion, grabbing physics, and a menu system. With the core components built, you will create Oculus versions of your code.",
                     price="$200", catalog=catalog2)

session.add(catalogItem10)
session.commit()

catalogItem11 = CatalogItem(user_id=1, name="Project 10: Performance Bounceback", description="Performance optimization is one of the most important skillsets for a VR developer, since apps running below the target framerate are essentially unplayable, causing nausea and discomfort. This project simulates a real-world scenario in which a VR game has been hastily built with a focus on functionality rather than performance. You have been hired to take the game and make it a performant app ready for release!",
                     price="$200", catalog=catalog2)

session.add(catalogItem11)
session.commit()

catalogItem12 = CatalogItem(user_id=1, name="Project 11: Kitchen Cleanup", description="This project is your first chance to make a game within Unreal Engine 4 for either standing or roomscale VR.  You will need to utilize motion controllers to build a kitchen-themed interaction game, and you will use functions, physics, blueprint communication, and audio to create an immersive experience. Spawn messy dishes and get them into the sink as quickly as possible!",
                     price="$200", catalog=catalog2)

session.add(catalogItem12)
session.commit()

catalogItem13 = CatalogItem(user_id=1, name="Project 12: Hide and Seek", description="This is your first chance to build an Unreal VR experience based around locomotion. You will create a find-the-object style of game, create a set of blueprints that randomly hides an object, and develop a locomotion method that allows you to move around the apartment so you can find the object.",
                     price="$200", catalog=catalog2)

session.add(catalogItem13)
session.commit()

catalogItem14 = CatalogItem(user_id=1, name="Project 13: VR Nanodegree Capstone", description="For your final project, you will work to complete a series of VR challenges, winning points as you progress. You will create a VR project of your choosing, using any hardware. But, it must meet certain criteria in order to win. You can choose from a wide range of achievements like app store submission, use of speech recognition, or mixed reality trailer. Each achievement then wins you a different number of points. To successfully complete the project, you need to reach the required points level.",
                     price="$200", catalog=catalog2)

session.add(catalogItem14)
session.commit()





# course project items for Robotics nanodegree 
catalog3 = Catalog(user_id=1, name="Robotics")

session.add(catalog3)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Search and Sample Return", description="This first project is styled after the NASA Sample Return Robot Competition. In a simulated environment you will perform a search for samples of interest using some basic computer vision techniques. With just a few lines of Python code you will get a chance to experience the three main steps in robotics: perception, decision making, and actuation.",
                     price="$200", catalog=catalog3)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Pick and Place", description="In this project, using what you now know of kinematics, you will use ROS to manipulate a robotic arm with six degrees of freedom in simulation to pick up an object from one location and put it another. You will need to first identify where the object is located, then successfully retrieve it and put it in another location without running into obstacles in the environment. Once you master this, you are ready for the Amazon Robotics Challenge!",
                     price="$200", catalog=catalog3)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Perception", description="Using what you have learned about perception, you will tackle the task of locating an object in a cluttered environment, then controlling a robotic arm to grab it and move it to a different location. The PR2 is an advanced two-armed robotics development platform created by Willow Garage and in this project, you will use the PR2 in simulation to accomplish this task. Here you will leverage MoveIt!, one of the most powerful software packages in the ROS ecosystem to perform collision detection and motion planning.",
                     price="$200", catalog=catalog3)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Follow Me", description="In this project, you will train a deep neural network to identify and track a target in simulation and then issue commands to a drone to follow that target. So-called follow me applications like this are key to many fields of robotics and the very same techniques you apply here could be extended to scenarios like adaptive cruise control in autonomous vehicles or human-robot collaboration in industry.",
                     price="$200", catalog=catalog3)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Motion Planning", description="Stay tuned for additional info we will cover the Term Two syllabus in depth in a future post",
                     price="$200", catalog=catalog3)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 6: Localization", description="Stay tuned for additional info we will cover the Term Two syllabus in depth in a future post.",
                     price="$200", catalog=catalog3)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Hardware Integration", description="Stay tuned for additional info we will cover the Term Two syllabus in depth in a future post, and provide details about your robot hardware!",
                     price="$200", catalog=catalog3)

session.add(catalogItem7)
session.commit()





# course project items for Digital Marketing nanodegree 
catalog4 = Catalog(user_id=1, name="Digital Marketing")

session.add(catalog4)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Prepare to Market", description="Articulate your objective and build a target persona for your product.",
                     price="$200", catalog=catalog4)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Market your Content", description="Write a blog post and distribute it across social platforms.",
                     price="$200", catalog=catalog4)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Run a Facebook Campaign", description="Create, manage and monitor a real-world Facebook ad campaign.",
                     price="$200", catalog=catalog4)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Search Engine Optimization (SEO) Audit", description="Recommend a target keyword list and optimize the design and UX of a website for search.",
                     price="$200", catalog=catalog4)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Run an Adwords Campaign", description="Create, manage and monitor a real-world AdWords campaign.",
                     price="$200", catalog=catalog4)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 6: Evaluate a Display Advertising Campaign", description="In this project, you will evaluate the results of a display advertising campaign and create a presentation of the results for management. Your summary will include the targeting strategy, creatives used, the results of the campaign, and recommendations on how to improve the campaign.",
                     price="$200", catalog=catalog4)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Market with Email", description="In this project, you will plan and prepare an email marketing campaign for a B2C or a B2B product. You will write an email, and evaluate the results of an email campaign.",
                     price="$200", catalog=catalog4)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Project 8: Create your Digital Marketing Portfolio", description="In your final project, you will summarize the different marketing campaigns you have executed, and reflect on the results. You will evaluate the ROI of your campaigns, compare the results across platforms, then formulate recommendations for future marketing action and budget allocation.",
                     price="$200", catalog=catalog4)

session.add(catalogItem8)
session.commit()





# course project items for Deep Learning Foundations nanodegree 
catalog5 = Catalog(user_id=1, name="Deep Learning Foundations")

session.add(catalog5)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Your first neural network", description="Build and train your own Neural Network from scratch to predict the number of bikeshare users on a given day.",
                     price="$200", catalog=catalog5)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Image Classification", description="Classify images from the CIFAR-10 dataset using a convolutional neural network.",
                     price="$200", catalog=catalog5)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Generate TV scripts", description="Use deep learning to generate new scripts for your favorite TV show.",
                     price="$200", catalog=catalog5)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Translate a Language", description="Translate from one language to another.",
                     price="$200", catalog=catalog5)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Generate Faces", description="Compete two neural networks against each other to generate realistic faces.",
                     price="$200", catalog=catalog5)

session.add(catalogItem5)
session.commit()





# course project items for Artificial Intelligence nanodegree 
catalog6 = Catalog(user_id=1, name="Artificial Intelligence")

session.add(catalog6)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Build a Game-Playing Agent", description="Design and implement an agent to play the game of Isolation, a deterministic, two-player game in which the players alternate turns moving between cells on a regular grid till one of them has no more moves left. Use adversarial search with heuristic evaluation functions to overcome computational challenges and make your agent a smarter player.",
                     price="$200", catalog=catalog6)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Implement a Planning Search", description="Solve air cargo logistics problems by decomposing them into individual actions using a formal planning framework, identifying dependencies and effects of each action, and generating valid plans using search techniques. Experiment with various automatically generated heuristics, including planning graph heuristics, and provide an analysis of your results.",
                     price="$200", catalog=catalog6)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Design a Sign Language Recognition System", description="Use Hidden Markov Models to recognize gestures in American Sign Language, from individual words to complete sentences. Train it on a dataset of videos that have been pre-processed and annotated, and test on novel sequences. Improve your recognizer by finding the best English translation of each sentence.",
                     price="$200", catalog=catalog6)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Term 2: Concentration", description="You will choose one of three concentrations. These may include Natural Language Processing, Computer Vision, and Speech Recognition. Actual concentrations are still being finalized so these may change.  More information coming soon!",
                     price="$200", catalog=catalog6)

session.add(catalogItem4)
session.commit()





# course project items for Self-Driving Car Engineer nanodegree 
catalog7 = Catalog(user_id=1, name="Self-Driving Car Engineer")

session.add(catalog7)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Detect Lane Lines", description="Detect highway lane lines from a video stream. Use OpenCV image analysis techniques to identify lines, including Hough transforms and Canny edge detection.",
                     price="$200", catalog=catalog7)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Traffic Sign Classification", description="Implement and train a convolutional neural network to classify traffic signs. Use validation sets, pooling, and dropout to choose a network architecture and improve performance.",
                     price="$200", catalog=catalog7)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="PRoject 3: Behavioral Cloning", description="Architect and train a deep neural network to drive a car in a simulator. Collect your own training data and use it to clone your own driving behavior on a test track.",
                     price="$200", catalog=catalog7)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Advanced Lane Detection", description="Detect lane lines in a variety of conditions, including changing road surfaces, curved roads, and variable lighting. Use OpenCV to implement camera calibration and transforms, as well as filters, polynomial fits, and splines.",
                     price="$200", catalog=catalog7)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Vehicle Tracking", description="Track vehicles in camera images using image classifiers such as SVMs, decision trees, HOG, and DNNs. Apply filters to fuse position data.",
                     price="$200", catalog=catalog7)

session.add(catalogItem5)
session.commit()





# course project items for Business Analyst nanodegree 
catalog8 = Catalog(user_id=1, name="Business Analyst")

session.add(catalog8)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Predict Sales for a Catalog Launch", description="A home-goods manufacturer wants to predict expected profits from a catalog launch. You will apply a framework to work through the problem and build a linear regression model to provide results and a recommendation.",
                     price="$200", catalog=catalog8)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Select the Location of a New Pet Store", description="A pet store chain is selecting the location for its next store. You will use data preparation techniques to build a robust analytic dataset and use it to build a predictive model to select the best location.",
                     price="$200", catalog=catalog8)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Create Reports from a Database", description="Design and implement a short quiz app about some topic you are familiar with.",
                     price="$200", catalog=catalog8)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="PRoject 4: Build Tableau Dashboards", description="A movie producer wants to better understand film industry trends before releasing its next movie. You will explore a dataset and build Tableau dashboards to answer a set of questions and tell a story with data.",
                     price="$200", catalog=catalog8)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Predict Loan Default Risk", description="A bank recently received an influx of loan applications. You will build and apply a classification model to provide a recommendation on which loan applicants the bank should lend to.",
                     price="$200", catalog=catalog8)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="PRoject 6: A/B Test a Menu Launch", description="A chain of coffee shops is considering launching a new menu. You will design and analyze an A/B test and write up a recommendation on whether the chain should introduce the new menu.",
                     price="$200", catalog=catalog8)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Forecast Video Game Demand", description="A video game producer is planning production levels. You will use time series forecasting models to forecast monthly demand and provide a recommendation to help match supply to demand.",
                     price="$200", catalog=catalog8)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Project 8: Combine Predictive Techniques", description="A grocery store chain is planning a significant expansion. You will use multiple analytical techniques to provide recommendations on where and how to expand. After completing the project, you will feel comfortable combining predictive techniques and delivering solutions to complex business problems.",
                     price="$200", catalog=catalog8)

session.add(catalogItem8)
session.commit()





# course project items for Android Basics nanodegree 
catalog9 = Catalog(user_id=1, name="Android Basics")

session.add(catalog9)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Build a Single Screen App", description="Design and implement a simple app that displays information about a small business.",
                     price="$200", catalog=catalog9)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Score Keeper App", description="Implement an app to track scores between two teams playing a game.",
                     price="$200", catalog=catalog9)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Quiz App", description="Design and implement a short quiz app about some topic you are familiar with.",
                     price="$200", catalog=catalog9)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Musical Structure App", description="Architect the user experience and technical design of an app to play music for a user.",
                     price="$200", catalog=catalog9)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Report Card", description="Create a custom Java class to model the information in a student report card.",
                     price="$200", catalog=catalog9)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 6: Tour Guide App", description="Create an app to guide a user around a city or location of your choice!",
                     price="$200", catalog=catalog9)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Book Listing App", description="Create an app to list the published books on a given topic using the Google Books API.",
                     price="$200", catalog=catalog9)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Project 8: News App", description="Create an app to display recent news stories on a topic of your choice using a web API.",
                     price="$200", catalog=catalog9)

session.add(catalogItem8)
session.commit()

catalogItem9 = CatalogItem(user_id=1, name="Project 9: Habit Tracker App", description="Create an app to track your habits!",
                     price="$200", catalog=catalog9)

session.add(catalogItem9)
session.commit()

catalogItem10 = CatalogItem(user_id=1, name="Project 10: Inventory App", description="Create an app to track the inventory of a retail store, including current stock and supplier information.",
                     price="$200", catalog=catalog9)

session.add(catalogItem10)
session.commit()





# course project items for Machine Learning Engineer nanodegree 
catalog10 = Catalog(user_id=1, name="Machine Learning Engineer")

session.add(catalog10)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 0: Titanic Survival Exploration", description="In this optional project, you will create decision functions that attempt to predict survival outcomes from the 1912 Titanic disaster based on each passengers features, such as sex and age. You will start with a simple algorithm and increase its complexity until you are able to accurately predict the outcomes for at least 80 percent of the passengers in the provided data. This project will introduce you to some of the concepts of machine learning as you start the Nanodegree program.",
                     price="$200", catalog=catalog10)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 1: redicting Boston Housing Prices", description="The Boston housing market is highly competitive, and you want to be the best real estate agent in the area. To compete with your peers, you decide to leverage a few basic machine learning concepts to assist you and a client with finding the best selling price for their home. Luckily, you have come across the Boston Housing dataset which contains aggregated data on various features for houses in Greater Boston communities, including the median value of homes for each of those areas. Your task is to build an optimal model based on a statistical analysis with the tools available. This model will then used to estimate the best selling price for your clients home.",
                     price="$200", catalog=catalog10)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 2: Finding Donors for CharityML", description="CharityML is a fictitious charity organization located in the heart of Silicon Valley that was established to provide financial support for people eager to learn machine learning. After nearly 32,000 letters sent to people in the community, CharityML determined that every donation they received came from someone that was making more than $50,000 annually. To expand their potential donor base, CharityML has decided to send letters to residents of California, but to only those most likely to donate to the charity. With nearly 15 million working Californians, CharityML has brought you on board to help build an algorithm to best identify potential donors and reduce overhead cost of sending mail. Your goal will be evaluate and optimize several different supervised learners to determine which algorithm will provide the highest donation yield while also reducing the total number of letters being sent.",
                     price="$200", catalog=catalog10)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 3: Creating Customer Segments", description="A wholesale distributor recently tested a change to their delivery method for some customers, by moving from a morning delivery service five days a week to a cheaper evening delivery service three days a week. Initial testing did not discover any significant unsatisfactory results, so they implemented the cheaper option for all customers. Almost immediately, the distributor began getting complaints about the delivery service change and customers were canceling deliveries losing the distributor more money than what was being saved. You have been hired by the wholesale distributor to find what types of customers they have to help them make better, more informed business decisions in the future. Your task is to use unsupervised learning techniques to see if any similarities exist between customers, and how to best segment customers into distinct categories.",
                     price="$200", catalog=catalog10)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 4: Train a Smartcab to Drive", description="In the not so distant future, taxicab companies across the United States no longer employ human drivers to operate their fleet of vehicles. Instead, the taxicabs are operated by self driving agents, known as smartcabs, to transport people from one location to another within the cities those companies operate. In major metropolitan areas, such as Chicago, New York City, and San Francisco, an increasing number of people have come to rely on smartcabs to get to where they need to go as safely and efficiently as possible. Although smartcabs have become the transport of choice, concerns have arose that a self-driving agent might not be as safe or efficient as human drivers, particularly when considering city traffic lights and other vehicles. To alleviate these concerns, your task as an employee for a national taxicab company is to use reinforcement learning techniques to construct a demonstration of a smartcab operating in real time to prove that both safety and efficiency can be achieved.",
                     price="$200", catalog=catalog10)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 5: Image Classification", description="Classify images from the CIFAR-10 dataset using a convolutional neural network.",
                     price="$200", catalog=catalog10)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 6: Capstone Project", description="In this capstone project, you will leverage what you have learned throughout the Nanodegree program to solve a problem of your choice by applying machine learning algorithms and techniques. You will first define the problem you want to solve and investigate potential solutions and performance metrics. Next, you will analyze the problem through visualizations and data exploration to have a better understanding of what algorithms and features are appropriate for solving it. You will then implement your algorithms and metrics of choice, documenting the preprocessing, refinement, and postprocessing steps along the way. Afterwards, you will collect results about the performance of the models used, visualize significant quantities, and validate, justify these values. Finally, you will construct conclusions about your results, and discuss whether your implementation adequately solves the problem.",
                     price="$200", catalog=catalog10)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Resume Review", description="In this project, you will update your resume according to the conventions that recruiters expect and get tips on how to best represent yourself to pass the 6 second screen. You will also make sure that your resume is appropriately targeted for the job you are applying for. We recommend all students update their resumes to show off their newly acquired skills regardless of whether you are looking for a new job soon.",
                     price="$200", catalog=catalog10)

session.add(catalogItem8)
session.commit()




# course project items for Front-End Web Developer nanodegree 
catalog11 = Catalog(user_id=1, name="Front-End Web Developer")

session.add(catalog11)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Build a Portfolio Site", description="You will be provided with a design mockup as a PDF-file and must replicate that design in HTML and CSS. You will develop a responsive website that will display images, descriptions and links to each of the portfolio projects you will complete throughout the course of the Front-End Web Developer Nanodegree.",
                     price="$200", catalog=catalog11)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Interactive Resume", description="You will develop an interactive resume application that reads your resume content from a JSON file and dynamically displays that content within a provided template. You will use objects, functions, conditionals, and control structures to compose the content that will display on the resume.",
                     price="$200", catalog=catalog11)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Classic Arcade Game Clone", description="You will be provided with visual assets and a game loop engine; using these tools you must add a number of entities to the game including the player characters and enemies to recreate the classic arcade game Frogger",
                     price="$200", catalog=catalog11)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Website Optimization", description="You will optimize a provided website with a number of optimization- and performance-related issues so that it achieves a target PageSpeed score and runs at 60 frames per second.",
                     price="$200", catalog=catalog11)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Neighborhood Map", description="You will develop a single page application featuring a map of your neighborhood or a neighborhood you would like to visit. You will then add additional functionality to this application, including: map markers to identify popular locations or places you had like to visit, a search function to easily discover these locations, and a listview to support simple browsing of all locations. You will then research and implement third-party APIs that provide additional information about each of these locations (such as StreetView images, Wikipedia articles, Yelp reviews, etc).",
                     price="$200", catalog=catalog11)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 6: Feed Reader Testing", description="In this project you are given a web-based application that reads RSS feeds. The original developer of this application clearly saw the value in testing, they have already included Jasmine and even started writing their first test suite! Unfortunately, they decided to move on to start their own company and we are now left with an application with an incomplete test suite. That is where you come in.",
                     price="$200", catalog=catalog11)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Resume Review", description="In this project, you will update your resume according to the conventions that recruiters expect and get tips on how to best represent yourself to pass the 6 second screen. You will also make sure that your resume is appropriately targeted for the job you are applying for. We recommend all students update their resumes to show off their newly acquired skills regardless of whether you are looking for a new job soon.",
                     price="$200", catalog=catalog11)

session.add(catalogItem7)
session.commit()




# course project items for full-stack nanodegree 
catalog12 = Catalog(user_id=1, name="Full-Stack Web Developer")

session.add(catalog12)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Movie Trailer Website", description="You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then use your code to generate a static web page allowing visitors to browse their movies and watch the trailers.",
                     price="$200", catalog=catalog12)

session.add(catalogItem1)
session.commit()


catalogItem2 = CatalogItem(user_id=1, name="Project 2: Portfolio Project website", description="You will be provided a design mockup as a PDF-file, and you must replicate that design in HTML and CSS. You will develop a responsive website that will display images, descriptions and links to each of the portfolio projects you will complete through the course of your Nanodegree program.",
                     price="$200", catalog=catalog12)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Logs Analysis", description="You will analyze data from the logs of a web service to answer questions such as What is the most popular page? and When was the error rate high? using advanced SQL queries.",
                     price="$200", catalog=catalog12)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Item Catalog", description="You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.",
                     price="$200", catalog=catalog12)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Neighborhood Map", description="You will develop a single-page application featuring a map of your neighborhood or a neighborhood you would like to visit. You will then add additional functionality to this application, including: map markers to identify popular locations or places you would like to visit, a search function to easily discover these locations, and a listview to support simple browsing of all locations. You will then research and implement third-party APIs that provide additional information about each of these locations (such as StreetView images, Wikipedia articles, Yelp reviews, etc).",
                     price="$200", catalog=catalog12)

session.add(catalogItem5)
session.commit()


catalogItem6 = CatalogItem(user_id=1, name="Project 6: Linux Server Configuration", description="You will take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.",
                     price="$200", catalog=catalog12)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Resume Review", description="In this project, you will update your resume according to the conventions that recruiters expect and get tips on how to best represent yourself to pass the 6 second screen. You will also make sure that your resume is appropriately targeted for the job you are applying for. We recommend all students update their resumes to show off their newly acquired skills regardless of whether you are looking for a new job soon.",
                     price="$200", catalog=catalog12)

session.add(catalogItem7)
session.commit()




# course project items for Android Developer nanodegree 
catalog13 = Catalog(user_id=1, name="Android Developer ")

session.add(catalog13)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Popular Movies, Stage 1", description="In this project, you will build an app to help users discover popular and recent movies. You will build a clean UI, sync to a server, and present information to the user.",
                     price="$200", catalog=catalog13)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Popular Movies, Stage 2", description="In this project, you will add to the app you built in Stage 1 by building on the detail view for each movie, allowing users to 'favorite' movies, and adding a tablet layout.",
                     price="$99", catalog=catalog13)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Baking App", description="In this project, you will create an app to view video recipes. You will handle media loading, verify your user interfaces with UI tests, and integrate third party libraries. You'll also provide a complete user experience with a home screen widget.",
                     price="$99", catalog=catalog13)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Build It Bigger", description="In this project, you will use Gradle to build a joke-telling app, factoring functionality into libraries and flavors to keep the build simple. You'll also configure a Google Cloud Endpoints development server to supply the jokes.",
                     price="$99", catalog=catalog13)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Make Your App Material", description="In this project, you will update the look and feel of an app to meet Material Design specifications.",
                     price="$99", catalog=catalog13)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Project 6: Capstone, Stage 1 - Design", description="This is your chance to take the skills that you've learned across your Nanodegree journey and apply it to an app idea of your own. You control the vision!  In Stage 1, you will design and plan your app, and receive feedback prior to building it in Stage 2.",
                     price="$99", catalog=catalog13)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 6: Capstone, Stage 2 - Build", description="This is your chance to take the skills that you've learned across your Nanodegree journey and apply it to an app idea of your own. You control the vision!  With your approved Stage 1 design and build plan in-hand, you will execute on your vision and build your app in Stage 2.",
                     price="$99", catalog=catalog13)

session.add(catalogItem7)
session.commit()




# course projects for IOS Nanodegree
catalog14 = Catalog(user_id=1, name="Become an IOS Developer")

session.add(catalog14)
session.commit()


catalogItem1 = CatalogItem(user_id=1, name="Project 1: Pitch Perfect", description="Ever wondered what you would sound like as a Chipmunk or Darth Vader? Wonder no more! In this first project, you will build an app that records a users voice and then plays the modulated audio through a variety of filters.",
                     price="$99", catalog=catalog14)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: MemeMe", description="Solidify your knowledge of iOS user interface concepts by building an app that creates memes from images! The project is split into two parts. In part 1, you will create an app that enables the user to take a picture, and add text at the top and bottom to form a meme, and share the meme with friends. In part 2, you will display sent memes in both a table and collection view.",
                     price="$99", catalog=catalog14)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: On the Map", description="By incorporating networking, apps truly become mobile -- interacting with interesting data using popular web services. In this project, you will build your first networked app that displays information posted by other Udacity students. You will create a map view with pins representing student locations, and by tapping a pin, the app will display a custom URL posted by a student.",
                     price="$99", catalog=catalog14)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Virtual Tourist", description="Tour the world without leaving the comforts of your couch! In this project, you will build an app that lets you tour the world from the comfort of your own couch. Users will be able to drop pins on a map, download pictures for the location, and save favorites to their device.",
                     price="$99", catalog=catalog14)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: You Decide!", description="Landing a job as an iOS Developer requires more than technical skills; it requires creativity and innovation. Drawing on everything you have learned so far in the Nanodegree, you will now dream up, design, and code your own custom app.",
                     price="$99", catalog=catalog14)

session.add(catalogItem5)
session.commit()




# course project items for Data Analyst nanodegree 
catalog15 = Catalog(user_id=1, name="Data Analyst")

session.add(catalog15)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Project 1: Analyze Bay Area Bike Share Data", description="Welcome to the Nanodegree program! Use this warm-up project to get an overview of parts of the data analysis process and get a taste of what this program is all about. In this project, you will download Anaconda and use a Jupyter notebook to explore a bike sharing dataset. No prior data analysis experience is required, though you will need to know some Python in order to complete the tasks presented.",
                     price="$200", catalog=catalog15)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Project 2: Investigate a Dataset", description="Choose one of Udacity's curated datasets and investigate it using NumPy and Pandas. Go through the entire data analysis process, starting by posing a question and finishing by sharing your findings.",
                     price="$99", catalog=catalog15)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Project 3: Wrangle OpenStreetMap Data", description="By incorporating networking, apps truly become mobile -- interacting with interesting data using popular web services. In this project, you will build your first networked app that displays information posted by other Udacity students. You will create a map view with pins representing student locations, and by tapping a pin, the app will display a custom URL posted by a student.",
                     price="$99", catalog=catalog15)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Project 4: Explore and Summarize Data", description="Use R and apply exploratory data analysis techniques to explore relationships in one variable to multiple variables and to explore a selected data set for distributions, outliers, and anomalies.",
                     price="$99", catalog=catalog15)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Project 5: Test a Perceptual Phenomenon", description="Use descriptive statistics and a statistical test to analyze the Stroop effect, a classic result of experimental psychology. Give your readers a good intuition for the data and use statistical inference to draw a conclusion based on the results.",
                     price="$99", catalog=catalog15)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Project 6: Identify Fraud from Enron Email", description="Play detective and put your machine learning skills to use by building an algorithm to identify Enron Employees who may have committed fraud based on the public Enron financial and email dataset.",
                     price="$99", catalog=catalog15)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Project 7: Create a Tableau Story", description="Create a data visualization from a data set that tells a story or highlights trends or patterns in the data. Use Tableau to create the visualization. Your work should be a reflection of the theory and practice of data visualization, such as visual encodings, design principles, and effective communication.",
                     price="$99", catalog=catalog15)

session.add(catalogItem7)
session.commit()




print "added catalog items!"