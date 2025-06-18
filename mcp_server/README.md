<h1 align="center">AI Discovery MCP Server</h1>

<p align="center">
  <img src="../public/ai_discovery_logo_w.png" alt="AI Discovery Logo" width="600">
</p>

## Overview

The AI Discovery MCP Server is a reference implementation that demonstrates how to make AI Discovery Specification information programmatically accessible to AI systems through the Module Context Protocol (MCP). This server serves as a bridge between AI clients and the AI Discovery Protocol, enabling AI systems to dynamically retrieve and understand AI specification documents and schemas.

## Purpose and Problem Statement

### The Challenge
AI systems often need access to up-to-date specification information to understand how to interact with other AI systems, APIs, or services. Traditionally, this information has been:
- Scattered across different documentation formats
- Difficult to discover programmatically
- Not standardized for AI consumption
- Often outdated or inconsistent

### The Solution
The AI Discovery MCP Server addresses these challenges by:
- **Standardizing Access**: Providing a consistent MCP interface for AI Discovery resources
- **Real-time Retrieval**: Fetching the latest specification documents directly from the AI Discovery Specification repository
- **AI-Optimized Format**: Delivering content in formats that AI systems can easily parse and understand
- **Protocol Compliance**: Implementing the AI Discovery Protocol to enable standardized AI-to-AI communication

## What is the AI Discovery Protocol?

The [AI Discovery Protocol](https://github.com/1155project/ai_discovery_specification) is a specification that defines how AI systems can discover and understand each other's capabilities, requirements, and interfaces. It provides:

- **Standardized Metadata**: Consistent format for describing AI system capabilities
- **Discovery Mechanisms**: Methods for AI systems to find and retrieve specification information
- **Schema Validation**: JSON schemas for validating AI discovery documents
- **Interoperability**: Common language for AI systems to communicate their capabilities

## Features

The server provides two essential resources that enable AI systems to access AI Discovery information:

### 1. **AI Discovery Document** (`data://ai_discovery_document`)
- **Purpose**: Retrieves the complete AI Discovery Specification document
- **Format**: Markdown document containing the full specification
- **Content**: Comprehensive documentation of the AI Discovery Protocol
- **Use Case**: AI systems can read and understand the protocol requirements

### 2. **AI Discovery Schema** (`data://ai_discovery_schema`)
- **Purpose**: Retrieves the JSON schema for AI Discovery documents
- **Format**: JSON schema for validating `./well-known/ai_discovery` documents
- **Content**: Schema definition for AI discovery metadata validation
- **Use Case**: AI systems can validate discovery documents and understand the expected structure

## How It Works

### Architecture
```
AI Client ←→ MCP Protocol ←→ AI Discovery MCP Server ←→ GitHub Repository
```

### Data Flow
1. **Client Request**: AI client requests AI Discovery resources via MCP
2. **Server Processing**: MCP server receives the request and identifies the resource
3. **GitHub Fetch**: Server fetches the latest content from the AI Discovery Specification repository
4. **Response**: Server returns the requested document or schema to the client
5. **Client Processing**: AI client can now understand and work with the AI Discovery information

### Real-time Updates
The server fetches content directly from the GitHub repository, ensuring that AI systems always have access to the most current version of the AI Discovery Specification.

## Use Cases

### For AI Developers
- **Integration Testing**: Verify that AI systems can properly discover and understand each other
- **Protocol Learning**: Understand the AI Discovery Protocol requirements
- **Schema Validation**: Validate AI discovery documents against the official schema

### For AI Systems
- **Self-Discovery**: AI systems can retrieve information about their own capabilities
- **Peer Discovery**: AI systems can discover and understand other AI systems
- **Protocol Compliance**: Ensure AI systems follow the AI Discovery Protocol standards

### For Organizations
- **AI Ecosystem**: Enable multiple AI systems to work together seamlessly
- **Standardization**: Implement consistent AI discovery mechanisms across systems
- **Interoperability**: Ensure AI systems can communicate effectively

## Benefits

### For the AI Community
- **Standardization**: Common approach to AI system discovery and communication
- **Interoperability**: AI systems can work together regardless of their implementation
- **Innovation**: Enables new AI-to-AI interaction patterns

### For Developers
- **Reference Implementation**: Clear example of how to implement AI Discovery
- **Testing Tool**: Validate AI Discovery implementations
- **Learning Resource**: Understand MCP and AI Discovery concepts

### For Organizations
- **Future-Proofing**: Prepare for AI Discovery Protocol adoption
- **Competitive Advantage**: Early adoption of AI interoperability standards
- **Ecosystem Participation**: Contribute to the growing AI Discovery ecosystem

## Prerequisites

- Python 3.12+
- Docker if running the MCP server as a container (recommended)

## Installation

### Using uv

1. Install uv if you don't have it:
   ```bash
   pip install uv
   ```

2. Install dependencies:
   ```bash
   uv pip install -e .
   ```

3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Configure your environment variables in the `.env` file (see Configuration section)

### Using Docker (Recommended)

1. Build the Docker image:
   ```bash
   docker build -t ai-discovery-mcp-server --build-arg PORT=8842 .
   ```

2. Create a `.env` file based on `.env.example` and configure your environment variables

## Configuration

The following environment variables can be configured in your `.env` file:

| Variable | Description | Example |
|----------|-------------|----------|
| `TRANSPORT` | Transport protocol (sse or stdio) | `sse` |
| `HOST` | Host to bind to when using SSE transport | `0.0.0.0` |
| `PORT` | Port to listen on when using SSE transport | `8842` |

## Running the Server

### Using uv

#### SSE Transport

```bash
# Set TRANSPORT=sse in .env then:
uv run src/main.py
```

The MCP server will essentially be run as an API endpoint that you can then connect to with config shown below.

#### Stdio Transport

With stdio, the MCP client iself can spin up the MCP server, so nothing to run at this point.

### Using Docker

#### SSE Transport

```bash
docker run --env-file .env -p:8842:8842 ai-discovery-mcp-server
```

The MCP server will essentially be run as an API endpoint within the container that you can then connect to with config shown below.

#### Stdio Transport

With stdio, the MCP client iself can spin up the MCP server container, so nothing to run at this point.

## Integration with MCP Clients

### SSE Configuration

Once you have the server running with SSE transport, you can connect to it using this configuration:

```json
{
  "mcpServers": {
    "ai-discovery-mcp-server": {
      "transport": "sse",
      "url": "http://localhost:8842/sse"
    }
  }
}
```

> **Note for Windsurf users**: Use `serverUrl` instead of `url` in your configuration:
> ```json
> {
>   "mcpServers": {
>     "ai-discovery-mcp-server": {
>       "transport": "sse",
>       "serverUrl": "http://localhost:8842/sse"
>     }
>   }
> }
> ```

> **Note for n8n users**: Use host.docker.internal instead of localhost since n8n has to reach outside of it's own container to the host machine:
> 
> So the full URL in the MCP node would be: http://host.docker.internal:8842/sse

Make sure to update the port if you are using a value other than the default 8842.

### Python with Stdio Configuration

Add this server to your MCP configuration for Claude Desktop, Windsurf, or any other MCP client:

```json
{
  "mcpServers": {
    "ai-discovery-mcp-server": {
      "command": "your/path/to/ai_discovery_mcp_server/.venv/Scripts/python.exe",
      "args": ["your/path/to/ai_discovery_mcp_server/src/main.py"],
      "env": {
        "TRANSPORT": "stdio"
      }
    }
  }
}
```

### Docker with Stdio Configuration

```json
{
  "mcpServers": {
    "ai-discovery-mcp-server": {
      "command": "docker",
      "args": ["run", "--rm", "-i", 
               "-e", "TRANSPORT", 
               "ai-discovery-mcp-server"],
      "env": {
        "TRANSPORT": "stdio"
      }
    }
  }
}
```

## Testing the Server

You can test the server using the included [Simple MCP Client](../simple_mcp_client/):

1. Start the MCP server (see Running the Server section above)
2. Run the simple client:
   ```bash
   cd ../simple_mcp_client
   python main.py
   ```
3. Verify that you receive the AI Discovery document and schema

## Contributing

This project serves as a reference implementation for the AI Discovery Protocol. Contributions are welcome to:

- Improve the MCP server implementation
- Add new AI Discovery resources
- Enhance error handling and reliability
- Add tests and documentation

## Related Projects

- **[AI Discovery Specification](https://github.com/1155project/ai_discovery_specification)**: The specification this server implements
- **[Simple MCP Client](../simple_mcp_client/)**: Example client for testing the server
- **[Module Context Protocol](https://modelcontextprotocol.io/)**: The underlying protocol for AI tool integration

## Future Enhancements

Potential future improvements include:
- Caching mechanisms for improved performance
- Additional AI Discovery resources (examples, tutorials, etc.)
- Webhook support for real-time updates
- Authentication and access control
- Metrics and monitoring capabilities