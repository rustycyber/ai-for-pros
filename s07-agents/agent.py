import json
import os
from tools import TOOL_REGISTRY, OPENAI_TOOLS_SCHEMA
from providers import OpenRouterProvider, OpenAIProvider

SYSTEM_PROMPT = "You are a helpful AI Agent with access to tools. Use tools when necessary."

def pause_for_user():
    """Wait for user to press Enter to continue"""
    input("\n⏸️  Press ENTER to continue...\n")

def print_message(msg, index):
    """Helper to print a message object (dict or ChatCompletionMessage)"""
    print(f"\n  Message {index}:")
    
    # Handle both dict and object formats
    if isinstance(msg, dict):
        print(f"    Role: {msg.get('role', 'unknown')}")
        if 'content' in msg:
            if isinstance(msg['content'], str):
                print(f"    Content: {msg['content']}")
            elif isinstance(msg['content'], list):
                print(f"    Content: {msg['content']}")
        if 'tool_call_id' in msg:
            print(f"    Tool Call ID: {msg['tool_call_id']}")
    else:
        # Handle ChatCompletionMessage object
        print(f"    Role: {msg.role}")
        if msg.content:
            print(f"    Content: {msg.content}")
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            print(f"    Tool Calls:")
            for tc in msg.tool_calls:
                print(f"      - ID: {tc.id}")
                print(f"        Name: {tc.function.name}")
                print(f"        Arguments: {tc.function.arguments}")

def run_agent_workshop(provider, prompt: str):
    print("="*60)
    print(" [STEP 1] INITIAL CONTEXT PACKAGE CREATION")
    print("="*60)
    print(f"System Prompt: '{SYSTEM_PROMPT}'")
    print(f"User Query:    '{prompt}'")
    pause_for_user()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]

    step_count = 1
    while True:
        print(f"\n{'='*60}")
        print(f" [TURN {step_count}] SENDING TO MODEL")
        print("="*60)
        print("\n📤 REQUEST PAYLOAD:")
        print("-" * 60)
        for i, msg in enumerate(messages):
            print_message(msg, i+1)
        print("\n  Tools Schema:")
        print(f"    {json.dumps(OPENAI_TOOLS_SCHEMA, indent=4)}")
        print("-" * 60)
        pause_for_user()

        msg_obj, tool_call = provider.generate(messages, OPENAI_TOOLS_SCHEMA)

        print(f"\n{'='*60}")
        print(f" [TURN {step_count}] MODEL RESPONSE")
        print("="*60)
        print("\n📥 RECEIVED FROM MODEL:")
        print("-" * 60)
        print(f"  Message Object Type: {type(msg_obj).__name__}")
        print_message(msg_obj, len(messages) + 1)
        print("-" * 60)

        messages.append(msg_obj)

        if tool_call:
            print(f"\n{'='*60}")
            print(" [STEP 2] LLM DECISION: TOOL CALL REQUESTED")
            print("="*60)
            print(f"Selected Tool: {tool_call['name']}")
            print(f"Arguments:     {json.dumps(tool_call['args'])}")
            print(f"Tool Call ID:  {tool_call['id']}")
            pause_for_user()

            # Step 3: Local Host Execution
            print(f"\n{'='*60}")
            print(" [STEP 3] LOCAL HOST MACHINE EXECUTION")
            print("="*60)
            func = TOOL_REGISTRY[tool_call['name']]
            execution_result = func(**tool_call['args'])
            print(f"Execution Output: {execution_result}")
            pause_for_user()

            # Step 4: Observation Feedback
            print(f"\n{'='*60}")
            print(" [STEP 4] FEEDING OBSERVATION BACK TO LLM")
            print("="*60)
            print("\n📤 ADDING TOOL RESULT TO MESSAGES:")
            print("-" * 60)
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call['id'],
                "content": execution_result
            }
            print(f"  Role: {tool_message['role']}")
            print(f"  Tool Call ID: {tool_message['tool_call_id']}")
            print(f"  Content: {tool_message['content']}")
            print("-" * 60)
            messages.append(tool_message)
            pause_for_user()
            step_count += 1
        else:
            print(f"\n{'='*60}")
            print(" [FINAL STEP] AGENT RESPONSE GENERATED")
            print("="*60)
            print(f"Final Response: {msg_obj.content}")
            pause_for_user()
            break

if __name__ == "__main__":
    # Choose provider (OpenRouter or OpenAI)

    # Option A: OpenRouter
    provider = OpenRouterProvider(api_key=os.getenv("OPENROUTER_API_KEY"), model="openai/gpt-4o-mini")

    # Option B: OpenAI Direct
    # provider = OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")

    run_agent_workshop(
        provider=provider,
        prompt="Hi, can you calculate 142 plus 859 for me?"
    )
