## Assessment: To-Do Application Development

## Objective
Develop a full-stack To-Do application with user authentication and CRUD operations using:
- Backend: Django 
- Database: SQLite 
- Frontend: HTML-CSS-Bootstap
- API: RESTful

## Authentication
- Register
- Login

## Deliverables

1. **API documentation**

*Markdown*
 **Authentication**

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| POST   | /api/login/        | Login user          |
| POST   | /api/register/     | Register user       |

---

 **Tasks**

| Method | Endpoint           | Description           | Auth Required |
|--------|--------------------|-----------------------|-------------- |
| GET    | /api/tasks/        | List all tasks        |  Bearer       |
| POST   | /api/tasks/        | Create new task       |  Bearer       |
| GET    | /api/tasks/{id}/   | Get task by ID        |  Bearer       |
| PUT    | /api/tasks/{id}/   | Update task           |  Bearer       |
| DELETE | /api/tasks/{id}/   | Delete task           |  Bearer       |

*Postman*
<img width="1822" height="689" alt="Screenshot from 2025-07-16 12-25-14" src="https://github.com/user-attachments/assets/7f5c4bba-a1fd-464d-b121-6e218d6c6f88" />
<img width="1804" height="834" alt="Screenshot from 2025-07-16 12-27-08" src="https://github.com/user-attachments/assets/a33bfe32-fd0c-4b34-95c0-389636093f73" />
<img width="1800" height="632" alt="Screenshot from 2025-07-16 12-28-11" src="https://github.com/user-attachments/assets/5a00dfe3-ef26-41f5-9bfa-3043bb5471f6" />

2. **Screenshots or screencast showing app functionality**

- Register UI:
<img width="1709" height="780" alt="image" src="https://github.com/user-attachments/assets/0d31da3b-a026-4280-a80b-8633ba74bbf7" />

- Login UI:
<img width="1810" height="575" alt="image" src="https://github.com/user-attachments/assets/8ac38249-2fda-4583-892e-b91c1d26a240" />

- Tasks List:
<img width="1885" height="680" alt="image" src="https://github.com/user-attachments/assets/5390143f-bdb6-4366-9ebd-7e519d74282d" />

- Add Tasks
<img width="1625" height="737" alt="image" src="https://github.com/user-attachments/assets/7c095b09-e01a-44fc-8b34-15fe29cc20be" />

- Individual Tasks with Edit and Delete Buttons:
<img width="1854" height="534" alt="image" src="https://github.com/user-attachments/assets/b116b903-1015-47e8-9948-cdc345f9dfa7" />
<img width="1416" height="729" alt="image" src="https://github.com/user-attachments/assets/33ef102b-b76a-4d85-b8cd-7468194a30a5" />

- *Screencast*
https://drive.google.com/file/d/1r6DfyXTaIiFwY-1iNWRCH6uhlqt2_EYp/view?usp=drive_link

3. **Deployment steps**

*Prerequisites*

Ensure the following are installed on system:

- Python:3.10
- pip
- Git

i. Clone the repository
```
git clone https://github.com/tushar-3549/Todo-App-Development
cd Todo-App-Development
```

ii. Create & activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # For Linux/macOS
```

iii. Install dependencies: `pip install -r requirements.txt`

iv. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

v. Create a superuser: `python manage.py createsuperuser`

vi. Run at localhost: `python manage.py runserver`

vii. Open in browser: `http://localhost:8000/`

*Deployment Using Docker*

i. Build the Docker image: `docker-compose build`

ii. Run the container: `docker-compose up`

iii. Access the app: `http://localhost:8000/`

iv. To stop the app: `docker-compose down`

v. Running in Docker 
```
docker-compose up -d   # Run in background
docker-compose logs -f # View logs
```

