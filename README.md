# AI To-Do App on Azure

## Features
- Simple Flask-based AI To-Do app
- Automatic labeling using random AI logic
- Deployed to Azure App Service
- Continuous Deployment via GitHub Actions

## Getting Started
1. Clone this repo
2. Run locally:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```
3. Access at `http://127.0.0.1:5000`

## Deploy to Azure
1. Create Azure App Service
2. Get publish profile and add it as GitHub Secret
3. Push to main branch to auto-deploy

## Folder Structure
```
ai_todo_app/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── .gitignore
├── .github/workflows/deploy.yml
└── README.md
```
