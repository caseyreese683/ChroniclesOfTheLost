
#### main.py

```python
#!/usr/bin/env python3
import random

cities = [
    "Eldorath – A golden city that vanished overnight, leaving only ruins filled with whispers.",
    "Nyxalis – A fortress of knowledge, sealed away after its people unlocked forbidden secrets.",
    "The Shattered Spire – A floating citadel that fell from the sky, now buried beneath the waves.",
    "Vorithal – A desert city swallowed by the sands, its relics waiting to be uncovered.",
    "Xan’Thir – An underground metropolis, said to still glow with eldritch energy."
]

def get_random_city():
    return random.choice(cities)

def main():
    print("Welcome to Chronicles of the Lost!")
    print("Here is a randomly generated lost city and its legend:")
    print(get_random_city())

if __name__ == "__main__":
    main()
