import sys
import json

import cloudkit_helper as ck


def get_zones():
    """Print out the zones"""
    print("Print out all the zones (we are just using default.)")
    ck.dump_zones()

def get_all_jokes():
    """Query CloudKit to get all the `joke` records.  We are also
    writing it to a file so we can debug it"""
    print('Querying all jokes...')
    jokes = ck.query_records('joke')
    ck.write_json_to_file(jokes, "jokes.json")
    for joke in jokes:
        print("========joke=========")
        print(joke["fields"])


def add_a_joke():
    new_joke_data = {
        'operations': [{
            'operationType': 'create',
            'record': {
                'recordType': 'joke',
                'fields': {
                    'question': {
                        'value': 'What did the number 0 say to the number 8?'
                    },
                    'response': {
                        'value': 'I like you belt..'
                    },
                    'rating_negative': {
                        'value': 10
                    },
                    'rating_positive': {
                        'value': 10
                    }
                }
            }
        }]
    }
    print('Posting operation to create quote...')
    result_modify_jokes = ck.cloudkit_request(
        '/development/public/records/modify',
        json.dumps(new_joke_data))
    print(result_modify_jokes['content'])

def add_joke_of_the_day(recordID):
    """Create a new joke of the day record and post it to iCloud
    Note: the recordID should come from processing the data
    """

    new_joke_of_the_day_data = {
        'operations': [{
            'operationType': 'create',
            'record': {
                'recordType': 'joke_of_the_day',
                'fields': {
                    'joke': {
                         'value': {
                             'recordName': '3CCB6936-49BD-4CDF-8FAB-63F362C5D1B8',
                             'zoneID:': {
                                 'zoneName': '_defaultZone'
                             },
                             'action': 'DELETE_SELF'
                         }
                     }
                }
            }
        }]
    }

    print('Posting operation to create quote...')
    result_modify_jokes = ck.cloudkit_request(
        '/development/public/records/modify',
        json.dumps(new_joke_of_the_day_data))
    print(result_modify_jokes['content'])



def main():
    #get_zones()
    #get_all_jokes()
    add_a_joke()
    #add_joke_of_the_day('ABC')


    

if __name__ == '__main__':
    main()
