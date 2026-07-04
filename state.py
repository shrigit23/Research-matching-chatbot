# ----------------------------
# SHARED CHATBOT STATE
# ----------------------------

# Stores the latest faculty search results
last_results = []

# Keeps track of the current result for "Show me another"
current_index = 0

# Current user mode
# Possible values: "student" or "professor"
mode = "student"