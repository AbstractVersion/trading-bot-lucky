import erc20token
import json

# Init SDK without a private key (for generic blockchain queries)
token_sdk = erc20token.SDK(provider_endpoint_uri='http://localhost:8545',                    contract_address='0x04f72aa40046c5fb3b143aaba3ab64d1a82410a7', 
                       contract_abi=json.loads(contract_abi))