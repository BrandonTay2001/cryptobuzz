# WARP.md

This file provides guidance to WARP (warp.dev) when working with the backend code in this directory.

## Backend Overview

**CryptoBuzz Backend** is a Flask API that serves cryptocurrency social media metrics data to the React frontend. The backend provides RESTful endpoints for news and metrics data.

## Project Structure

```
backend/
├── app.py              # Main Flask application
├── routes/             # API route blueprints
│   ├── __init__.py
│   ├── news.py         # News-related endpoints
│   └── metrics.py      # Metrics-related endpoints
├── requirements.txt    # Python dependencies
└── WARP.md            # This file
```

## Development Guidelines

- Use Flask blueprints for organizing routes
- Enable CORS for frontend communication
- Follow RESTful API conventions
- Return JSON responses with consistent structure
- Use environment variables for configuration
- Implement proper error handling and logging