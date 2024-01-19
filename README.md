# Streaker API
API for [streakapp](https://github.com/esmond-adjei/streakapp) <br>
Streakapp is a useful tool for keeping track of your daily tasks and habits ensuring you stay motivated to achieve your goals. <br>

## Installation
1. Clone the repo
```bash
git clone https://github.com/esmond-adjei/streaker.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. change directory into the project
```bash
cd streaker
```

4. Run the app
```bash
python manage.py runserver
```

## API endpoints

### Task
| Endpoint | Method | Description | Status |
| --- | --- | --- | --- |
| /api/task/ | GET | Get all tasks | :heavy_check_mark: |
| /api/task/{id} | GET | Get a task by id | :heavy_check_mark: |
| /api/task/{id} | PUT | Update a task by id | :heavy_check_mark: |
| /api/task/{id} | DELETE | Delete a task by id | :heavy_check_mark: |

### Streak
| Endpoint | Method | Description | Status |
| --- | --- | --- | --- |
| /api/streak/ | GET | Get all streaks | :heavy_check_mark: |
| /api/streak/{id} | GET | Get a streak by id | :heavy_check_mark: |
| /api/streak/{id} | PUT | Update a streak by id | :heavy_check_mark: |
| /api/streak/{id} | DELETE | Delete a streak by id | :heavy_check_mark: |


### User
| Endpoint | Method | Description | Status |
| --- | --- | --- | --- |
| /api/user/register | POST | Register a new user | :x: |
| /api/user/login | POST | Login a user | :x: |
| /api/user/logout | POST | Logout a user | :x: |
| /api/user/ | GET | Get all users | :x: |
| /api/user/{id} | GET | Get a user by id | :x: |
| /api/user/{id} | PUT | Update a user by id | :x: |
| /api/user/{id} | DELETE | Delete a user by id | :x: |
