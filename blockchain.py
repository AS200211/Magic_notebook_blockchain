import hashlib
import time

# --------------------------
# Block Class
# --------------------------
class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions  # list of txs
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        tx_str = "".join(self.transactions)
        value = f"{self.index}{self.timestamp}{tx_str}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

# --------------------------
# Blockchain Class
# --------------------------
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []  # mempool

    def create_genesis_block(self):
        genesis_block = Block(0, time.time(), ["Genesis Block"], "0")
        self.mine_block(genesis_block)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, difficulty=4):
        if not self.pending_transactions:
            print("⛔ No transactions to mine!")
            return

        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )

        self.mine_block(new_block, difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []  # clear mempool

    def mine_block(self, block, difficulty=4):
        print(f"⛏️ Mining block {block.index}...")
        while not block.hash.startswith("0" * difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"✅ Block {block.index} mined: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

if __name__ == "__main__":
    my_coin = Blockchain()

    # Add some sample transactions
    my_coin.add_transaction("Alice → Bob: 5 BTC")
    my_coin.add_transaction("Bob → Charlie: 2 BTC")

    # Mine block containing the above transactions
    my_coin.mine_pending_transactions()

    # Add more
    my_coin.add_transaction("Charlie → Alice: 1 BTC")
    my_coin.add_transaction("Alice → Dave: 3 BTC")

    # Mine again
    my_coin.mine_pending_transactions()

    # Print the chain
    for block in my_coin.chain:
        print(f"\n🔗 Block {block.index}")
        print(f"Time: {time.ctime(block.timestamp)}")
        print(f"Transactions: {block.transactions}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}")
