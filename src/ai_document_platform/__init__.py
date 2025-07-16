"""Document Intelligence Platform - A portfolio demonstration of modern software engineering."""

__version__ = "0.1.0"


def main() -> None:
    """Main entry point for the application."""
    print(f"Document Intelligence Platform v{__version__}")
    print(
        "Use 'uvicorn ai_document_platform.api.main:app --reload' to start the development server"
    )


if __name__ == "__main__":
    main()
