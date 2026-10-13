knowledge_base = [
    "Machine learning enables computers to learn patterns from data.",
    "RAG stands for Retrieval-Augmented Generation.",
    "Python is a popular programming language for AI and data science.",
    "Embeddings represent text as numerical vectors.",
    "A vector database stores vectors for similarity search."
]

def retrieve_information(question):
    question_words = set(question.lower().split())

    results = []

    for document in knowledge_base:
        document_words = set(
            document.lower().replace(".", "").split()
        )

        score = len(question_words & document_words)

        if score > 0:
            results.append((score, document))

    results.sort(reverse=True)

    return results

question = input("Ask a question: ")

results = retrieve_information(question)

print("\nRetrieved information:")

if results:
    for score, document in results:
        print("-", document)
else:
    print("No matching information found.")
