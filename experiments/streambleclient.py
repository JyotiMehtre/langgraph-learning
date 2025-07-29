from mcp import ClientSession, StdioServerParameters
from mcp.client.streamable_http import streamablehttp_client
from langchain_mcp_adapters.tools import load_mcp_tools
import asyncio
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel

model_name = "gemini-2.0-flash-001"
model_provider = "google_vertexai"


async def get_llm(name:str, provider:str) -> BaseChatModel:
    """get the llm

    Args:
        name (str): name of the mode
        provider (str): provider

    Returns:
        BaseChatModel: llm
    """
    return init_chat_model(model=name, model_provider=provider)


async def get_mcp_tools_n_execute():
    async with streamablehttp_client("http://localhost:9000/mcp/") as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            tools = await load_mcp_tools(session)
            gemini_llm = await get_llm(model_name, model_provider)
            gemini_llm_with_mcp_tools = gemini_llm.bind_tools(tools)

            # Ask LLM
            response = await gemini_llm_with_mcp_tools.ainvoke(
                [HumanMessage(
                    content=
                    "I have 10 bikes i bought one, How many bikes do i have ?")]
            )
            print(response)


if __name__ == "__main__":
    asyncio.run(get_mcp_tools_n_execute())