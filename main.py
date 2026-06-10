import random
import string
from typing import Union, Dict

# Name Assignment (variables and constants)
MINING_REWARD = 3.125
current_block_height = 800000
BTC_TO_SATS = 100_000_000


# Functions
def calculate_total_reward(blocks_mined) -> float:
    return blocks_mined * MINING_REWARD


def is_valid_tx_fee(fee):
    return fee > 0


def is_large_balance(balance):
    return balance >= 50.0


def tx_priority(size_bytes, fee_btc):
    fee_rate = fee_btc / size_bytes

    if fee_rate >= 0.00005:
        return "high"
    elif fee_rate >= 0.00001:
        return "medium"
    else:
        return "low"


def is_mainnet(network):
    return network.lower() == "mainnet"


def is_in_range(value):
    return 100 <= value <= 200


def is_same_wallet(wallet1, wallet2):
    return wallet1 is wallet2


def normalize_address(address):
    return address.strip().lower()


def add_utxo(utxos, new_utxo):
    utxos.append(new_utxo)
    return utxos


def find_high_fee(fee_list):
    highest_fee = max(fee_list)
    return (fee_list.index(highest_fee), highest_fee)


def get_wallet_details():
    return ("satoshi_wallet", 50.0)


def get_tx_status(tx_pool, txid):
    return tx_pool.get(txid, "not found")


def unpack_wallet_info(wallet_info):
    owner, balance = wallet_info
    return f"Wallet {owner} has balance: {balance} BTC"


def calculate_sats(btc: float) -> int:
    return int(btc * BTC_TO_SATS)


def generate_address(prefix: str = "bc1q") -> str:
    suffix = "".join(
        random.choices(string.ascii_lowercase + string.digits, k=32)
    )
    return prefix + suffix


def validate_block_height(height):
    if not isinstance(height, int):
        return (False, "Block height must be an integer")

    if height < 0:
        return (False, "Block height cannot be negative")

    return (True, "Valid block height")


def halving_schedule(blocks):
    rewards = {}
    initial_reward = 50 * BTC_TO_SATS
    halving_interval = 210000

    for block in blocks:
        halvings = block // halving_interval
        rewards[block] = initial_reward // (2 ** halvings)

    return rewards


def find_utxo_with_min_value(utxos, target):
    valid_utxos = [u for u in utxos if u["value"] >= target]

    if not valid_utxos:
        return {}

    return min(valid_utxos, key=lambda x: x["value"])


def create_utxo(txid: str, vout: int, **kwargs) -> Dict[str, Union[str, int]]:
    utxo = {
        "txid": txid,
        "vout": vout
    }

    utxo.update(kwargs)
    return utxo