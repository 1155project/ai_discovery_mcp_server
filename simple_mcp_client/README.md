<h1 align="center">Simple MCP Client</h1>

## Overview

This is a simple MCP (Module Context Protocol) client that demonstrates how to programmatically connect to and consume an MCP Server. It serves as a practical example within the AI Discovery MCP Server project, showing how AI clients can retrieve the AI Discovery Specification document and supporting information through the MCP protocol.

## Purpose

The simple MCP client is designed to:
- Demonstrate the basic concepts of MCP client-server communication
- Show how to programmatically access AI Discovery Specification resources
- Provide a reference implementation for developers learning MCP integration
- Serve as a testing tool for the AI Discovery MCP Server

## Features

- **Resource Discovery**: Lists all available resources from the MCP server
- **Resource Retrieval**: Reads and displays the content of each available resource
- **Async Communication**: Uses asynchronous operations for efficient MCP communication
- **SSE Transport**: Connects to the MCP server using Server-Sent Events (SSE) transport

## How It Works

The client connects to the AI Discovery MCP Server running on `http://127.0.0.1:8842/sse` and:
1. Lists all available resources (typically the AI Discovery specification document and schema)
2. Retrieves and displays the content of each resource
3. Demonstrates the basic MCP client-server interaction pattern

## Prerequisites

- Python 3.12+
- The AI Discovery MCP Server must be running (see the [MCP Server README](../mcp_server/README.md) for setup instructions)

## Installation

1. Navigate to the simple_mcp_client directory:
   ```bash
   cd simple_mcp_client
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the AI Discovery MCP Server is running (see the [MCP Server README](../mcp_server/README.md))

2. Run the client:
   ```bash
   python main.py
   ```

3. The client will connect to the server, list available resources, and display their content.

## Expected Output

When running successfully, you should see output similar to:
```
Resource: ai_discovery_specification - AI Discovery Specification document
Result: [specification content]
Resource: ai_discovery_schema - JSON schema for AI Discovery specification
Result: [schema content]
```

## Integration with AI Discovery Protocol

This client demonstrates how AI systems can programmatically access the AI Discovery Specification through the MCP protocol. It shows the practical implementation of the AI Discovery Protocol's goal of making AI specification information easily discoverable and accessible to AI clients.

## Related Components

- **[MCP Server](../mcp_server/)**: The server that provides AI Discovery resources
- **[AI Discovery Specification](https://github.com/1155project/ai_discovery_specification)**: The specification this project demonstrates
- **[Module Context Protocol](https://modelcontextprotocol.io/)**: The underlying protocol for AI tool integration

