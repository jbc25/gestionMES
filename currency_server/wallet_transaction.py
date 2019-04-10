import requests
from django.conf import settings

def add_transaction(account, amount, concept=None):
    api_url = '{}api/v1/wallet/currency_purchased/'.format(settings.CURRENCY_SERVER_BASE_URL)
    headers = {'Authorization': settings.CURRENCY_SERVER_AUTH_HEADER}

    transaction_data = {
        "account": account.cif,
	    "amount": amount,
        "concept": concept,
    }

    r = requests.post(api_url, json=transaction_data, headers=headers)

    if r.ok:
        result = r.json()
        uuid = result['id']
        return True, uuid
    else:
        return False, r.status_code

