import state
from rag import agent_router

print("=" * 50)
print("🎓 RESEARCH MATCHING CHATBOT")
print("=" * 50)

# ----------------------------
# MODE SELECTION
# ----------------------------
print("\nSelect User Mode")
print("1. Student")
print("2. Professor")

choice = input("Enter choice: ")

if choice == "2":
    state.mode = "professor"
else:
    state.mode = "student"

print(f"\n✅ {state.mode.title()} Mode Activated\n")


def show_commands():
    if state.mode == "student":
        print("""
Available Commands

• Who works on NLP?
• Tell me about Dr. Ravi Kumar
• Show me another
• Suggest a project
""")
    else:
        print("""
Available Commands

• What's trending in NLP?
• Who in our department works on NLP?
• Find collaboration in NLP
• What research areas are missing in our department?
""")


show_commands()

# ----------------------------
# CHAT LOOP
# ----------------------------
while True:

    query = input("\nAsk your query (type 'exit', 'switch mode'): ")

    if query.lower() == "exit":
        print("\n👋 Thank you for using the Research Matching Chatbot!")
        break

    elif query.lower() == "switch mode":

        print("\nSelect User Mode")
        print("1. Student")
        print("2. Professor")

        choice = input("Enter choice: ")

        if choice == "2":
            state.mode = "professor"
        else:
            state.mode = "student"

        print(f"\n✅ Switched to {state.mode.title()} Mode\n")
        show_commands()
        continue

    response = agent_router(query)
    print(response)