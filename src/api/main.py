from fastapi import FastAPI, HTTPException
from .network_model import Networks
from typing import Dict
from .address_not_found_error import AddressNotFoundError
from .get_coverages import get_coverage_from_address

app = FastAPI()


@app.get("/", response_model=Networks)
async def network_coverage(q: str) -> Networks:
    '''
    API main road.
    One query parameter `q` for an address.
    If no address is found, a 404 error is raised
    '''
    try:
        return get_coverage_from_address(q)
    except AddressNotFoundError:
        raise HTTPException(status_code=404, detail="Address not found")
    except:
        raise
