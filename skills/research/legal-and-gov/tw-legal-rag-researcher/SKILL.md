---
name: tw-legal-rag-researcher
description: Use TW Legal RAG for Taiwan judgment retrieval and citation-grounded legal research, reducing hallucination. This skill instructs the agent on how to interact with the TW Legal RAG system through various interfaces.
---

# TW Legal RAG Researcher

This skill enables Manus to perform legal research in Taiwan by leveraging the TW Legal RAG system. It ensures that legal information is retrieved accurately, cited properly, and minimizes the risk of generating fabricated content (hallucinations).

## When to Use This Skill

Use this skill when the task involves:
- Retrieving Taiwan judgments or legal documents.
- Performing legal research related to Taiwan law.
- Answering legal questions that require citation-grounded evidence.
- Analyzing legal cases or precedents in Taiwan.

## When Not to Use This Skill

Do NOT use this skill for:
- Providing legal advice or opinions.
- Researching non-Taiwanese legal systems.
- Tasks that do not require specific legal judgment citations.
- Handling sensitive personal data that cannot be anonymized.

## Privacy and Anonymization Rules

- Always anonymize any personal or sensitive information from user queries before sending them to TW Legal RAG.
- Never include real names, ID numbers, addresses, or other personally identifiable information in queries or retrieved content unless explicitly instructed and legally permissible.

## Database Connection Rule

- The TW Legal RAG system is a remote service; direct database connection is not required or permitted.

## TW Legal RAG Interfaces and Priority

Always use the available interfaces in the following priority:

1.  **CLI**: `twlegalrag` (preferred for scripting and automation)
    -   GitHub / CLI: [https://github.com/aa0101181514/tw-legal-rag.git](https://github.com/aa0101181514/tw-legal-rag.git)
2.  **MCP endpoint**: `https://tlr.dr-lawbot.com/mcp` (for programmatic access within Manus)
3.  **OpenAPI schema**: `https://tlr.dr-lawbot.com/openapi.yaml` (for direct API calls if MCP is not suitable)
4.  **Public web UI**: [https://dr-lawbot.com/ask](https://dr-lawbot.com/ask) (only as a fallback for manual reference or when other interfaces are unavailable/unsuitable)
-   **TwinkleAI Hub**: [https://hub.twinkleai.tw/](https://hub.twinkleai.tw/) (for general information and resources related to TwinkleAI)

## Twinkle Hub MCP Integration

Twinkle Hub provides a general MCP endpoint for accessing various Taiwan-specific data and tools, which can complement legal research. It acts as a tool layer, providing data and functionalities, while the AI is responsible for understanding and organizing the information.

### 1. Obtain API Key

1.  Navigate to [https://hub.twinkleai.tw/](https://hub.twinkleai.tw/).
2.  Log in to your account.
3.  Go to the account/API key related page (e.g., [/dashboard](/en/dashboard)) to obtain your Twinkle Hub API Key (starts with `sk-...`).

### 2. Twinkle Hub MCP Endpoint

The official Twinkle Hub MCP endpoint is: `https://api.twinkleai.tw/mcp/`

### 3. Claude Desktop / Cursor Configuration

To configure your MCP client (e.g., Claude Desktop, Cursor), add the following to your MCP configuration file:

```json
{
  "mcpServers": {
    "twinkle-hub": {
      "type": "http",
      "url": "https://api.twinkleai.tw/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_TWINKLE_HUB_API_KEY"
      }
    }
  }
}
```

**Important**: Replace `YOUR_TWINKLE_HUB_API_KEY` with your actual API key. Ensure this key is kept confidential and never committed to public repositories.

### 4. Claude Code Connection

To connect using Claude Code, execute the following command:

```bash
claude mcp add --transport http twinkle-hub https://api.twinkleai.tw/mcp/ \
  --header "Authorization: Bearer YOUR_TWINKLE_HUB_API_KEY"
```

**Important**: Replace `YOUR_TWINKLE_HUB_API_KEY` with your actual API key.

### 5. How to Prompt AI to Use Twinkle Hub MCP

Once connected, you can instruct the AI to use the `twinkle-hub` MCP with prompts like:

-   "請使用 `twinkle-hub` MCP，列出目前可用工具。"
-   "請使用 `twinkle-hub` MCP 查詢台灣政府開放資料中和「空氣品質」相關的資料集。"

### Security Note

-   Never embed your API key directly into GitHub repositories, screenshots, or public chat logs.
-   Twinkle Hub is a MCP tool layer, not a model itself; it provides data and tools, while the AI is responsible for understanding and organizing the information.

## CLI Workflow

To use the `twlegalrag` CLI tool:

1.  **Install the CLI**: If not already installed, use `pip install twlegalrag`.
2.  **Pack a question**: To prepare a question for RAG, use:
    ```bash
    twlegalrag pack "<your legal question>" -o bundle.json
    ```
    This will create a `bundle.json` file containing the packed question.
3.  **Search for relevant judgments**: To search for judgments based on keywords and read the content, use:
    ```bash
    twlegalrag search "<keywords>" -n 5 --read
    ```
    This command will retrieve the top 5 relevant judgments and display their content.

## Answering from Retrieved Materials

-   **Cite all sources**: Every piece of information derived from TW Legal RAG MUST be cited with its `citation_id` (e.g., J1, J2, J3).
-   **Mark unsupported claims**: Any claim or statement that cannot be directly supported by the retrieved materials MUST be marked as `unverified`.
-   **Never invent information**: DO NOT invent judgments, case numbers, court holdings, or any other legal details. If information is not found, state that it is not available.

## Legal Advice Disclaimer

-   Always include a disclaimer that the provided information is for research purposes only and does not constitute legal advice. Advise the user to consult a qualified legal professional for specific legal issues.

## Final Answer Format

When presenting the final answer, adhere to the following structure:

```
Based on the retrieval from TW Legal RAG:

[Answer content, with inline citations like J1, J2, etc.]

Unsupported claims: [List any claims marked as `unverified` or state "None"]

Retrieved Judgments:
- J1: [Judgment summary/key finding]
- J2: [Judgment summary/key finding]
...

**Disclaimer**: This information is for research purposes only and does not constitute legal advice. Consult a qualified legal professional for advice on specific legal issues.
```

## Handling Unavailable Retrieval

If the TW Legal RAG system is unavailable or returns an error, the agent MUST state that retrieval was not available and provide a general, non-advisory explanation of the legal topic, followed by the legal advice disclaimer. Example:

"TW Legal RAG retrieval was not available at this time. Generally, the concept of [legal topic] involves [general explanation of the concept].

**Disclaimer**: This information is for research purposes only and does not constitute legal advice. Consult a qualified legal professional for advice on specific legal issues."
