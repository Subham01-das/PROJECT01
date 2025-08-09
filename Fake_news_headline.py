import random

subjects= ["Sharukh Khan",
           "Virat Kohli",
           "Nirmala Sitharaman",
           "A Mumbai Cat"
           "A Group of Monkeys",
           "Prime Minister Modi",
           "Auto Rickshaw Driver from Delhi"]
actions=["launches",
         "cancels",
         "dances with",
         "eats",
         "declares war on",
         "orders",
         "celebrates"]
Places_or_things=["at Red fort",
                  "in a Mumbai local train",
                 "in a Delhi metro",
                 "at the Taj Mahal",
                 "in a cricket stadium",
                 "at the Gateway of India",
                 "in a Bollywood movie"]
while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    place_or_thing= random.choice(Places_or_things)
    headline=f" BREAKING NEWS : {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do yoy want another headline ? (yes/no)".strip().lower())
    if user_input != "yes":
        print("\n Thank you for using the Fake News Headline Generator!")
        break
