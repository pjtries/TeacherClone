class DashboardService:
    """Service to handle dashboard analytics logic."""

    @staticmethod
    def get_stats() -> dict:
        """
        Calculates and returns student performance statistics.
        In the future, this will aggregate data from the Database/Logs.
        """
        return {
            "total_questions": 125,
            "top_topics": ["Deadlock", "CPU Scheduling", "Virtual Memory"],
            "weak_areas": ["Paging", "Disk Management"]
        }

dashboard_service = DashboardService()
