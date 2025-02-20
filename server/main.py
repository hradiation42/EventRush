from http.client import HTTPResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from model import SignUp, Login, Register


from database import signin
from database import register
from database import register_event


app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register", status_code=201)
async def registering_signup(signup: SignUp):
    response = await register(signup.dict())
    if response:
        print("post successfull!")
        return 
    raise HTTPException(400, "something went wrong/bad request")
    

@app.post("/login", response_model=SignUp, status_code=200) #removed response model as data not fetched from the database 
async def register_login(login:Login):
    # details = login.dict()
    # Email = login.email
    response = await signin(login)
    if response:
        return response
    # raise HTTPException(400, f"something went wrong/bad request {}")



# @app.post("/cultural", response_model=cultural_events, status_code=200)
# async def coding_events_func(event: cultural_events):
#     response = await register_cultural_events(event)
#     if response:
#         return response
#     raise HTTPException(404,"there are no events to register")


# TO SEND ID TO FRONTEND USING RESPONSE

# @app.post("/cultural", status_code=200)
# async def event_id(event:id):
#     response = await event_id(event)
#     if response:
#         return response
#     raise HTTPException(404, "there are no events to register")


@app.post("/registeration",status_code=200)
async def registeration_event(register: Register):
    response = await register_event(register.dict())
    if response:
        return 
    raise HTTPException(400, "something went wrong / bad request")
    
    
@app.post("/user", status_code=200)
async def userdetails():
    return 0
