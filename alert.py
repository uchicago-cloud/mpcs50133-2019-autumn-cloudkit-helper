import sys
import json

import cloudkit_helper as ck

def add_alert(message):
    """Create a new alert with a custom message"""

    data = {
        'operations': [{
            'operationType': 'create',
            'record': {
                'recordType': 'alert',
                'fields': {
                    'message': {
                        'value': message,
                    }
                }
            }
        }]
    }

    print('Posting operation to create quote...')
    result = ck.cloudkit_request(
        '/development/public/records/modify', json.dumps(data))
    print(result['content'])


def main():
    message = input("What would you like to say to your users?\n")
    add_alert(message)


if __name__ == '__main__':
    main()
