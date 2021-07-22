## Getting Started
1. Install and actvate a virtual environment
   ```bash
   $ python3.6 -m venv --without-pip virtual

   $ source virtual/bin/activate
   ```

2. Install **pip** and project **dependencies**
   ```sh
   (virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python
   virtual) $ pip install -r requirements.txt
    ```
* See deployment for notes on how to deploy the project on a live system.

### Database requirements
1.  To get a development env running, use the **.env.example** file to create **your own** `.env` file.
2.  Create a **postgres** db and add the credentials to the .env file
```
(virtual)$ psql
pc-name=#  CREATE DATABASE <name>;
```
Import db: ```psql -U username dbname < dbexport.pgsql```

3.  Apply initial migrations
```sh 
(virtual) $ python manage.py migrate 
```
4. Run migrations to your database
```sh
(virtual) $ python manage.py makemigrations application
(virtual) $ python manage.py migrate
```
5. Create admin account
```
(virtual) $ python manage.py createsuperuser
```
6.  Start development server
```
 (virtual) $ python3 manage.py runserver
 ```

## License
This project is licensed under the MIT License - see the LICENSE.md file for details
