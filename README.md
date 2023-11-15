# caregigs
CareGiGs

### Clone this project:

```
git clone [repo]
```

## Backend:
__________________
### Go to Django Backend:

```
cd backend
```

### Create Virtual Environment:

```commandline
python -m venv venv
source venv/bin/activate
```

#### Install requirements:

```commandline
pip install -r requirements.txt
```

### Create .env file and configure variables for database, email and others: 

```commandline
cp .env.example .env
```

#### Migrate database:

```commandline
python manage.py migrate
```


#### Create a superuser:

```commandline
python manage.py createsuperuser
```

### Run with:

```commandline
python manage.py runserver
```

### Run flake8 and isort . --interactive before commit:

```commandline
flake8
```

```commandline
isort . --interactive
```


__________________
