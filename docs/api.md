# API Documentation

## Overview

The Document Intelligence Platform provides a RESTful API built with FastAPI, featuring automatic OpenAPI documentation, type safety, and async support.

## Base URL

- Development: `http://localhost:8000`
- Production: TBD

## Authentication

Currently, the API is open for development. Authentication will be implemented in future versions.

## Endpoints

### System Endpoints

#### GET /
Root endpoint providing basic API information.

**Response:**
```json
{
  "message": "Document Intelligence Platform API",
  "version": "0.1.0"
}
```

#### GET /api/v1/health
Health check endpoint for monitoring and load balancer probes.

**Response:**
```json
{
  "status": "healthy",
  "service": "document-intelligence-platform"
}
```

### Document Endpoints (Planned)

The following endpoints are planned for implementation:

- `POST /api/v1/documents/upload` - Upload document
- `GET /api/v1/documents/{document_id}` - Get document details
- `GET /api/v1/documents` - List documents with pagination
- `DELETE /api/v1/documents/{document_id}` - Delete document

### Search Endpoints (Planned)

- `POST /api/v1/search/semantic` - Perform semantic search
- `GET /api/v1/search/history` - Get search history

## Interactive Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: Available at `/docs`
- **ReDoc**: Available at `/redoc`

These interfaces provide:
- Complete API schema
- Interactive request/response testing
- Automatic validation documentation
- Type information and examples

## Error Handling

The API follows standard HTTP status codes and returns structured error responses:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {},
    "timestamp": "2024-01-15T10:30:00Z"
  }
}
```

## Type Safety

The API is built with comprehensive type hints and Pydantic models for:
- Request/response validation
- Automatic documentation generation
- Runtime type checking
- Better IDE support and development experience

## CORS Configuration

CORS is configured to allow all origins in development. This will be restricted in production environments.
