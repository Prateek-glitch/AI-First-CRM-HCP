def suggest_nba_tool(db, payload):
    sentiment = payload.get("sentiment", "neutral")
    # Optional: use LLM here if already wired
    if sentiment == "positive":
        action = "Share advanced clinical evidence deck and propose pilot adoption."
    elif sentiment == "negative":
        action = "Schedule clarification call, address objections, and share safety FAQs."
    else:
        action = "Send follow-up summary and propose next meeting."

    return {
        "tool": "suggest_next_best_action",
        "sentiment": sentiment,
        "recommended_action": action
    }