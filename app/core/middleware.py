import time
from app.core.logger import logger

async def log_timing(request, call_next):

    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    logger.info(
        f"{request.method} {request.url.path} took {duration:.3f}s"
    )

    response.headers["X-Process-Time"] = str(duration)

    return response