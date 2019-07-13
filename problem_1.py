import json
import pprint


def get_json_format(dic):
    return json.dumps(dic)


def main():
    bio = {
        'name': 'Rizqullah Taufanriansyah',
        'age': 21,
        'address': 'Ahmad Yani 60, Kota Bogor',
        'hobbies': ['Reading', 'Coding', 'Learning'],
        'is_married': False,
        'list_school': [
            {
                'name': 'SMAN 2 Bogor',
                'year_in': 2013,
                'year_out': 2016,
                'major': 'IPA',
            },
            {
                'name': 'Universitas Bakrie',
                'year_in': 2017,
                'year_out': 2021,
                'major': 'Informatics',
            }
        ],
        'skills': [
            {
                'skill_name': 'English',
                'level': 'Advanced',
            },
            {
                'skill_name': 'Python',
                'level': 'Advanced'
            }
        ],
        'interest_in_coding': True,
    }
    pprint.pprint(get_json_format(bio))


if __name__ == "__main__":
    main()
