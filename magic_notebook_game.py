import hashlib
import time

# ------------------------------
# The Block class: One notebook page
# ------------------------------
class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

# ------------------------------
# Create the Genesis Block
# ------------------------------
blockchain = []
def create_genesis_block():
    return Block(0, "Genesis Block - The club begins!", "0")

blockchain.append(create_genesis_block())

# ------------------------------
# Game Loop: Add new blocks manually
# ------------------------------
def add_new_block():
    transactions = input("\nEnter a fun transaction (like 'Alice sends 2 coins to Bob'): ")
    last_block = blockchain[-1]
    index = len(blockchain)
    previous_hash = last_block.hash

    print("🔐 Solving Proof of Work (Guess the right number)...")

    nonce = 0
    while True:
        temp_block = Block(index, transactions, previous_hash, nonce)
        if temp_block.hash.startswith("0000"):
            print("🎉 Puzzle Solved! Valid nonce found:", nonce)
            print("🧾 Block hash:", temp_block.hash)
            blockchain.append(temp_block)
            break
        nonce += 1

# ------------------------------
# View the Blockchain
# ------------------------------
def view_chain():
    print("\n📘 Magic Notebook (Blockchain):")
    for block in blockchain:
        print(f"\n🔗 Block {block.index}")
        print(f"Time: {block.timestamp}")
        print(f"Transactions: {block.transactions}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")

# ------------------------------
# Main Menu
# ------------------------------
while True:
    print("\n--- Magic Notebook Club ---")
    print("1. Add a new block (write a page)")
    print("2. View the notebook (blockchain)")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_new_block()
    elif choice == "2":
        view_chain()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Try again.")
