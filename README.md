[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s7J27iqd)

EduBridge AI – Multimodal AI Assistant for Early Childhood Education

Problem Statement:




Early childhood education involves multiple types of information such as:

- homework notices
- worksheets
- voice messages from teachers
- photos of assignments
- multilingual communication

Managing this manually becomes difficult for parents and teachers.

EduBridge AI solves this by creating an AI assistant that can understand documents, images, and voice messages and answer questions about them.

System Architecture

The system works using a RAG (Retrieval-Augmented Generation) architecture.

Flow:

User Input
   |
   v
Streamlit Interface
   |
   v
File Processing Layer
(PDF / Image / Audio)
   |
   v
Text Extraction
(PyPDF / EasyOCR / Whisper)
   |
   v
Text Chunking
(LangChain Text Splitter)
   |
   v
Embeddings Generation
(Sentence Transformers)
   |
   v
Vector Database
(Pinecone)
   |
   v
Relevant Context Retrieval
   |
   v
LLM Reasoning
(Ollama – Llama model)
   |
   v
AI Response

Technologies Used

Frontend

Streamlit
Provides a simple UI where users can:

- upload files
- ask questions
- view AI responses

Language Model

Ollama (Local LLM)

Used to:

- generate answers
- interpret retrieved documents
- support role-based responses

Advantages:

- runs locally
- private
- fast for demos

RAG Pipeline

Retrieval-Augmented Generation ensures that the AI answers using uploaded documents instead of guessing.

Components:

- chunking
- embeddings
- vector search
- LLM reasoning

Embeddings Model

Sentence Transformers

Model used:

- all-MiniLM-L6-v2

Purpose:
Convert text into vector embeddings so semantic search can be performed.

Vector Database

Pinecone

Used to:

- store document embeddings
- perform similarity search
- retrieve relevant chunks for questions

Chunking

LangChain RecursiveCharacterTextSplitter

Documents are split into small chunks to improve retrieval accuracy.

Example chunk size:

- 300 characters

Multimodal Input Support

The system supports three types of inputs.

1. Document Processing

File type:

- PDF

Tool used:

- PyPDF

Purpose:
Extract text from school notices, assignments, etc.

Example:

- Homework notice
- Weekly assignment
- Teacher announcements

2. Image Processing (Computer Vision)

Tool used:

- EasyOCR

Purpose:
Extract text from images.

Examples:

- homework worksheet photos
- notice board images
- scanned assignments

Flow:

Image → OCR → Text → RAG pipeline

3. Voice Processing

Tool used:

- Whisper

Purpose:
Convert voice messages to text.

Example:

Parent records audio:

"My daughter missed class today. What homework should she do?"

Pipeline:

Audio → Whisper transcription → Text → RAG retrieval → LLM answer

Multilingual Capability

The system can process multiple languages.

Examples tested:

- English
- Tamil

Voice input in Tamil was transcribed correctly using Whisper.

Metadata Tracking

Each document chunk now stores metadata such as:

- filename
- content
- similarity score

This allows the AI to mention which file the answer came from.

Example response:

Source File: maths_homework.pdf

Improved Retrieval Accuracy

You implemented improvements such as:

1. Chunk enrichment

Each chunk now contains filename information:

Filename: homework_notice.pdf
Content: ...

2. Similarity score filtering

Only chunks with strong relevance are used.

This prevents unrelated answers.

3. Relevance gating

If the user asks something unrelated (e.g., sports question), the system now responds:

I could not find relevant information in the uploaded documents.

Instead of hallucinating answers.

Hybrid AI Mode

The system now supports two modes of answering.

Mode 1 — Document-based answer

Example:

What is today's homework?

AI retrieves relevant documents and answers.

Mode 2 — General AI fallback

Example:

Write numbers from 1 to 10

If documents are irrelevant, AI answers using general knowledge.

Current Features

Your project now supports:

File Upload

Users can upload:

- PDF documents
- images
- audio files

Multimodal Understanding

The system understands:

- Text
- Images
- Voice

AI Question Answering

Users can ask questions like:

- What is today's homework?
- Which file contains the worksheet?
- What did the parent ask in the audio?

Source-aware answers

The system can reference document sources.

Knowledge Base Management

Users can:

- Clear Knowledge Base
- Upload new files
- Ask new questions

Testing Completed

You tested:

- Document QA

- AI answers homework questions correctly.

- Image OCR

- Homework image text extracted successfully.

- Voice transcription

- Tamil and English audio converted to text.

- Metadata retrieval

- AI identifies source files.

- Unrelated query handling

- System now avoids incorrect answers.

Why This Project Is Strong

Your project demonstrates several industry AI concepts:

Concept Implementation
RAG     Document-grounded AI
Vector Search   Pinecone
Embeddings      Sentence Transformers
OCR     EasyOCR
Speech Recognition      Whisper
LLM     Ollama
Multimodal AI   Text + Image + Audio

Most hackathon projects implement only one of these.
Your system integrates all of them.

Possible Future Improvements

These can be added later:

- multilingual translation
- teacher dashboard
- AI homework explanation
- better voice query integration
- analytics for teachers

One-line Project Description

EduBridge AI is a multimodal educational assistant that uses retrieval-augmented generation to answer questions from school documents, images, and voice messages using AI.

If you want, I can also help you prepare:

- Hackathon presentation explanation (how to explain this in 2 minutes)
- Demo flow to impress judges
- Architecture diagram for slides
- Possible judge questions and answers.
