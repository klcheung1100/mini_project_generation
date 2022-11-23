# Jenny's Mini Project of Data Engineering Skill Boot Camp 2022 @ Generation

<img src="https://github.com/klcheung1100/mini_project_generation/blob/master/mini_project_pic.png">

<h3>My code is at <a href="https://github.com/klcheung1100/mini_project_generation/blob/master/mini_project_week6.5.py">mini_project_final.py</a>

<h3> 1. Project Bakcground
<h4> <br>This is my individual mini project @ <a href="https://uk.generation.org/">Generation</a>
<br> During the lessons, I've leant Database fundamental, Programming languages including Python and SQL as well as Agile and scrum methodology by doing a lot of hands-on projects and exercises.
<br>As one of the milestone, I built up an order management system and database for "Pop Up cafe". In this project, I have made use of Python (including PyMySql), MySQL to perform data collection, data encoding, data normalisation as well as data persistence.

<h3> 2. Client requirements
<h4><br>The client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding
offices. As such, they require a software application which helps them to
log and track orders.
<br>•As a business, the client wants to maintain a collection of products and couriers.
<br>•When a customer makes a new order, the client needs to create this on the
system.
<br>•The client needs to be able to update the status of an order i.e: preparing, out-for-delivery, delivered.
<br>•When the client exit the system, they need all data to be persisted and not lost.
<br>•When the client starts the system, they need to load all persisted data.

<h3> 3. How did your design go about meeting the project's requirements?
<h4><br> A) I've designed the database through MySQL. By creating serveral tables, I stored the products / orders / couriers' data into specific tables. The client needs to log in to the MySQL local host to access the database, which can ensure the protect of data.
<br>B) I've imported PyMySQL to access the database. By extracting data from the database, client can do different operations to the data, for example, to view / create / update / delete the data from products / orders / couriers tables. By using hashlib library, I built a login system. If the user is fail to login, the user will not be able to proceed. I also imported the pretty table library to enhance the readability.
<br> C) Once there is any updates from the client, the database can automatically update the data.
<br> D) To optimise user experience, I add a "Search" engine in the system. Client can search the orders by Courier ID/ Product ID / Order ID / Status ID.

<h3>4. If you had more time, what is one thing you would improve upon?
<h4>If I had more time, I would create a GUI (Graphic User Interface) to optimise user experience. It will be easier for non-technical person to use the system. Also, I will make a test_mini_project.py to test the code.

<h3>5. What did you most enjoy implementing?
<h4>During the project time, I enjoyed the problem solving task most. Making challenges offers me a way to gain satisfaction. By solving different tasks, I gain a lot of confidence and skills. Now I am more familiar with Python and SQL, and more capable of pursuing better programming skills.

<h3>You can see what I've learnt during the Data Engineering Bootcamp <a href="https://uk.generation.org/manchester/data-engineering/">@Generation</a>
