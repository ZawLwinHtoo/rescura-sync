# Rescura Sync ⚡
### Autonomous Humanitarian Logistics & Disaster Dispatch Platform

Rescura Sync is a full-stack real-time emergency response platform that coordinates disaster alerts from GDACS, estimates UN Sphere-standard humanitarian relief supplies (water, food rations, trauma kits), calculates multi-modal logistics transit durations (Land, Air, Water), and exports official Emergency Action Plans.

---

## 🚀 One-Click Quick Start (Windows)

Requires Python 3.10 or later and internet access for the first dependency installation. SQLite supports the local dashboard without cloud database credentials.

```sh
python run.py
```

This creates `backend/.venv`, installs declared dependencies when they change, and serves the dashboard at http://127.0.0.1:8000. No cloud keys are created or configured automatically.

For a demonstration without live disaster feed requests:

```sh
python run.py --offline-feed
```

This uses a separate `backend/demo.db` and pauses remote disaster feeds. Maps and external basemap tiles can still require internet access. The UI's test-emergency action can create explicitly simulated events.

The existing Windows launchers are also available:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ZawLwinHtoo/rescura-sync.git
   cd rescura-sync
   ```

2. **Double-click `run.bat` (or `start.bat`)**:
   * ✅ Automatically checks and verifies Python 3.10+ installation.
   * ✅ Defaults to a local SQLite database; optional cloud services need your own configuration.
   * ✅ Creates an isolated virtual environment (`backend\.venv`).
   * ✅ Installs all required dependencies (`fastapi`, `uvicorn`, `scikit-learn`, `pandas`, `fpdf2`, etc.).
   * ✅ Starts the local backend server at `http://127.0.0.1:8000`.
   * ✅ Automatically launches your default browser to the interactive dashboard.

---

## 🛠️ Tech Stack & Architecture

* **Backend**: FastAPI (Python 3.10+), SQLAlchemy 2.0 Async, SQLite/PostgreSQL, Scikit-Learn ML Model, FPDF2 Report Engine.
* **Frontend**: Pure Vanilla HTML5/CSS3/JavaScript (No complex build steps required, fully served by FastAPI at `/`).
* **External Integrations**: GDACS Real-Time Live Feeds, Supabase Cloud Database & WebSockets, OpenStreetMap GIS routing.

## Docker

```sh
docker compose up --build
```

The image includes both the API and the dashboard. PostgreSQL must pass its health check before the API starts. The PostgreSQL driver is included in the backend requirements. The bundled database credentials are for local development.

## Verification

```sh
cd backend
python -m pip install -r requirements.txt
python run_tests.py
```

The API suite uses a temporary SQLite database and a fixed disaster feed fixture. It exercises status, feedback, inventory intake/issue/adjustment, transaction history, dispatch, mission display, and resolution without modifying an operator's database or fetching live disasters.

This repository is a portfolio demonstration. Its generated logistics estimates and sample depot inventory are not validated emergency operations instructions. The optional Expo mobile application has its own dependencies and environment configuration in `rescura-mobile/`.

---

## 📄 License
Humanitarian Open License. Built for disaster relief operations and rapid humanitarian emergency response.
