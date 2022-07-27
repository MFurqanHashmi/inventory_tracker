This is a inventory tracking application to demonstrate basic CRUD operations in a web app. It use Django as it's backend framework along with Bootstrap and Crisp Forms for the frontend. 

For ease of demonstration the web app can be deployed using docker on any machine.

## Setup Instructions
1. Clone the project onto your machine
	`git clone https://github.com/MFurqanHashmi/inventory_tracker.git`
2. Move into the project directory
	 `cd inventory_tracker`
3. Perform migrations to setup the DB
	`docker-compose run web python inventory_tracker/manage.py migrate`
4. Create and start the container
	 `docker-compose up`

The web application can now be accessed using a browser on your host machine at the localhost address [http://127.0.0.1:8000/item/list/](http://127.0.0.1:8000/item/list/)


## Usage Instructions

***Create***
You can create a new item by clicking the *"Add New Item"* button shown on the `/item/list/` route or by going the `/item/` route directly


***Read***
You can view the list of items at the `/item/list/` route


***Update***
You can update an existing entry by clicking the edit button on the right end of the item entry.


***Delete***
You can delete an existing entry by clicking the edit button on the right end of the item entry.


***Create New Warehouses***
As you have seen in the Create form the warehouses can only be selected from a dropdown. In order to add new warehouse locations you can click the *"Add New Warehouse"* button on the `/item/list/` page or by going the `/item/warehouse/` route directly
