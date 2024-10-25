# Instructions for Setting Up Django Project and Loading Orders

## Step 1: Install Django
1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Open your terminal or command prompt.
3. Install Django using pip by running the following command:
   pip install django

## Step 2: Create a New Django Project (if you haven't already)
1. Create a new Django project by running the following command:
   django-admin startproject myproject
   Replace `myproject` with your desired project name.
2. Navigate to your project directory:
   cd myproject
3. Create a new Django app (if you haven't created one yet):
   python manage.py startapp myapp
   Replace `myapp` with your desired app name.

## Step 3: Set Up Your Models
1. Open the `models.py` file in your app folder and define your models (e.g., `SalesData`).

## Step 4: Create a Management Command
1. Create a directory structure for management commands if it doesn't exist:
   mkdir -p myapp/management/commands
2. Create a Python file (e.g., `load_orders.py`) in the `commands` directory with the logic to load your CSV files into the database.

## Step 5: Place Your CSV Files
1. Create a folder named `FILES` in the root directory of your Django project:
   mkdir FILES
2. Place your CSV files (e.g., `order_region_a.csv`, `order_region_b.csv`) into the `FILES` folder.

## Step 6: Run the Command to Load Orders
1. Open your terminal or command prompt and navigate to the root directory of your Django project (where `manage.py` is located).
2. Run the following command to load orders from the CSV files:
   python manage.py load_orders

## Additional Notes
- Ensure your Django project is properly configured and the database is migrated.
- Check for any errors or warnings in the terminal output during the command execution.

## Install dependencies from requirements.txt use below command
pip install -r requirements.txt

## Payload for jokes API
{url_path}/scripts/jokes/
example:  http://127.0.0.1:8000/scripts/jokes/
POST request
## CURL request
curl --location 'http://127.0.0.1:8000/scripts/jokes/' \
--header 'Content-Type: application/json' \
--data '{
    "number_of_jokes": 2
}'

One can specify how many number of jokes they want to fetch

