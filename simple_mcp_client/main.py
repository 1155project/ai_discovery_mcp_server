from fastmcp import Client
import asyncio

# The Client automatically uses SSETransport for URLs containing /sse/ in the path
client = Client("http://127.0.0.1:8842/sse")

async def main():
    async with client:
        resources = await client.list_resources()
        for r in resources:
            print(f"Resource: {r.name} - {r.description}")
            result = await client.read_resource(r.uri)
            print(f"Result: {result}")

asyncio.run(main())