from fastapi import FastAPI
from .routers import documentation, user, event, mentor, partner, alumni, faq, contact, blog

app = FastAPI()

app.include_router(documentation.router)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(mentor.router)
app.include_router(partner.router)
app.include_router(alumni.router)
app.include_router(faq.router)
app.include_router(contact.router)
app.include_router(blog.router)

# uhh might add on to this later