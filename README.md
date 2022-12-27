# krassite

This project relize:
1. CRUD news;
2. Import/export xlsx file with intresting places into/from django admin;
3. Send mails to contacts from django admin.

## You can install from Docker:
1. Setup project into you directory:  
`git clone`
2. Rename .env.example file to .env and set constants.
3. In **docker-compose.yml** so set contats for you database.
4. Run docker-compose:  
`docker-compose up --build -d`

After this you have to create superuser for you:  
`docker-compose exec webapp python manage.py createsuperuser`  

And go to 127.0.0.1:8000

## Using

### News
You can create news in admin for this path:  
`localhost:8000/admin` - login with your password  

 - *In admin you can change title/content by rich text*

For use API use path: `localhost:8000/api/new` for chech all news and  
`localhost:8000/api/new/id` - for once new (where id - id-number of new)

### Import/export xlsx files
In admin site you can import xlsx fiiles into places, by clicked into button "Import" and select a file.

### Send mail with constance.
In admin site change title/content of mail by constance, set recipients in contact table.  
Then go to *localhost:8000/send_mail*
