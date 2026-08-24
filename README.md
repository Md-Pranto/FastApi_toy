# Day 8: FastAPI Basics

Toy API built to learn FastAPI, Pydantic models, path/query parameters, and async endpoints.

## Endpoints
- `GET /` - welcome message
- `GET /mango/{mango_type}` - returns a fun message based on mango type
- `POST /mango/details/{mango_id}` - accepts a `MangoDes` body and returns price with VAT if provided
- `GET /item_details/{item_id}` - demonstrates query parameters

Run with:
uvicorn main:app --reload