from pydantic import BaseModel

class TrainParameters(BaseModel):
    '''DTO for data coming from client-side.'''
    model: str