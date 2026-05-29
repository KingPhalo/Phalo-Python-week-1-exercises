import random
import string
from typing import Union, Tuple, List, Dict

# Name Assignment (variables and constants)
MINING_REWARD = 3.125
current_block_height = 800000
BTC_TO_SATS = 100_000_000 

# Functions
def calculate_total_reward(blocks_mined) -> int:
    return blocks_mined * MINING_REWARD


def is_in_range(value):
    return 100 <= value <=200


def is_same_wallet(wallet1,wallet2):
    return wallet1 is wallet2 


def normalize_address(address):
    return address.strip().lower()


def add_utxo(utxos, new_utxo):
    utxos.append(new_utxo)
    return utxos


def is_mainnet(network):
    return network.lower() == "mainnet"

def is_large_balance(balance):
    return balance > 50.0


def is_valid_tx_fee(fee):
    return 0.00001 <= fee <= 0.01


def tx_priority(size_bytes, fee_btc):
    fee_rate = fee_btc / size_bytes

    if fee_rate >= 0.00005:
        return "high"
    elif fee_rate >= 0.00001:
        return "medium"
    else:
        return "low"




def find_high_fee(fee_list):
    for i, fee in enumerate(fee_list):
        if fee > 0.005:
            return (i, fee)
    return None


def generate_address(prefix: str = "bc1q") -> str:
    suffix_length = 32 - len(prefix)
    suffix = "".join(random.choices(string.ascii_letters + string.digits, k=suffix_length))
    return prefix + suffix


def halving_schedule(blocks):
    reward = 50 * BTC_TO_SATS
    interval = 210000
    result = {}

    for b in blocks:
        halvings = b // interval
        result[b] = reward // (2 ** halvings)

    return result


def find_utxo_with_min_value(utxos, target):
    valid = [u for u in utxos if u["value"] >= target]
    if not valid:
        return {}
    return min(valid, key=lambda x: x["value"])


def create_utxo(txid, vout, **kwargs):
    utxo = {"txid": txid, "vout": vout}
    utxo.update(kwargs)
    return utxo


def get_wallet_details():
    return ("satoshi_wallet", 50.0)


def get_tx_status(tx_pool, txid):
    return tx_pool.get(txid, "not found")

def unpack_wallet_info(wallet_info):
    name, balance = wallet_info
    return f"Wallet {name} has balance: {balance} BTC"


def calculate_sats(btc: float) -> int:
    return int(btc * BTC_TO_SATS)


def generate_address(prefix: str = "bc1q") -> str:
    suffix_length = 32 - len(prefix)
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=suffix_length))
    return prefix + suffix 


def validate_block_height(height):
    if not isinstance(height, int):
        return (False, "Block height must be an integer")

    if height < 0:
        return (False, "Block height cannot be negative")

    if height > 800000:
        return (False, "Block height seems unrealistic")

    return (True, "Valid block height")

def halving_schedule(blocks):
    result = {}
    reward = 50 * BTC_TO_SATS
    interval = 210000

    for b in blocks:
        halvings = b // interval
        result[b] = reward // (2 ** halvings)

    return result


def find_utxo_with_min_value(utxos, target):
    valid = [u for u in utxos if u["value"] >= target]

    if not valid:
        return {}

    return min(valid, key=lambda x: x["value"])


def create_utxo(txid: str, vout: int, **kwargs) -> Dict[str, Union[str, int]]:
    """Create a UTXO dictionary with optional additional fields."""
    # TODO: Create a base dictionary with txid and vout
    # TODO: Merge any extra keyword arguments into the base

