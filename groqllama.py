import time
from groq import Groq

# Initialize Groq client with API key
client = Groq(api_key="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")

# Initialize variables
user_code = []
stop_flag = False  # Flag to stop monitoring

def send_to_ai_model(code_line):
    """
    Sends the given line of code to an AI model for analysis and correction.
    Returns the corrected code.
    """
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Correct this Python code:\n{code_line}"}],
            temperature=1,
            max_completion_tokens=100,
            top_p=1,
            stream=False,
            stop=None,
        )
        # Correcting the way we access the message content
        corrected_code = completion.choices[0].message.content.strip()
        return corrected_code
    except Exception as e:
        return f"Error in AI processing: {e}"

def highlight_error(line, corrected_line):
    """
    Highlights the corrected word with a red underline.
    """
    if line != corrected_line:
        # Apply red underline (ANSI escape code)
        print(f"\033[4;31m{corrected_line}\033[0m")  # Red underlined
        time.sleep(3)  # Show for 3 seconds (you can adjust the time)
        print("\033[0m")  # Reset formatting after the time has passed
    else:
        print(corrected_line)

def monitor_typing():
    """
    Monitors real-time user input and sends it to the AI model for correction.
    """
    global stop_flag
    print("\nReal-time Python Code Error Detector (Type 'exit' to stop):\n")
    
    while not stop_flag:
        line = input(">>> ")  # Capture user input
        if line.lower() == "exit":
            stop_flag = True
            break

        corrected_line = send_to_ai_model(line)  # Get AI corrections

        # Highlight errors and corrected line
        highlight_error(line, corrected_line)

        user_code.append(corrected_line)

    print("\nFinal Corrected Code:\n" + "\n".join(user_code))

# Run monitoring in a separate thread
monitor_typing()
