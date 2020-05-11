import json

from swagger_client.api.auth_api import AuthApi
from swagger_client.api_client import ApiClient
from swagger_client.api.bank_api import BankApi
from swagger_client.api.transactions_api import TransactionsApi
from swagger_client.models.account import Account
from swagger_client.models.tx_broadcast import TxBroadcast
from swagger_client.models.std_tx_core import StdTxCore
import ctypes


class ApiContext(object):

    def __init__(self, from_address, name, password, base_req, lib):
        self.client = ApiClient()
        self.from_address = from_address
        self.name = name
        self.password = password
        self.base_req = base_req
        self.lib = lib

    def refresh_acc_num_and_seq(self):
        (data, data_str) = AuthApi().get_account(address=self.from_address)
        self.base_req['account_number'] = data.result.account_number
        self.base_req['sequence'] = data.result.sequence

    def sign_and_broadcast(self, unsigned_bytes):
        sign = self.lib.SignAndBuildBroadcast
        sign.restype = ctypes.c_char_p
        bz = sign(self.name, self.password, str.encode(unsigned_bytes), self.base_req['chain_id'].encode("utf-8"),
                  "block".encode("utf-8"), int(self.base_req['account_number']), int(self.base_req['sequence']))
        tx = json.loads(bz)
        tx = tx['tx']
        std_tx = StdTxCore(tx['msg'], tx['fee'], tx['memo'], tx['signatures'])
        tx_broadcast = TxBroadcast(std_tx, 'block')
        (resp, resp_str) = TransactionsApi().broadcast_tx(tx_broadcast)
        return resp


def test():
    # init keybase
    key_name = "key_name".encode("utf-8")
    password = "12345678".encode("utf-8")
    from_addr = "coinex10c22dwn7hxps77tnkpj5pzu9zcpq5zf76xms55"

    lib = ctypes.CDLL('./wallet_mac.so')
    lib.BearInit('tmp'.encode("utf-8"))
    get_address = lib.GetAddress
    get_address.restype = ctypes.c_char_p

    # init param
    fee = [
        {
            'denom': 'cet',
            'amount': "50000000"
        }
    ]
    gas = "500000"
    req = {
        'account_number': "0",
        'chain_id': "coinexdex-test1",
        'fees': fee,
        'from': from_addr,
        'gas': gas,
        'gas_adjustment': "1.1",
        'memo': "",
        'sequence': "0",
        'simulate': False,
    }
    base_req = req
    account = Account(base_req, fee, "0")

    # init context
    ctx = ApiContext(from_addr, key_name, password, base_req, lib)
    ctx.refresh_acc_num_and_seq()

    # transfer coins
    (res, res_str) = BankApi().send_coins("coinex1cdc2t8k3gexm0aad6xaxlpcprcqr768vzk8u6z", account)
    ctx.sign_and_broadcast(res_str.data)


if __name__ == "__main__":
    test()
