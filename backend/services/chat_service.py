def generate_answer(question: str) -> dict:
    """
    Mock AI logic that generates an answer based on keywords.
    Future-ready: This can be replaced with a RAG/LLM pipeline.
    """
    q_lower = question.lower()
    
    if "deadlock" in q_lower:
        answer = (
            "A deadlock is a situation where two or more processes are unable to proceed "
            "because each is waiting for the other to release a resource. In OS theory, "
            "it is characterized by four conditions: Mutual Exclusion, Hold and Wait, "
            "No Preemption, and Circular Wait."
        )
        source = "Operating Systems Principles - Lecture Notes"
        confidence = 0.98
    elif "cpu" in q_lower:
        answer = (
            "The Central Processing Unit (CPU) is the primary component of a computer "
            "that acts as its 'brain.' It performs basic arithmetic, logic, controlling, "
            "and input/output operations specified by the instructions in a computer program."
        )
        source = "Computer Architecture Module"
        confidence = 0.95
    else:
        answer = (
            f"I see you're asking about '{question}'. Currently, I can provide detailed "
            "explanations for 'deadlock' and 'cpu'. For other topics, please check back "
            "as my knowledge base expands!"
        )
        source = "General Knowledge Base"
        confidence = 0.8
        
    return {
        "answer": answer,
        "source": source,
        "confidence": confidence
    }
