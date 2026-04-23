class IngestService:
    """Service to handle document ingestion logic."""

    @staticmethod
    def process_file() -> dict:
        """
        Simulates file processing. 
        In the future, this will involve OCR/PDF parsing and Vector DB insertion.
        """
        return {
            "file_id": "f-mock-123",
            "status": "processing"
        }

    @staticmethod
    def get_ingestion_status(file_id: str) -> dict:
        """
        Simulates checking the status of a processed file.
        """
        return {
            "file_id": file_id,
            "status": "completed"
        }

ingest_service = IngestService()
