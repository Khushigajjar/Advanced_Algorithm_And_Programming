def analyze_message(message):
    uppercase_count = 0
    punctuation_count = 0
    alphabetic_count = 0
    repeated_spam = False
    prev_char = None
    repeat_count = 1

    for char in message:
        if char.isalpha():
            alphabetic_count += 1
            if char.isupper():
                uppercase_count += 1

        if char in ['!', '?']:
            punctuation_count += 1

        if char == prev_char:
            repeat_count += 1
            if repeat_count > 3:
                repeated_spam = True
        else:
            repeat_count = 1
            prev_char = char

    caps_ratio = (uppercase_count / alphabetic_count) if alphabetic_count > 0 else 0

    if caps_ratio >= 0.6 or punctuation_count >= 5:
        classification = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punctuation_count >= 3:
        classification = "URGENT"
    else:
        classification = "CALM"

    return uppercase_count, punctuation_count, caps_ratio, classification, repeated_spam

# Assuming the analyze_message function is already defined

# Test messages
test_messages = [
    "Hey, want to connect?",          # Expected: CALM
    "PLEASE ACCEPT MY REQUEST!!!",   # Expected: AGGRESSIVE
    "Are you free? I need to talk!!!" # Expected: URGENT
]

for msg in test_messages:
    uppercase_count, punctuation_count, caps_ratio, classification, repeated_spam = analyze_message(msg)
    print(f"Message: {msg}")
    print(f"Uppercase: {uppercase_count}, Punctuation: {punctuation_count}, Caps ratio: {caps_ratio:.2f}")
    print(f"Repeated spam: {repeated_spam}")
    print(f"Classification: {classification}")
    print("-"*50)