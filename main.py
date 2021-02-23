"""
The developed module parses an json object (file) obtained using the Twitter
API. The module contains a function get_multiple_fields_by(json_data: dict,
detail=False) to provide access to various parts of the json object.
For example, get_user_choice_by(inner_data) asks the user to enter the
dictionary key whose meaning he wants to view. 
https://github.com/akerni/lab3task2
"""
import json
import twitter2

# def parse_json_by(filepath: str) -> dict:
#     with open(f'{filepath}', 'r', encoding='utf-8-sig') as file:
#         return json.load(file)

def get_json_data():
    return twitter2.get_json_friends()


def get_multiple_fields_by(json_data: dict, detail=False):
    """
    The function provides an access to various parts of the json object. 
    """
    def _show_mono_fields_by(dct: dict, _detail):
        info = [
            (set, '(...)'),
            (dict, '{...}'),
            (list, '[...]'),
        ]
        if isinstance(dct, dict):
            print('Info:')
            for idx, pair in enumerate(dct.items()):
                if not _detail and idx == 5:
                    break

                k, v = pair[0], pair[1]

                if isinstance(v, (dict, set, list)):
                    curr_info = "".join(x[1] for x in info if isinstance(v, x[0]))
                    print(f'--- {k}: {curr_info}')
                    continue

                print(f'--- {k}: {v}')
            print()

    if not isinstance(json_data, dict):
        if isinstance(json_data, list) and all(isinstance(data, (str, int)) for data in json_data):

            if not json_data:
                print('Empty.')
                return None

            print('Info:')
            for val in json_data:
                print(f'--- {val}')
            return None
        json_data = json_data[get_user_choice_by(json_data) - 1]

    _show_mono_fields_by(json_data, detail)
    inner_fields = {}
    for key, val in json_data.items():
        if isinstance(val, (dict, set, list)):
            inner_fields.update({
                key: val
            })

    return inner_fields


def get_user_choice_by(inner_data):
    """
    The fucntion asks the user to enter the dictionary key whose meaning he
    wants to view.
    """
    if isinstance(inner_data, list):
        while True:
            print(f'We have {len(inner_data)} data blocks inside.')
            try:
                inner_answer = int(input(f'Pick which to show: '))
                if inner_answer not in range(1, len(inner_data) + 1):
                    raise ValueError
                return inner_answer
            except ValueError:
                print('!_Invalid answer_!\n')

    while True:
        print('Inner info:')
        for idx, key in enumerate(inner_data.keys()):
            print(f'{idx + 1}. {key}')
        try:
            answer = int(input("Enter: "))
            if answer not in range(1, len(inner_data.keys()) + 1):
                raise ValueError
            return answer
        except ValueError:
            print('!_Invalid answer_!\n')


def main():
    # js = (parse_json_by('test.json'))
    js = get_json_data()

    while True:
        inner_data = get_multiple_fields_by(js, detail=True)
        if not inner_data:
            print('Json file is ended.')
            break

        user_choice = get_user_choice_by(inner_data)
        js = inner_data[list(inner_data.keys())[user_choice - 1]]


if __name__ == '__main__':
    main()
