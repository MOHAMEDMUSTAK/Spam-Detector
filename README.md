# Spam Detector (Rule-Based AI)
## Overview
This is a simple AI-based Python project that classifies a message as Spam or Not Spam using rule-based scoring and pattern detection. The system analyzes common spam keywords, suspicious links, and excessive punctuation to determine whether a message is spam.
## Tech Stack
- Python 3
- Regular Expressions (re module)
## How It Works
The program assigns a spam score based on:
- Presence of common spam keywords (e.g., "free", "win", "cash")
- Detection of suspicious links (http:// or https://)
- Excessive exclamation marks
If the total score exceeds a defined threshold, the message is classified as Spam.
## How to Run
1. Make sure Python is installed.
2. Clone this repository or download the project files.
3. Open terminal inside the project folder.
4. Run:
python spam_detector.py
5. Enter a message when prompted.
## Example
Input:
Congratulations! You have won free cash!!! Click here now!
Output:
Result: Spam
## Use Cases
- Email filtering systems
- Message moderation tools
- Basic cybersecurity automation
- NLP learning projects
- Beginner AI demonstrations
## Future Improvements
- Machine Learning-based spam classifier
- Dataset training support
- Web interface using Flask or Streamlit
- Improved scoring algorithm
- Probability-based output
## Author
Mohamed Mustak M
