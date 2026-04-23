from collections import Counter

class DashboardService:
    """Service to handle dashboard analytics logic."""

    def __init__(self):
        # Mock stored chat data
        self.questions = [
            "What is deadlock?",
            "Explain CPU scheduling",
            "What is paging?",
            "Explain deadlock conditions",
            "What is memory management?",
            "CPU scheduling algorithms",
        ]

    def get_dashboard_data(self) -> dict:
        """
        Calculates and returns student performance statistics.
        Simulates analytics using in-memory data.
        """
        # 1. Total questions
        total_questions = len(self.questions)

        # 2. Extract keywords and count frequency
        # Keywords to track: deadlock, cpu, memory, paging
        keywords = ["deadlock", "cpu", "memory", "paging"]
        counts = Counter()

        for q in self.questions:
            q_lower = q.lower()
            for kw in keywords:
                if kw in q_lower:
                    counts[kw] += 1

        # 3. Top topics (Top 2-3 topics)
        # sorted_counts = [('deadlock', 2), ('cpu', 2), ('memory', 1), ('paging', 1)]
        sorted_topics = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        top_topics = [topic.capitalize() for topic, count in sorted_topics[:3] if count > 0]

        # 4. Weak areas (topics that appear less frequently)
        # Topics with count 1 or lower in this mock
        weak_areas = [topic.capitalize() for topic, count in sorted_topics if count <= 1 and count > 0]
        
        # If no weak areas found from keywords, provide a default
        if not weak_areas:
            weak_areas = ["Memory Management"]

        # 5. Recent questions (last 3 questions)
        recent_questions = self.questions[-3:]

        return {
            "total_questions": total_questions,
            "top_topics": top_topics,
            "weak_areas": weak_areas,
            "recent_questions": recent_questions
        }

dashboard_service = DashboardService()
