import random
import json
import os
import sys

SAVE_FILE = "save_date.json"

class Character:
    def __init__(self, name, job_class, level=1, exp=1, gold=0, stats=None):
        self.name = name
        self.job_class = job_class
        self.level = level
        self.exp = exp
        self.gold = gold

        if stats:
            self.vit = stats['vit']
            self.str = stats['str']
            self.agi = stats['agi']
            self.dex = stats['dex']
            self.int = stats['int']
            self.spr = stats['spr']
        else:
            self.vit = 10
            self.str = 10
            self.agi = 10
            self.dex = 10
            self.int = 10
            self.spr = 10

        self.update_sub_stats()

    def update_sub_stats(self):
        self.max_hp = 100 + (self.vit * 20)
        self.max_mp = 50 + (self.spr * 10)
        self.p_atk = 10 + (self.str * 2.5)
        self.m_atk = 10 + (self.int * 2.5)
        self.p_def = 0 + (self.vit * 1.5)
        self.m_def = 0 + (self.int * 1.5)
        self.spd = 100 + self.agi
        self.acc = 80 + (self.dex * 0.5)
        self.crit_rate = 5 + (self.dex * 0.2)
        self.crit_dmg = 1.5

        self.current_hp = self.max_hp
        self.current_mp = self.max_mp

    def to_dict(self):
        return {
            "name": self.name,
            "job_class": self.job_class,
            "level": self.level,
            "exp": self.exp,
            "gold": self.gold,
            "stats": {
                "vit": self.vit, "str": self.str, "agi": self.agi,
                "dex": self.dex, "int": self.int, "spr": self.spr
            }
        }

class Monster:
    def __init__(self, name, player_level):
        self.name = name
        self.level = player_level

        self.max_hp = 50 + (player_level * 30)
        self.current_hp = self.max_hp
        self.atk = 5 + (player_level * 5)
        self.exp_reward = 10 * player_level
        self.gold_reward = 5 * player_level

    def attack(self, target):
        damage = max(1,int(self.atk - target.p_def))
        target.current_hp -= damage
        return damage

def save_game(player):
    data = player.to_dict()
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("\n[System] Game Saved Successfully")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("\n[System] No save file found!")
        return None

    with open(SAVE_FILE, 'r') as f:
        data = json.load(f)


    return Character(
        data['name'],
        data['job_class'],
        data['level'],
        data['exp'],
        data['gold'],
        data['stats']
    )

def display_stats(self):
    # --- Helper Function for Health Bars ---
    def draw_bar(current, max_val, length=20):
        # Calculate how many 'blocks' are full
        ratio = current / max_val
        filled_len = int(length * ratio)
        return "█" * filled_len + "-" * (length - filled_len)

    # --- The Header ---
    print(f"\n{'='*40}")
    print(f" 🛡️  CHARACTER SHEET: {self.name.upper()}")
    print(f"{'='*40}")
        
    # --- Basic Info ---
    print(f" Class: {self.job_class:<15}  Level: {self.level}")
    print(f" EXP:   {self.exp:<15}  Gold:  {self.gold}")
    print(f"{'-'*40}")
    
    print(f" HP:  {self.current_hp}/{self.max_hp:<5}")
    print(f" MP:  {self.current_mp}/{self.max_mp:<5}")
    print(f"{'-'*40}")

    # --- Main Stats (2 Columns) ---
    print(f" {'[ MAIN STATS ]':<17} | {'[ ATTRIBUTES ]'}")
    print(f" STR: {self.str:<12} |  VIT: {self.vit}")
    print(f" AGI: {self.agi:<12} |  DEX: {self.dex}")
    print(f" INT: {self.int:<12} |  SPR: {self.spr}")
    print(f"{'-'*40}")

    # --- Combat Stats (2 Columns) ---
    print(f" {'[ OFFENSE ]':<17} | {'[ DEFENSE ]'}")
    print(f" P.ATK: {self.p_atk:<10.1f} |  P.DEF: {self.p_def:.1f}")
    print(f" M.ATK: {self.m_atk:<10.1f} |  M.DEF: {self.m_def:.1f}")
    print(f" CRIT:  {self.crit_rate:<9.1f}% |  SPD:   {self.spd}")
    print(f"{'='*40}\n")

def visit_market(player):
    print("\n--- MARKETPLACE ---")
    print("Merchant: 'Items coming soon in v1.1!'")
    input("Press Enter to return...")

def visit_dungeon(player):
    print("\n--- DUNGEON ---")
    # Spawn a monster scaled to player level
    enemy_names = ["Slime", "Goblin", "Wolf"]
    monster = Monster(random.choice(enemy_names), player.level)
    
    print(f"A Lv.{monster.level} {monster.name} appears!")
    print(f"Monster HP: {monster.max_hp} | Atk: {monster.atk}")
    
    while monster.current_hp > 0 and player.current_hp > 0:
        action = input("\n[A]ttack or [R]un? > ").lower()
        if action == 'a':
            # Player attacks
            dmg = max(1, int(player.p_atk)) # Simplified (armor ignored for now)
            monster.current_hp -= dmg
            print(f"You hit {monster.name} for {dmg} damage!")
            
            if monster.current_hp <= 0:
                print(f"You defeated the {monster.name}!")
                player.gold += monster.gold_reward
                player.exp += monster.exp_reward
                print(f"Gained {monster.exp_reward} EXP and {monster.gold_reward} Gold.")
                break
            
            # Monster attacks
            dmg_taken = monster.attack(player)
            print(f"{monster.name} hits you for {dmg_taken} damage!")
            print(f"Your HP: {player.current_hp}/{player.max_hp}")
        
        elif action == 'r':
            print("You ran away!")
            break

def main():
    player = None
    
    # --- WELCOME SCREEN ---
    while not player:
        print("\n=== SIMPLE RPG ===")
        print("1. New Game")
        print("2. Load Game")
        choice = input("> ")
        
        if choice == '1':
            name = input("Enter Name: ")
            job = input("Enter Class: ")
            player = Character(name, job)
        elif choice == '2':
            player = load_game()
        else:
            print("Invalid choice.")

    # --- MAIN GAME LOOP ---
    while True:
        print(f"\n[{player.name} | Lv.{player.level} | HP:{player.current_hp}/{player.max_hp} | Gold:{player.gold}]")
        print("1. Go to Dungeon")
        print("2. Go to Market")
        print("3. View Stats")
        print("4. Save Game")
        print("5. Quit")
        
        choice = input("What will you do? > ")
        
        if choice == '1':
            visit_dungeon(player)
        elif choice == '2':
            visit_market(player)
        elif choice == '3':
            # A quick way to print all stats
            display_stats(player)
        elif choice == '4':
            save_game(player)
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
