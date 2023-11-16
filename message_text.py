# def get_love_message():
#     message_text = "Good morning, my love. I hope you have a wonderful day."
#     return message_text

import random


def get_love_message():
    love_messages = []

    # List of template phrases
    template_phrases = [
        "Good morning, my love. {} You are the sunshine of my life.",
        "You are the most amazing person I know. {} Thank you for being in my life.",
        "I love you more than words can say. {} Thinking of you always.",
        "Wishing you a day filled with joy and happiness. {} Have a great day!",
        "You are my soulmate, my best friend, and the love of my life. {} You make my world complete.",
        "I can't imagine my life without you. {} I am so grateful for you.",
        "You make me laugh every day. {} You are the reason for my happiness.",
        "I am so grateful for you. {} You are my everything.",
        "I love you to the moon and back. {} You are my world.",
        "You are my confidante, my rock, and my inspiration. {} I cherish every moment we spend together.",
        "You make me feel complete. {} I am so lucky to have you in my life.",
        "You are my everything and more. {} Thank you for being my sunshine.",
    ]

    # List of adverbs and adjectives to add variety to the messages
    adverbs = ["truly", "deeply", "utterly", "completely", "incompletely", "incredibly", "unbelievably"]
    adjectives = ["beautiful", "amazing", "wonderful", "intelligent", "kind", "caring", "supportive"]

    # Generate 365 unique messages with random phrases and modifiers
    for i in range(365):
        # Randomly select a template phrase
        template_phrase = random.choice(template_phrases)

        # Randomly select an adverb and adjective to modify the message
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)

        # Insert the adverb and adjective into the template phrase
        modified_phrase = template_phrase.format(f"{adverb} {adjective}")

        # Add the unique message to the list
        love_messages.append(modified_phrase)

    generated_love_message = random.choice(love_messages)

    my_list = love_messages

    # Specify the file path
    file_path = "love_messages.txt"

    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write each element of the list to a new line in the file
        for item in my_list:
            file.write(str(item) + '\n')

    print(f"List has been saved to {file_path}")

    return generated_love_message


get_love_message()
