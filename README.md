# Digital Institutional Resource Library

A web-based academic resource management platform developed as a **five-member university team project** at Manav Rachna University.

The platform was designed to help students, faculty members, and administrators upload, organise, search, manage, and retrieve academic documents through role-based interfaces.

> **Project context:** This repository is maintained as a portfolio copy of the original team project. My primary contribution was in **frontend development using React**, along with some involvement in **database-related integration and data handling**. The project was later continued and extended by junior students after my involvement ended.

---

## Overview

The Digital Institutional Resource Library was created to provide a centralised system for managing institutional academic resources.

Instead of relying on scattered files and manual document sharing, the application provides a structured interface where authorised users can access and manage resources based on their role.

The project combines a modern React frontend with a Django-based backend and database functionality.

---

## Key Features

The current codebase includes functionality for:

- User registration and login
- Role-based user access
- Academic document upload and management
- Document search and retrieval
- Document editing
- Categories and department management
- Faculty resource management
- Administrator dashboard functionality
- User management
- Group management
- Document request workflows
- Document deletion/request workflows
- Authentication and protected application routes

---

## Tech Stack

### Frontend

- React
- JavaScript
- Vite
- Tailwind CSS
- Redux Toolkit
- React Router
- Axios
- Framer Motion
- Font Awesome
- Heroicons

### Backend

- Python
- Django
- Django REST Framework
- Django REST Framework Simple JWT
- Django CORS Headers

### Database / Data

- MongoDB
- PyMongo
- Django application models
- Pandas

### Development Tools

- Git
- GitHub
- VS Code
- npm
- REST APIs

---

## My Contribution

I worked primarily on the **frontend development** of the project as part of the original five-member team.

My involvement included:

- Developing and supporting React-based user interfaces
- Working on frontend pages and navigation flows
- Supporting integration between frontend components and backend APIs
- Contributing to database-related integration and data handling
- Working with the team to translate project requirements into application features
- Supporting testing and integration of frontend functionality

Because the project was later continued by junior students, the current repository contains functionality that may have been added or modified after my involvement.

I therefore only claim responsibility for the areas I personally contributed to.

---

## Application Structure

The project follows a frontend/backend architecture:

```text
Digital-Institutional-Resource-Library
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── repository/
│   ├── library/
│   │   ├── databases/
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── permissions.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── repository/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
└── README.md
