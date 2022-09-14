from pydantic import BaseModel, Field
from typing import Dict

class Coverage(BaseModel):
    class Config:
        allow_population_by_field_name=True

    g2: bool = Field(alias="2G")
    g3: bool = Field(alias="3G")
    g4: bool = Field(alias="4G")
    
    
class Networks(BaseModel):
    available_networks: Dict[str, Coverage]



