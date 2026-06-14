from modules.rag import answer_question

result = answer_question("What is the punishment under POCSO?")

print(result["answer"])

print("\nSources:")
print(result["sources"])