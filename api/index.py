import sys
import traceback
from pathlib import Path

# Add backend directory to sys.path so backend imports work seamlessly on Vercel
ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

try:
    from main import app  # noqa: E402
except Exception:
    from fastapi import FastAPI
    from fastapi.responses import PlainTextResponse

    err_msg = traceback.format_exc()
    app = FastAPI()

    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
    async def debug_err(path: str):
        return PlainTextResponse(f"Startup Exception on Vercel:\n{err_msg}", status_code=500)
