from fastapi import APIRouter, status, HTTPException, Cookie, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import database
from database.log_scan import Logscan
# init Logscan
scanner_logs = Logscan()

TITLE_PAGE = "LOGSCAN Page"


logscan_page = APIRouter(tags=["Logscan Page"])
template = Jinja2Templates(directory="templates/")


@logscan_page.get("/logscan-page", response_class=HTMLResponse)
async def logscan_page_load(request: Request, search: str = None, limit: int = 10, offset: int = 0):
    offsets = int((offset - 1) * limit)
    records_logs = scanner_logs.show_logs(search=search, limit=limit, offset=offsets)
    retval_logscan = {"request": request, "title": TITLE_PAGE, "logscan_data": records_logs.get("data_logs"), 
                      "total_records": records_logs.get("total_records"),
                      "limit": limit, "page": offset}
    
    return template.TemplateResponse("logscan.html", context=retval_logscan, status_code=status.HTTP_200_OK)