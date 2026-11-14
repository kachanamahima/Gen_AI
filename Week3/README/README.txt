WEEK 3 - MONGODB CONNECTIVITY & LLM MONITORING

FILES
- main.py: starts the program and lets you select Gemini or Ollama
- llm_client.py: common provider interface, AI calls, retries and monitoring
- mongo_logger.py: saves call records in MongoDB
- cost_calculator.py: estimates Gemini cost and sets Ollama cost to zero
- requirements.txt: Python packages
- .env.example: environment-variable template

WINDOWS / VS CODE SETUP

1. Open this folder in VS Code.
2. Open Terminal > New Terminal.
3. Create and activate a virtual environment:

   py -m venv .venv
   .\.venv\Scripts\Activate.ps1

   If PowerShell blocks activation, use:
   .\.venv\Scripts\activate.bat

   Or run commands with:
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt

4. Install packages:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

5. Create your local environment file:
   Copy-Item .env.example .env
   Keep the placeholder key if you are using Ollama. Add your own Gemini API key only if selecting Gemini.

6. Make sure MongoDB is running (PowerShell):
   Get-Service MongoDB
   Start-Service MongoDB

   Start-Service is only needed if the service is stopped. If access is denied,
   open PowerShell as Administrator.

7. For Ollama, make sure Ollama is installed and running, then download the model:
   ollama pull llama3.2

   You can test it with:
   ollama run llama3.2

8. Run the project:
   python main.py

   Enter 2 for Ollama, then type a question.

9. Open MongoDB Compass and connect to:
   mongodb://localhost:27017/

   Open database llm_monitoring > collection call_logs.
   A document is inserted after each successful or failed model request.

NOTES
- The Gemini price values in cost_calculator.py are sample values from the
  assignment, not verified current prices. Update them for your chosen model.
- If the Gemini model name is unavailable to your API key, set GEMINI_MODEL
  in .env to a model currently available to your account.
- Ollama runs locally; this project records its token counts and sets its
  per-token API cost to 0.
