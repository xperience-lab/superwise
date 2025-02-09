import logging
import time
import requests
from .config import APPROVAL_TIMEOUT_DURATION_SECONDS, BACKEND_URL, SUPERWISE_PROJECT_ID, SUPERWISE_API_KEY

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# This should let users send the channels also which they want to use for sending message
def request_approval(channel_id: str, channel: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            message = func(*args, **kwargs)
            response = wait_for_approval(message, channel, channel_id)
            return message, response
        return wrapper
    return decorator

def wait_for_approval(message: str, channel: str, channel_id: str):
    # send requests to backend to be out for approval
    logging.info('sending reqeuest for approval....')
    request_id = send_approval_request(message, channel, channel_id)

    # poll for the request response and until you get response keep polling
    response = None
    start_time = time.time()
    logging.info('waiting for response')
    while (not response or response == 'PROCESSING'): 
        # fetch the response
        current_time = time.time()
        if (current_time - start_time > APPROVAL_TIMEOUT_DURATION_SECONDS):
            # TODO: Handle logging properly
            return 'Failed'

        response = get_status(request_id)
        logging.info(f'Response received {response}')
        
        if (response is None or response == 'PROCESSING'):
            time.sleep(3)
        
    return response


def send_approval_request(message: str, channel: str, channel_id: str) -> str:
    url = f"{BACKEND_URL}/approval-requests"
    payload = {"message": message, "channel": channel, "channel_id": channel_id}
    
    response = requests.post(
        url, 
        json=payload,
        headers={"x-superwise-project-id": SUPERWISE_PROJECT_ID, "x-superwise-api-key": SUPERWISE_API_KEY},
    )

    
    if response.status_code == 200:
        return response.json().get("request_id", "")
    else:
        raise Exception(f"Failed to send approval request: {response.text}")

def get_status(request_id: str) -> str:
    url = f"{BACKEND_URL}/approval-requests/status?id={request_id}"
    
    response = requests.get(
        url, 
        headers={"x-superwise-project-id": SUPERWISE_PROJECT_ID, "x-superwise-api-key": SUPERWISE_API_KEY}
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get status: {response}")
