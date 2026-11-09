"""Bootstrap and run the local dashboard without writing cloud credentials."""
from pathlib import Path
import argparse
import hashlib
import os
import subprocess
import sys
import venv


def main():
    parser = argparse.ArgumentParser(description="Run the Rescura Sync local demonstration")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--offline-feed", action="store_true", help="Disable live disaster feeds and use a separate local demo database")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or later is required")
    if not 1 <= args.port <= 65535:
        parser.error("port must be between 1 and 65535")
    backend = Path(__file__).resolve().parent / "backend"
    environment = backend / ".venv"
    python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not python.exists():
        print("Creating isolated Python environment...", flush=True)
        venv.EnvBuilder(with_pip=True).create(environment)
    requirements = backend / "requirements.txt"
    digest = hashlib.sha256(requirements.read_bytes()).hexdigest()
    marker = environment / ".requirements-sha256"
    if not marker.exists() or marker.read_text() != digest:
        subprocess.run([str(python), "-m", "pip", "install", "-r", str(requirements)], check=True)
        marker.write_text(digest)
    config = os.environ.copy()
    if args.offline_feed:
        config["RESCURA_OFFLINE"] = "1"
        config["DATABASE_URL"] = "sqlite+aiosqlite:///" + (backend / "demo.db").as_posix()
        print("Live disaster feeds paused. Using the separate local demo database.", flush=True)
    print(f"Dashboard: http://127.0.0.1:{args.port}", flush=True)
    return subprocess.call([str(python), "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", str(args.port)], cwd=backend, env=config)


if __name__ == "__main__":
    raise SystemExit(main())
