Project Overview:

"Wort des Tages" is a serverless German vocabulary app that picks a fresh word each day, gets Generative AI to write example sentences, and emails it to subscribers. No manually curated word lists - picked by a LLM to keep content dynamic and fresh.

## Core Features:

- Daily Word picking by LLM
- AI-Generated Examples: Use LLM to create example sentences
- Email Broadcasting: Send daily vocab emails to subscribers
- Automated Scheduling: Runs daily via EventBridge

## Success Criteria:

- A subscriber receives a German word email every day with useful examples
- New people can easily subscribedocs
- System runs reliably without manual intervention

Road map to build thinnest end-to-end working system
- Lambda with hardcoded German word + basic example
- EventBridge trigger (maybe hourly for testing)
- SES sending to my email only
- Then expand: Add LLM → Add real subscribers → Add better content

Progress:
- AWS setup -> done
- decision made: python + AWS SDK
- SAM configuration -> done
