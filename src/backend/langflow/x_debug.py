import sys

sys.path.append("src/backend")

import uvicorn
from langflow.main import create_app
# from langflow.__main__ import get_number_of_workers

app = create_app()
uvicorn.run(
    "langflow.main:create_app",
    host="127.0.0.1",
    port=6006,
    log_level="debug",
)
