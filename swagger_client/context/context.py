from swagger_client.api.auth_api import AuthApi
from swagger_client.api_client import ApiClient


class ApiContext(object):

    def __init__(self, name, password, base_req):
        self.client = ApiClient()
        self.name = name
        self.password = password
        self.base_req = base_req

    def refresh_acc_num_and_seq(self):
        data = AuthApi().get_account(address=self.name)
        if data.result is not None:
            self.base_req.account_number = data.result.account_number
            self.base_req.sequence = data.result.sequence


class BaseReq(object):

    def __init__(self, chain_id, fees, from_address, gas, memo):
        self.account_number = "0"
        self.chain_id = chain_id
        self.fees = fees
        self.from_address = from_address
        self.gas = gas
        self.gas_adjustment = "1.1"
        self.memo = memo
        self.sequence = "0"
        self.simulate = False

    def set_fees(self, amount):
        self.fees[0].amount = amount

    def set_gas(self, gas):
        self.gas = gas

    def set_memo(self, memo):
        self.memo = memo

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_sequence(self, sequence):
        self.sequence = sequence


if __name__ == "__main__":
    ApiContext("coinex1h6favnlytw3lgpy8cm6lcv530z0ctj6rplwt06", "123", None).refresh_acc_num_and_seq()
