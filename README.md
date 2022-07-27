This is a inventory tracking application to demonstrate basic CRUD operations in a web app.

It use Django as it's backend framework along with Bootstrap and Crisp Forms for the frontend. 

For ease of demonstration the web app can be deployed using docker on any machine.

***Setup Instructions***
1. Clone the project onto your machine
	`git clone …`
2. Move into the project directory
	 `cd inventory_tracker`
3. Perform migrations to setup the DB
	`docker-compose run web python inventory_tracker/manage.py migrate`
4. Create and start the container
	 `docker-compose up`

The web application can now be accessed using a browser on your local machine at the localhost address [http://127.0.0.1:8000/item/list/](http://127.0.0.1:8000/item/list/)