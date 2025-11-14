"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Brittney Rouse
Date: 11/10/25

AI Usage: ChatGPT helped me with the following issues:
- BIGGEST MISTAKE : I orignally had undefined values within each subclass for the health, strength, and magic. The valid values were passed directly to super(), and did not
need to be overriden afterwards. The code was originally written like this:
super().__init__(self, name, health=120, strength=15, magic=5)
self.health = health
self.strength = strength
self.magic = magic
This was later changed to the correct code :
super().__init__(name, "Warrior", health=120, strength=15, magic=5)
- importing "random" for random.int() for the Rogue's critical hit
- I had previously put "self" when calling super.__init__() (for example, I had originally put super().__init__(self, name, health, strength, magic) - "self" should NOT have
been called; I did this for every class, so I had to correct it in multiple places
- I also called super() incorrectly in Player.display_stats - I had originally had super().display_stats(self, name, health, strength, magic); however, it only needed super().
display_stats(), with no self or other arguments
- "damage" was also originally undefined in every single method because of the way I had written it; I had originally written it as self.damage_taken =
target.take_damage(damage) * self.strength, which is obviously incorrect because damage was never defined. ChatGPT corrected this to the current code (damage = self.strength
target.take_damage(damage))
- When checking to see if the health ever went below 0, I originally had it so the health would be changed to 1 if self.health went to 0 OR below, which was incorrect - it
needed to be self.health = 0 if self.health < 0 (Makes sure the health never goes into the negatives, BUT it's less than one)
- I also added the character class into the argument in the Warrior, Mage, and Rogue class constructors (I had previously not added that)
- All overriding attacks duplicated damage - I called the original attack function (super().attack(target)) while ALSO doing the different attack styles; this led to the
original attack being called AND the unique attacks, doing more than damage than intended
- Also corrected the output code - print(f"{target.take_damage(damage)} damage was taken!") was changed to print(f"{self.name} dealt {damage} damage to {target.name}!")
(and later customized for each class)
- Got rid of redundant lines (I had originally put self.name = name  in every subclass? Silly, simple mistake.)
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

##ChatGPT - previously forgot to import random for random.int() in Rogue class
import random

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        ##Sets up a character's name, health, strength, and magic values
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage

        ##ChatGPT helped with the next two lines - I had incorrectly written it before as "self.damage_taken = target.take_damage(damage) * self.strength", which was
        ##incorrect since damage was never defined.
        ##This code calculates a basic attack that any character can use (not exclusive to any class)
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} deals {damage} damage to {target.name}!")

        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0

        ##ChatGPT corrected this code slightly (previously, I had it as "if self.health <= 0, self.health = 1" which was a silly mistake (I misread the instructions as
        ##self.health couldn't equal 0 or less(instead of it not going BELOW 0))
        ##There was also an unnecessary "else" branch, but what was in the else branch was already written above the if-branch.
        ##This code takes away the health dealt in an attack; if health goes below 0, it is automatically corrected to exactly 0
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
            
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        ##Prints the character's current stats with identical formatting
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")
        

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)
        ##Initializes the player's character
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level
        ##Displays the original stats with the addition of the player's class, level, and experience
        super().display_stats()
        print(f"Character Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")
        

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # TODO: Call super().__init__() with warrior-appropriate stats
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        # Suggested stats: health=120, strength=15, magic=5
    
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        ##Damage has ten additional points taken away, and a line specifically for the warrior is printed out
        damage = self.strength + 10
        target.take_damage(damage)
        print(f"With a solid strike, {self.name} deals {damage} damage to {target.name}!")

        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        ##Damage is multiplied by three (very strong attack) and a special line is printed out
        damage = self.strength * 3
        target.take_damage(damage)
        print(f"{self.name} deals {damage} damage to {target.name} with a power strike!")


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        super().__init__(name, "Mage", health=80, strength=8, magic=20)

        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        ##Damage is calculated with self.magic instead of self.strength; a line unique to the mage is written
        damage = self.magic + 5
        target.take_damage(damage)
        print(f"With a magical attack, {self.name} deals {damage} damage to {target.name}!")

        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        ##Damage is multiplied by two (special attack) and a unique line is printed out
        damage = self.magic * 2
        target.take_damage(damage)
        print(f"{self.name} deals {damage} damage to {target.name} with a fireball!")


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)
        
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        ##Checks for critical attack ("result" must be three or less out of a range of 1-10); if it is a crtical, the damage is multiplied by two, and "Critical hint!" is
        #printed out. Else, the amount of damage stays the same.
        result = random.randint(1,10)
        if result <= 3:
            damage = self.strength * 2
            target.take_damage(damage)
            print(f"{self.name} deals {damage} damage to {target.name}! Critical hit!")
        else:
            damage = self.strength
            target.take_damage(damage)
            print(f"{self.name} deals {damage} damage to {target.name}!")

        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage
        ##Damage is always multiplied by two (critical attack) and a special line is printed out
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"Sneak attack! {self.name} deals {damage} damage to {target.name}!")


class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus
    
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        ##Shows the weapon name followed by the bonus damage it adds
        print(f"{self.name}: {self.damage_bonus} damage bonus")


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
