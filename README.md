# Digital Institutional Resource Library

A web-based academic resource management platform developed as a five-member
team project at Manav Rachna University. The system was designed to help
students and faculty upload, organise, search and manage institutional
documents through role-based interfaces.

> This repository is maintained as a portfolio copy of the original team
> project. My primary contribution was frontend development using React,
> along with some database-related integration. The project was subsequently
> continued and extended by junior students after I left the university.

## Features

- User registration and authentication
- Document upload and resource management
- Search and filtering of academic documents
- Faculty and administrator dashboards
- Category and department management
- User and group management
- Document request and deletion workflows

## Tech Stack

### Frontend
- React
- JavaScript
- Vite
- Tailwind CSS
- Redux Toolkit
- React Router
- Axios

### Backend
- Python
- Django
- Django REST Framework
- JWT authentication

### Database
- MongoDB
- SQLite for Django application data

## My Contribution

I worked primarily on the frontend of the application as part of the
five-member development team.

My contributions included:

- Developing and supporting React-based user interfaces
- Working on frontend navigation and application workflows
- Integrating frontend components with backend APIs
- Contributing to database-related integration and data handling
- Collaborating with the wider team on feature implementation and testing

The codebase was later continued and extended by junior students, so some
features in the current repository were developed after my involvement.

## Project Architecture

Frontend (React)
        |
        | REST API
        v
Backend (Django / Django REST Framework)
        |
        +---- MongoDB
        |
        +---- SQLite / Django models

## Running Locally

### Frontend

```bash
cd frontend
npm install
npm run dev
