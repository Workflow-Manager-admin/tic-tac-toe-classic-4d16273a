# Tic Tac Toe Backend (Django)

This directory implements the backend component for the classic Tic Tac Toe game architecture. The backend is supplied as a Django application exposing a minimal API (currently a health-check endpoint and stub for future game history), laying the foundation for service monitoring and future extensibility.

## Overview

- **Purpose:**  
  - Presently, the backend serves as a proof of liveness (health endpoint). It is designed for future expansion—such as saving game history, user profiles, statistics, or enabling remote multiplayer.
  - This is a separation-of-concerns demonstration: keeping game logic and UI in the frontend, while backend handles service status, monitoring, and future persistence or networking needs.

## Project Structure

```
backend/
  manage.py               # Standard Django management interface
  requirements.txt        # Python dependencies
  config/                 # Django project settings, URLs, WSGI/ASGI entrypoints
  api/                    # App for REST API endpoints
    views.py              # Health endpoint and game history stub/API
    models.py             # Stub model for extensible game history records
    urls.py               # Endpoint URL configuration
    migrations/           # Django migration files
    management/commands/  # Custom command to generate OpenAPI spec
  interfaces/openapi.json # OpenAPI auto-generated spec for the REST API
```

## Exposed API

### Health Endpoint

- **Route:** `/api/health/`
- **Method:** GET
- **Purpose:** Allows deployment scripts, monitoring, and the frontend to verify the backend service is live.
- **Response:**
  ```json
  {
    "message": "Server is up!"
  }
  ```

### Game History API (Stub)

- **Route:** `/api/game-history/`
- **Method:** GET
- **Purpose:** Placeholder endpoint for listing previously played games. Returns an empty list. Provides a natural expansion point for storing games, stats, or leaderboards as needed.
- **Response:**
  ```json
  {
    "games": []
  }
  ```

## Division of Responsibilities

- **Backend:**
  - Provides REST API endpoints for system health, and could offer persistent storage or multiplayer support in future.
  - No move validation or game logic is implemented; gameplay is always managed in the frontend.
- **Frontend (Flutter Application):**
  - Handles all game rules, state, and user interactions locally.
  - Might call backend endpoints for health check or, in future, to sync data.

### Extensibility and Future Improvements

- **Game History:**  
  Expand `api.models.GameHistory` to store game boards, winners, timestamps, or player identities.
- **New APIs:**  
  Add endpoints to record new games, retrieve stats, or support matchmaking.
- **Authentication:**  
  Add user accounts if remote or social features are planned.
- **Network Play:**  
  Backend can manage remote player sessions and move synchronization.

## Running and Local Development

1. Ensure Python 3 and pip are installed.
2. Install requirements:

   ```
   pip install -r requirements.txt
   ```

3. Run migrations (no game table fields are required for current version, but migrations exist):

   ```
   python manage.py migrate
   ```

4. Start the development server:

   ```
   python manage.py runserver
   ```

   The API will be at http://localhost:8000/api/ and the OpenAPI/Swagger UI at http://localhost:8000/docs/

## Theming and Style (for API docs)

- Documentation styling is provided via Swagger UI and Redoc interfaces.
- There is currently no end-user UI; theming is only relevant to users of the API docs.

## Container Interaction

- At present, the frontend and backend are loosely coupled: the frontend only requires the backend to be live if future enhancements use server-stored data.
- For cloud or production deployment, the backend may provide centralized analytics, auditing, or remote game play—without affecting the local play fallback in the frontend.

----

For API schema, see [interfaces/openapi.json](../interfaces/openapi.json) or navigate to the `/docs/` endpoint after starting the server.
