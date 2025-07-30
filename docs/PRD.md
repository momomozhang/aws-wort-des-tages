Project Overview:

"Wort des Tages" is a serverless German vocabulary app that picks a fresh word each day, gets Generative AI to write example sentences for different skill levels (A1-C1), and emails it to subscribers. No manually curated word lists - everything pulls from real German dictionary APIs to keep content dynamic and fresh.

## Core Features:

- Daily Word Fetching: Grab a German word from external dictionary API each day
- AI-Generated Examples: Use LLM to create 2 example sentences per CEFR level (A1, A2, B1, B2, C1)
- Email Broadcasting: Send nicely formatted daily vocab emails to subscribers
- Subscriber Management: Basic email subscription/unsubscription
- Automated Scheduling: Runs daily via EventBridge

## Success Criteria:

- A subscriber receives a German word email every day with useful examples
- New people can easily subscribe via API
- System runs reliably without manual intervention