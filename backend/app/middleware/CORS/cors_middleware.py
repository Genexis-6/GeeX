from fastapi.middleware.cors import CORSMiddleware



# accepted urls
origins = [
    "http://localhost:5173"
]

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=["*"],
        allow_origins=origins,
        allow_methods=["*"],
    )
    


