from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_balance():
    from web3 import Web3
    import config

    web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/56cdea790ef844a284e61b0ec74075d2'))

    balance = web3.eth.get_balance('0xB1d20CEC597a6F8506315C4090b5a5F846ec190E')

    return f"Balance: {balance}"

if __name__ == '__main__':
    app.run()


# from_account = '0xB1d20CEC597a6F8506315C4090b5a5F846ec190E'
# to_account = '0x510912c2035467895c433b7642912162841df570'

# private_key = '0x810f096086d89dbd5d5a635f9e206e4a3193e9cb89ac08801c0708325422ff82'
# address1 = Web3.to_checksum_address(from_account)
# address2 = Web3.to_checksum_address(to_account)

# nonce = web3.eth.get_transaction_count(address1)

# tx = {
#     'nonce': nonce,
#     'to': address2,
#     'value': web3.to_wei(0.002, 'ether'),
#     'gas': 21000,
#     'gasPrice': web3.to_wei(40, 'gwei'),
# }

# signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
