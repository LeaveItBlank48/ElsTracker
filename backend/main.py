
# ElsTracker Python

# Character Information
character_name = "Elsword"
character_level = 75
character_class = "Knight Emperor"
combat_power = 1500000.5

# Display Character Information
print("Welcome to ElsTracker Python!")
print("Character:", character_name)
print("Level:", character_level)

# Character Leveling
character_level = character_level + 15

print("New Level:", character_level)

# Check Character Level
if character_level > 99:
    print("Invalid character level!")
elif character_level == 99:
    print("Character is max level!")
else:
    print("Character is not max level yet.")


# =====================================
# Character Database
# =====================================

characters = [
    {
        "name": "Elsword",
        "weapon": "Great Sword",
        "job_paths": [
            {
                "name": "Knight Emperor",
                "advancements": [
                    "Sword Knight",
                    "Lord Knight",
                    "Knight Emperor"
                ]
            },
            {
                "name": "Rune Master",
                "advancements": [
                    "Magic Knight",
                    "Rune Slayer",
                    "Rune Master"
                ]
            },
            {
                "name": "Immortal",
                "advancements": []
            },
            {
                "name": "Genesis",
                "advancements": []
            }
        ]
    },
    {
        "name": "Aisha",
        "weapon": "Staff",
        "job_paths": []
    },
    {
        "name": "Rena",
        "weapon": "Bow",
        "job_paths": []
    }
]


# =====================================
# Display Character Database
# =====================================

# First loop: Go through every character
for character in characters:
    print("Character:", character["name"])
    print("Weapon:", character["weapon"])

    # Second loop: Go through the character's job paths
    for job in character["job_paths"]:
        print("Job Path:", job["name"])

        # Third loop: Go through each job's advancements
        for advancement in job["advancements"]:
            print("        -", advancement)

    print()  # Blank line between characters

def display_character(name, weapon):
    print("Character:", name)
    print("Weapon:", weapon)


display_character("Aisha", "Staff")