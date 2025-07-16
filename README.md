# AI Document Platform

A document intelligence platform that demonstrates enterprise-grade software engineering practices and modern AI/ML integration patterns.

## Project Goals

This platform showcases:

- **Modern Python Architecture**: Clean architecture with FastAPI, async programming, and dependency injection
- **AI/ML Integration**: Real-world implementation of OpenAI embeddings, vector search, and semantic analysis
- **Cloud-Native Design**: Containerized microservices with AWS integration and scalable infrastructure
- **Production Best Practices**: Comprehensive testing, CI/CD, monitoring, and security patterns
- **Developer Experience**: Modern tooling with UV, pre-commit hooks, and automated code quality

## What This Platform Does

Transform your document workflows with AI-powered intelligence:
- **Smart Document Processing**: Upload PDFs and text files with automatic content extraction and analysis
- **Semantic Search**: Find documents by meaning, not just keywords, using vector embeddings
- **AI Summarization**: Get instant summaries and key insights from lengthy documents
- **RESTful API**: Production-ready API with interactive documentation and async processing

## Features

- Document upload and storage (PDF, text files)
- AI-powered text extraction and analysis
- Semantic search using vector embeddings
- RESTful API with FastAPI
- Background task processing with Celery
- Containerized deployment with Docker and Kubernetes
- Modern Python tooling with UV package manager

## Technology Stack

### Backend
- **Python 3.9+** - Core language
- **FastAPI** - Web framework with async support
- **UV** - Package and environment management
- **SQLAlchemy** - Database ORM with async support
- **Celery** - Background task processing

### AI/ML
- **OpenAI API** - Text embeddings and summarization
- **Pinecone** - Vector database for semantic search
- **PyPDF2/pdfplumber** - PDF text extraction

### Infrastructure
- **Docker** - Containerization
- **Kubernetes** - Container orchestration
- **AWS S3** - Object storage
- **PostgreSQL** - Relational database
- **Redis** - Caching and task queue

## Quick Start

### Prerequisites

- Python 3.9+
- UV package manager
- Docker and Docker Compose
- AWS account (for S3 storage)
- OpenAI API key
- Pinecone account

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-document-platform
```

2. Install dependencies:
```bash
uv sync --dev
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start the development environment:
```bash
docker-compose up -d
```

5. Run database migrations:
```bash
uv run alembic upgrade head
```

6. Start the development server:
```bash
uv run uvicorn ai_document_platform.api.main:app --reload
```

## Development

### Code Quality

This project uses modern Python tooling for code quality:

- **Black** - Code formatting
- **Ruff** - Fast Python linter
- **MyPy** - Static type checking
- **Pre-commit** - Git hooks for code quality

Run code quality checks:
```bash
uv run black src/ tests/
uv run ruff check src/ tests/
uv run mypy src/
```

### Testing

Run tests with pytest:
```bash
uv run pytest
```

Run tests with coverage:
```bash
uv run pytest --cov=src --cov-report=html
```

### Docker Development

Build and run with Docker Compose:
```bash
docker-compose up --build
```

## API Documentation

The API is built with comprehensive type hints and automatic validation for better reliability and developer experience.

Once the server is running, visit:
- Interactive API docs: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc
- API reference: [docs/api.md](docs/api.md)

## Project Structure

```
├── src/ai_document_platform/    # Main application code
│   ├── api/                     # FastAPI routes and endpoints
│   ├── services/                # Business logic layer
│   ├── models/                  # Data models and schemas
│   ├── repositories/            # Data access layer
│   ├── clients/                 # External service clients
│   └── utils/                   # Utility functions
├── tests/                       # Test suite
│   ├── unit/                    # Unit tests
│   ├── integration/             # Integration tests
│   └── e2e/                     # End-to-end tests
├── docker/                      # Docker configuration
├── scripts/                     # Utility scripts
└── docs/                        # Documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and code quality checks
5. Submit a pull request
