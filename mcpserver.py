from fastmcp import FastMCP

mcp = FastMCP("MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, bro, {name}!"

from fastmcp.server.auth.providers.jwt import JWTVerifier, RSAKeyPair

# 生成用于测试的密钥对
key_pair = RSAKeyPair.generate()

# 使用公钥配置您的服务器
verifier = JWTVerifier(
    public_key=key_pair.public_key,
    issuer="https://test.yourcompany.com",
    audience="test-mcp-server"
)

# 使用私钥生成测试令牌
test_token = key_pair.create_token(
    subject="test-user-123",
    issuer="https://test.yourcompany.com",
    audience="test-mcp-server",
    scopes=["read", "write", "admin"]
)

print(f"Test token: {test_token}")


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)