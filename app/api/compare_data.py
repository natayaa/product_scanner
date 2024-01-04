from fastapi import APIRouter, status, HTTPException, Cookie
from fastapi.responses import JSONResponse

from database.product_connection import ProductConnection
from database.log_scan import Logscan

# jsonbody
from api.model.compare_payload import CompareBody

scanner = APIRouter(tags=["Scanner API Endpoint"], prefix="/app/resources/api/v1/data/model")
# initiate ProducttConnection
products = ProductConnection()
logscan = Logscan()

@scanner.post("/compare", response_class=JSONResponse)
async def compare_data(payload: CompareBody):
    # retrieve data from user and then compare based on registered item in database
    check_datas = products.check_data(tv_model_input=payload.tv_model, remote_barcode_input=payload.remote_tv_barcode)
    if check_datas:
        # write log into table
        write_scanned = logscan.insert_logscan(incharge="user", result="OK", )
        return JSONResponse(content={"message": f"{payload.tv_model} is matched with {payload.remote_tv_barcode}",
                                     "success": check_datas},
                            status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": f"{payload.tv_model} is not matched with {payload.remote_tv_barcode}",
                                     "success": check_datas},
                            status_code=status.HTTP_400_BAD_REQUEST)