---
name: twinkle-hub-mcp-researcher
description: "Connect to Twinkle Hub MCP for Taiwan-specific data retrieval, public dataset lookup, and tool calling. Use for: Taiwan government records, company data, statistics, and citation-grounded research."
---

# Twinkle Hub MCP Researcher

This skill enables agents to leverage Twinkle Hub for accurate Taiwan-related data retrieval and research via Model Context Protocol (MCP).

## Twinkle Hub Resources
- **Website**: [https://hub.twinkleai.tw/](https://hub.twinkleai.tw/)
- **Docs**: [https://hub.twinkleai.tw/docs](https://hub.twinkleai.tw/docs)
- **MCP Endpoint**: [https://api.twinkleai.tw/mcp/](https://api.twinkleai.tw/mcp/)
- **Tools Marketplace**: [https://hub.twinkleai.tw/tools](https://hub.twinkleai.tw/tools)
- **GitHub**: [https://github.com/ai-twinkle/Hub](https://github.com/ai-twinkle/Hub)

## When to Use
- Researching Taiwan-specific topics (government, law, economy, demographics).
- Accessing real-time or verified Taiwan public datasets.
- Performing citation-grounded research where factual accuracy is critical.
- Discovering and using specialized Taiwan data tools.

## When Not to Use
- General global knowledge already present in the model.
- Non-Taiwan related research.
- Reasoning tasks that do not require external data retrieval.

## MCP Connection Rules
Agents MUST use Twinkle Hub through MCP when available.

### Connection Configurations

**Claude Desktop / Cursor:**
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

**Claude Code CLI:**
```bash
claude mcp add --transport http twinkle-hub https://api.twinkleai.tw/mcp/ \
  --header "Authorization: Bearer YOUR_TWINKLE_HUB_API_KEY"
```

## Privacy & Security
- **API Key Protection**: NEVER expose the API key in logs, commits, screenshots, or final answers.
- **Data Privacy**: DO NOT send private personal data, secrets, or confidential company data unless explicitly confirmed by the user.
- **Anonymization**: Prefer anonymized queries for data retrieval.

## Operational Workflow

### 1. Verify Availability
Before proceeding, verify if the `twinkle-hub` MCP server is connected and its tools are available.

### 2. Discover Tools
If specific tools are unknown, ask the system to list or discover available Twinkle Hub tools to identify the best fit for the query.

### 3. Call Taiwan Data Tools
Execute tool calls to retrieve data. Treat Twinkle Hub as a **retrieval/tool layer**, not a reasoning model.

### 4. Data Integrity & Citations
- **Separation**: Clearly separate retrieved data from model-based assumptions.
- **Citations**: REQUIRE citations or tool-result references for all factual claims.
- **Unverified Claims**: Mark any claim that cannot be backed by tool output as "unverified".
- **Anti-Hallucination**: NEVER invent dataset results, government records, company data, or statistics.

### 5. Error Handling
If Twinkle Hub is unavailable:
- State clearly that "retrieval was unavailable".
- Provide only a general explanation based on internal knowledge.
- Do not attempt to simulate tool outputs.

## Final Response Format
Final outputs must be structured, professional, and include a "Sources" or "References" section mapping claims to Twinkle Hub tool outputs.
