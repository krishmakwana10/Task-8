print(" TechBot here! I'm your virtual tech assistant. Type 'exit' to quit.")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("TechBot: Goodbye! Hope your tech issues are solved.")
        break
    elif "not working" in msg:
        print("TechBot: Have you tried turning it off and on again?")
    elif "internet" in msg:
        print("TechBot: Please check your router and cables. Try restarting the modem.")
    elif "slow" in msg:
        print("TechBot: Try clearing cache and closing background apps.")
    elif "blue screen" in msg:
        print("TechBot: Uh-oh! You might need a system restore or repair.")
    else:
        print("TechBot: Can you provide more technical details?")
