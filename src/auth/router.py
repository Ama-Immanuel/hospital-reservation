from fastapi import APIRouter

router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)   

@router.get('/login')
def login():
    return{"login"}


@router.get('/register')
def register():
    return("register")
