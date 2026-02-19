# 🛠️ Setup & Run Guide: Project 7
How to import and run your Self-Healing Workflow in n8n.

## 1. Prerequisites
- An **n8n** account (Sign up at [n8n.io](https://n8n.io) or run locally via Docker).
- An OpenAI API Key.

## 2. Importing the Workflow
1. Open your n8n canvas.
2. Click on the **Workflow Menu** (top right) > **Import from File**.
3. Select the `workflow_template.json` from this folder.

## 3. Configuration
1. **AI Agent Node:** Click the node and add your OpenAI Credentials.
2. **Slack Node:** (Optional) Connect your Slack Workspace or replace this node with an "Email" node.
3. **Webhook Node:** Click the node to get your "Production URL".

## 4. Testing the Build
Use a tool like **Postman** or **cURL** to send a fake alert to your Webhook:
```bash
curl -X POST [https://your-n8n-url.com/it-alert](https://your-n8n-url.com/it-alert) \
     -H "Content-Type: application/json" \
     -d '{"message": "Nginx service is down on Web-Server-01"}'
