from datasets import Dataset
from ragas import evaluate
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from ragas.run_config import RunConfig
from ragas.metrics import (
    Faithfulness,
    AnswerRelevancy,
    ContextPrecision,
    ContextRecall,
)

eval_data = [
    {
        "question": "What documents are required during joining procedure?",
        "ground_truth": """
        Mark sheets, passing certificates, birth certificate,
        address proof, relieving letter, salary slip,
        medical certificate, Aadhaar/PAN/passport,
        photographs.
        """
    },
    {
        "question": "What is the salary payment policy?",
        "ground_truth": """
        Salary becomes due and payable on the last working day of each month.
        """
    },
    {
        "question": "What happens if identity card is lost multiple times?",
        "ground_truth": """
        Loss of identity card more than two occasions
        shall be viewed as misconduct.
        """
    },
    {
        "question": "What are the types of leave available?",
        "ground_truth": """
        Casual Leave, Earned Leave, Half Pay Leave,
        Commuted Leave, Extraordinary Leave,
        Maternity Leave, Paternity Leave,
        Adoption Leave.
        """
    }
]

from app.rag.rag_pipeline import ask_question
from app.rag.chat import groq_llm
from ragas.embeddings import LangchainEmbeddingsWrapper


embeddings = LangchainEmbeddingsWrapper(
    HuggingFaceBgeEmbeddings(
        model_name= "BAAI/bge-large-en-v1.5"
        )
)

dataset = []

for item in eval_data:

    question = item["question"]
    ground_truth = item["ground_truth"]

    result = ask_question(question)

    dataset.append(
        {
            "question": question,
            "answer": result["answer"],
            "contexts": [result["context"]],
            "ground_truth": ground_truth,
        }
    )

evaluation_dataset = Dataset.from_list(dataset)

result = evaluate(
    dataset=evaluation_dataset,
    metrics=[
        Faithfulness(),
        AnswerRelevancy(strictness=1),
        ContextPrecision(),
        ContextRecall(),
    ],
    llm=groq_llm,
    embeddings=embeddings,
    run_config=RunConfig(max_workers=2)
)

print(result)