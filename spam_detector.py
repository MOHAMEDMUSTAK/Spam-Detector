import re
# List of common spam keywords
SPAM_KEYWORDS = [
    "win", "winner", "free", "cash", "prize",
    "click here", "urgent", "lottery", "money",
    "offer", "credit card", "claim now"
]
def detect_spam(message):
    """
    Detects whether a message is Spam or Not Spam
    using keyword matching and pattern detection.
    """
    message = message.lower()
    score = 0
    # Keyword scoring
    for word in SPAM_KEYWORDS:
        if word in message:
            score += 1
    # Detect suspicious links
    if re.search(r"http[s]?://", message):
        score += 2
    # Detect excessive exclamation marks
    if message.count("!") > 2:
        score += 1
    # Final decision
    if score >= 2:
        return "Spam"
    else:
        return "Not Spam "
if __name__ == "__main__":
    user_input = input("Enter a message: ")
    result = detect_spam(user_input)
    print("Result:", result)
