Worms - Architecture

1. Architecture Overview
Worms will use a client-server architecture:
 -React/Vite frontend handles the user interface.
 -FastAPI backend handles business logic and API requests.
 -PostgreSQL stores application data.
 -The frontend communicates with the backend through HTTP/REST APIs.

2. Technology Stack
Layer       Technology
Frontend    React + Vite
Language    JavaScript
Styling     CSS
Backend     Python + FastAPI
Database    PostgreSQL
API         REST
Authentication  JWT
Version Control Git + GitHub
Development     VS Code
Containerization    Docker //later

3. High-Level Architecture
User -> React Frontend -(HTTP/REST)-> FastAPI Backend -> PostgreSQL Database

4. Responsibilities

Frontend
-Display the application UI
-Handle user interactions
-Send API requests
-Display API responses

Backend
-Authenticate users
-Validate incoming data
-Apply application/business rules
-Handle CRUD operations
-Communicate with PostgreSQL

Database
-Store users
-Store books
-Store reading status
-Store reading progress
-Store book access information
-Store ratings/reviews

5. Authentication
Users will authenticate through the FastAPI backend. Passwords will be securely hashed before being stored. Successful authentication will provide a JWT that the frontend can use when making authenticated API requests.

6. Development Approach
Worms will be developed in stages, beginning with the core account and library functionality before implementing secondary features such as the TBR randomizer and reviews.
