from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
    {
        "id": 3,
        "author": "John Smith",
        "title": "Getting Started with FastAPI",
        "content": "FastAPI is a modern Python framework for building APIs quickly and efficiently.",
        "date_posted": "April 22, 2025",
    },
    {
        "id": 4,
        "author": "Alice Johnson",
        "title": "Understanding Python Decorators",
        "content": "Decorators allow you to extend the behavior of functions without modifying their original code.",
        "date_posted": "April 23, 2025",
    },
    {
        "id": 5,
        "author": "Michael Brown",
        "title": "Why Learn Django?",
        "content": "Django is a powerful Python web framework that provides everything you need to build scalable web applications.",
        "date_posted": "April 24, 2025",
    },
    {
        "id": 6,
        "author": "Sarah Wilson",
        "title": "REST API Best Practices",
        "content": "Building clean REST APIs requires proper HTTP methods, meaningful status codes, and consistent URL naming conventions.",
        "date_posted": "April 25, 2025",
    },
    {
        "id": 7,
        "author": "David Miller",
        "title": "Introduction to PostgreSQL",
        "content": "PostgreSQL is a powerful open-source relational database management system used in modern applications.",
        "date_posted": "April 26, 2025",
    },
    {
        "id": 8,
        "author": "Emily Davis",
        "title": "Python List Comprehensions",
        "content": "List comprehensions provide a concise and readable way to create lists in Python.",
        "date_posted": "April 27, 2025",
    },
    {
        "id": 9,
        "author": "Robert Wilson",
        "title": "Understanding HTTP Status Codes",
        "content": "HTTP status codes help clients understand whether a server request was successful or encountered an error.",
        "date_posted": "April 28, 2025",
    },
    {
        "id": 10,
        "author": "Sophia Martinez",
        "title": "Building Your First React Application",
        "content": "React makes it easier to build interactive user interfaces using reusable components and state management.",
        "date_posted": "April 29, 2025",
    },
]


@app.get("/")
def home():
    return {"message": "Hello World!"}


@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/test-html", response_class=HTMLResponse, include_in_schema=False)
@app.get("/test-two-url", response_class=HTMLResponse, include_in_schema=False)
def get_html():
    return f"<h1>{posts[0]['title']}</h1>"
