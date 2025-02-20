# Fleet Scraper

A comprehensive web scraper and API for collecting and managing vehicle fleet data. This project scrapes detailed car specifications from various manufacturers and provides a REST API to access the collected data.

## Features

Current Features:
- Automated web scraping of car specifications using Playwright
- Support for multiple car makes, models, and sub-models
- RESTful API for data access
- PostgreSQL database for data storage
- Django-based backend with robust data models
- Configurable year range for data collection
- Containerized application with Docker
- Easy deployment with Docker Compose

Upcoming Features:
- Command Line Interface (CLI) for data management and queries
- Web dashboard for data visualization
- Advanced search and filtering capabilities
- Export functionality (CSV, JSON, Excel)
- Vehicle comparison tool
- Analytics and reporting features

## Prerequisites

- Docker and Docker Compose
- Python 3.x (for local development)

## Project Structure
```
.
├── src/
│   ├── api/           # Django REST API
│   ├── scraper/       # Web scraper implementation
│   └── .env          # Environment variables
├── docker-compose.yml
├── start.sh          # Startup script
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fleet-scraper.git
cd fleet-scraper
```

2. Set up environment variables:
Create a `.env` file in the `src` directory with the following variables:
```env
# Scraper Configuration
SITE_SCRAPER="https://www.automobile-catalog.com/"
STARTING_SCRAP_YEAR="2020"

# Database Configuration
POSTGRES_DB="fleetdb"
POSTGRES_USER="fleetuser"
POSTGRES_PASSWORD="fleetpass"
POSTGRES_HOST="fleet_db"
POSTGRES_PORT="5432"

# Django Configuration
SECRET_KEY="django-insecure-1cn_xd7&mc1cnrs*37@nrmx-7i$=0g_)k8bclnc6=x+%^a6#sq"
DJANGO_HOST="http://127.0.0.1"
DJANGO_PORT="8000"
```

## Deployment

### Using Docker (Recommended)

1. Make the startup script executable:
```bash
chmod +x start.sh
```

2. Run the startup script:
```bash
./start.sh
```

This will:
- Start the PostgreSQL database container
- Build and start the Django API container
- Run database migrations
- Start the web scraper

The services will be available at:
- Django API: `http://localhost:8000`
- PostgreSQL: `localhost:5432`

### Manual Setup (Development)

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Start the PostgreSQL database:
```bash
docker-compose up -d postgres
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Start the scraper:
```bash
cd src/scraper
python scraper.py
```

## Usage

### API Endpoints

- `POST /api/make` - Create a new car make
- `POST /api/model` - Create a new car model
- `POST /api/submodel` - Create a new car sub-model
- `POST /api/car` - Create a new car entry
- `GET /api/search` - Search cars with filters

#### Search Parameters

The search endpoint supports the following filters:
- `make` - Filter by car make
- `model` - Filter by car model
- `sub_model` - Filter by sub-model
- `category` - Filter by car category

Example:
```
GET /api/search?make=toyota&category=suv
```

## Project Roadmap

### Phase 1 - Core Features (Completed)
- ✅ Basic scraper implementation
- ✅ Database models and migrations
- ✅ REST API endpoints
- ✅ Docker setup
- ✅ Automated deployment

### Phase 2 - CLI Implementation (In Progress)
- ✅ Command line interface structure
- 🔄 Basic CRUD operations
- ✅ Search and filter commands
- ✅ Export functionality
- 🔄 Configuration management

### Phase 3 - Web Dashboard (Planned)
- ⏳ User interface design
- ⏳ Frontend implementation
- ⏳ Authentication system
- ⏳ Advanced search interface
- ⏳ Vehicle comparison tool
- ⏳ Analytics dashboard

## Testing

Run the test suite:
```bash
docker-compose exec web python manage.py test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Dependencies

Key dependencies include:
- Django 5.1.6
- Django REST Framework 3.15.2
- Playwright 1.50.0
- PostgreSQL (latest)
- Gunicorn 23.0.0
- Python-dotenv 1.0.1
- Pydantic 2.10.6

See `requirements.txt` for a complete list of dependencies.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
