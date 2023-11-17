import os
from pathlib import Path
from affinda import AffindaAPI, TokenCredential
from dotenv import load_dotenv


load_dotenv()

def upload_resume_to_affinda(file_path):
    token = os.environ.get(
        "AFFINDA_API_KEY",
        'aff_daeadbf43a7d3715c6bf01210d31bc7724ed1a06',
    )
    collection_identifier = os.environ.get(
        "AFFINDA_COLLECTION_ID",
        'UECgssMN',
    )

    credential = TokenCredential(token=token)
    client = AffindaAPI(credential=credential)

    with open(file_path, "rb") as f:
        document = client.create_document(file=f, collection=collection_identifier)
    
    
    cv_identifier = document.as_dict().get('meta', {}).get('identifier')
    return cv_identifier