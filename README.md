
---

# LifeStories

LifeStories is a Django-based web platform dedicated to sharing personal narratives. Each user on LifeStories can contribute one comprehensive story of their life, detailing various significant events and the lessons they’ve learned. This project aims to preserve these stories as lasting memories for readers and contributors alike.

## Key Features

- **Single Story per User**: Each user can share one evolving story that includes multiple events from their life.
- **Event Updates**: Users can update their story by adding new events at any time, making their narratives dynamic and current.
- **Privacy through Cartoonification**: For users concerned about privacy, LifeStories offers an option to 'cartoonify' images associated with their stories, providing anonymity while maintaining personal expression.
- **Inclusive Storytelling**: LifeStories encourages people of all ages to share their experiences, not just those who have lived long lives. Whether you're young or old, your story matters.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: SQLite (development), PostgreSQL (production),
- **Frontend**: HTML, CSS (Bootstrap for styling), JavaScript
- **Additional Tools**:  Cloudinary, whitenose, django-auto-logout, django-cleanup (will add Docker) to further simplify the process of deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:c

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lifestories.git
```

2. Navigate to the project directory:
```bash
cd lifestories
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Migrate the database:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000` in your browser to view the application.

7. Have your .env file to proceed with the web functionalities, feel free to adjust from settings.py to remove unecessary utilities if your working on local
```bash
DEBUG=# either False Or True
PGDATABASE=# your database name
PGHOST=# your database host
PGPASSWORD=# your database password
PGPORT=# your database port
PGUSER=# your database user
SECRET_KEY=# your secret key, e.g., qxwna35$pck

# Make sure to have your media file storage hosting service API key if you deploy, else remove cloudinary from installed_apps in settings.py
CLOUDINARY_CLOUD_NAME=# your Cloudinary cloud name
CLOUDINARY_API_KEY=# your Cloudinary API key
CLOUDINARY_API_SECRET=# your Cloudinary API secret

```

## Contributing

We welcome contributions to LifeStories! If you have suggestions or improvements, please fork the repository and submit a pull request. You can also open an issue if you find bugs or have feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

---
