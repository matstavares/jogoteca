# 🎮 Jogoteca

A web application developed with Flask to manage a game library. Allows you to register, edit, view, and delete games with a user authentication system.

## 📋 Features

- ✅ **Game listing**: View all games registered in the library
- ✅ **Game registration**: Add new games with name, category, console, and cover image
- ✅ **Game editing**: Update information of existing games
- ✅ **Game deletion**: Remove games from the library
- ✅ **Authentication system**: User login and logout
- ✅ **Image upload**: Upload cover images for games
- ✅ **CSRF protection**: Security against Cross-Site Request Forgery attacks
- ✅ **Password encryption**: Passwords protected with bcrypt

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database
- **Flask-WTF** - Forms and CSRF protection
- **Flask-Bcrypt** - Password encryption
- **MySQL** - Relational database
- **WTForms** - Form validation
- **Jinja2** - Template engine

## 📦 Prerequisites

Before you begin, make sure you have installed:

- Python 3.7 or higher
- MySQL Server
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/jogoteca.git
cd jogoteca
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**
```bash
# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

1. **Configure the MySQL database:**

   Create a database named `jogoteca` in MySQL:
```sql
CREATE DATABASE jogoteca;
```

2. **Configure database credentials:**

   Edit the `config.py` file and adjust MySQL credentials:
```python
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='your_username',
        senha='your_password',
        servidor='localhost',
        database='jogoteca'
    )
```

3. **Configure the SECRET_KEY:**

   Change the `SECRET_KEY` in the `config.py` file to a secure key:
```python
SECRET_KEY = "your_secret_key_here"
```

4. **Prepare the database:**

   Run the script to create the tables:
```bash
python prepara_banco.py
```

## 🎯 Usage

1. **Start the Flask server:**
```bash
python jogoteca.py
```

2. **Access the application:**

   Open your browser and navigate to: `http://localhost:5000`

3. **Login:**

   - Access the login page
   - Use your credentials to authenticate
   - After logging in, you can add, edit, and delete games

## 📁 Project Structure

```
jogoteca/
│
├── jogoteca.py          # Main application file
├── models.py            # Database models (Jogos, Usuarios)
├── views_game.py        # Routes related to games
├── views_user.py        # Routes related to users
├── helpers.py           # Helper functions and forms
├── config.py            # Application configuration
├── prepara_banco.py     # Script to initialize the database
├── requirements.txt     # Project dependencies
├── templates/           # HTML templates
│   ├── template.html
│   ├── lista.html
│   ├── novo.html
│   ├── editar.html
│   └── login.html
├── static/              # Static files (CSS, JS, images)
└── uploads/            # Directory for game cover uploads
```

## 🔐 Security

- Passwords are encrypted using bcrypt
- CSRF protection implemented on all forms
- Session authentication for sensitive operations
- Form validation with WTForms

## 📝 Data Models

### Jogos (Games)
- `id`: Unique identifier (primary key)
- `nome`: Game name (max 50 characters)
- `categoria`: Game category (max 40 characters)
- `console`: Game console (max 20 characters)

### Usuarios (Users)
- `nickname`: User nickname (primary key, max 8 characters)
- `nome`: Full name (max 20 characters)
- `senha`: Encrypted password (max 100 characters)

## 🤝 Contributing

Contributions are always welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m 'Add MyFeature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under GPLv3 terms.

## 👨‍💻 Author

Developed as a Flask framework learning project.