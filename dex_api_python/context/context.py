import json
import pickle
from dex_api_python.api.auth_api import AuthApi
from dex_api_python.api_client import ApiClient
from dex_api_python.api.bank_api import BankApi
from dex_api_python.api.transactions_api import TransactionsApi
from dex_api_python.models.account import Account
from dex_api_python.models.tx_broadcast import TxBroadcast
from dex_api_python.models.std_tx_core import StdTxCore
import ctypes


class ApiContext(object):

    def __init__(self, from_address, name, password, base_req, lib, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.from_address = from_address
        self.name = name
        self.password = password
        self.base_req = base_req
        self.lib = lib

    def refresh_acc_num_and_seq(self):
        (data, data_str) = AuthApi(self.api_client).get_account(address=self.from_address)
        self.base_req['account_number'] = data.result.account_number
        self.base_req['sequence'] = data.result.sequence

    def sign_and_broadcast(self, unsigned_bytes):
        sign = self.lib.SignAndBuildBroadcast
        sign.restype = ctypes.c_char_p
        unsigned_tx_bytes = str.encode(unsigned_bytes, encoding='utf-8')
        bz = sign(self.name, self.password, unsigned_tx_bytes, self.base_req['chain_id'].encode("utf-8"),
                  "block".encode("utf-8"), int(self.base_req['account_number']), int(self.base_req['sequence']))
        tx = json.loads(bz)
        tx = tx['tx']
        std_tx = StdTxCore(tx['msg'], tx['fee'], tx['memo'], tx['signatures'])
        tx_broadcast = TxBroadcast(std_tx, 'block')
        (resp, resp_str) = TransactionsApi(self.api_client).broadcast_tx(tx_broadcast)
        return resp


def test():
    # init keybase
    key_name = "key_name".encode("utf-8")
    password = "12345678".encode("utf-8")
    to_addr = "coinex10c22dwn7hxps77tnkpj5pzu9zcpq5zf76xms55"

    lib = ctypes.CDLL('./wallet_mac.so')
    lib.BearInit('tmp'.encode("utf-8"))
    get_address = lib.GetAddress
    get_address.restype = ctypes.c_char_p

    # from_addr = "coinex10hmcj9sp6gef5244wxkwt9jgweuwpp9fjcmwng"
    from_addr_bytes = get_address(key_name)
    from_addr_str = str(from_addr_bytes, encoding='utf-8')

    # init param
    fee = [
        {
            'denom': 'cet',
            'amount': "600000"
        }
    ]
    coins = [
        {
            'denom': 'cet',
            'amount': "1000000000"
        }
    ]
    gas = "30000"
    req = {
        'account_number': "0",
        'chain_id': "coinexdex-test1",
        'fees': fee,
        'from': from_addr_str,
        'gas': gas,
        'gas_adjustment': "1.1",
        'memo': "",
        'sequence': "0",
        'simulate': False,
    }
    base_req = req
    account = Account(base_req, coins, "0")

    # init context
    ctx = ApiContext(from_addr_str, key_name, password, base_req, lib)
    ctx.refresh_acc_num_and_seq()

    # transfer coins
    (res, res_str) = BankApi().send_coins(to_addr, account)
    ctx.sign_and_broadcast(res_str.data)


if __name__ == "__main__":
    test()
