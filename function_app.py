import os
import azure.functions as func
import logging
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="test")
def test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url="https://techassessment4.vault.azure.net", credential=credential)

    secret_name = "Test"
    retrieved_secret = client.get_secret(secret_name)
    
    return func.HttpResponse(retrieved_secret)
