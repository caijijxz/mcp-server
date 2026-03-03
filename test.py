import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client


async def test_connection():
    url = "https://light-white-hamster.fastmcp.app/mcp"
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyXzEyMyIsInVzZXJuYW1lIjoibWNwX2FkbWluIiwic2NvcGUiOiJtY3A6Y29ubmVjdCIsImV4cCI6MTc3MjUzMTc0NCwiaWF0IjoxNzcyNTI5OTQ0fQ.UWicsW5beY1MfQmRHjzRiUXmyv-Q4hqXW_I5j7-rrk4"}

    try:
        async with sse_client(url=url, headers=headers) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                print(f"连接成功！发现 {len(tools.tools)} 个工具:")
                for t in tools.tools:
                    print(f" - {t.name}: {t.description}")

                # 尝试调用第一个工具
                if tools.tools:
                    res = await session.call_tool(tools.tools[0].name, arguments={"input": "test"})
                    print(f"调用结果: {res}")
    except Exception as e:
        print(f"连接失败: {e}")


asyncio.run(test_connection())