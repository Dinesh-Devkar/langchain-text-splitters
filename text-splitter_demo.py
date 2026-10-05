from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

text="""
What is Machine Learning?
Machine Learning (ML) is a branch of Artificial Intelligence (AI) where computers learn patterns from data and use those patterns to make predictions or decisions, instead of being explicitly programmed with every rule.

Simple example
Suppose you want a computer to identify whether an email is spam or not spam.

Instead of writing hundreds of rules like:

"If the email contains 'free money', mark it as spam."

You give the computer many examples:

Email	Label
"Win $1,000 now!"	Spam
"Meeting at 3 PM"	Not Spam
"Congratulations, you won!"	Spam
"Here's the project report"	Not Spam

The ML algorithm analyzes these examples, learns patterns, and then can predict whether a new, unseen email is spam.

The basic idea
Data
  ↓
Machine Learning Algorithm
  ↓
Learn Patterns
  ↓
Trained Model
  ↓
New Data
  ↓
Prediction

Main types of Machine Learning
Supervised Learning
The model learns from data that already has answers/labels.

Spam detection

House-price prediction

Image classification

Unsupervised Learning
The model receives data without predefined answers and tries to discover patterns.

Customer segmentation

Clustering

Anomaly detection

Reinforcement Learning
The model learns by interacting with an environment and receiving rewards or penalties.

Game-playing AI

Robotics

Autonomous decision-making

Machine Learning vs AI
Think of it like this:

Artificial Intelligence (AI) → The broader field of making machines behave intelligently.

Machine Learning (ML) → A way of achieving AI by allowing machines to learn from data.

Deep Learning (DL) → A subset of ML that uses neural networks with many layers.

"""
# splitter=CharacterTextSplitter(chunk_size=50,chunk_overlap=40,strip_whitespace=True)

# docs=splitter.split_text(text)

# print(docs)

# print(len(docs))


#====================================================================================================

loader=PyPDFLoader("datasets/The_AI_Marketing_Canvas.pdf")

docs=loader.load()

splitter=CharacterTextSplitter(chunk_size=500,chunk_overlap=50,strip_whitespace=True)

documents=splitter.split_documents(docs)

print(len(documents))

print("="*30)

print(documents[2])


