import requests

from clients.people.people_client import PeopleClient
from tests.assertions.people_assertions import *
from tests.helpers.people_helpers import *
from utils.print_helpers import pretty_print
from uuid import uuid4
from json import dumps
from config import BASE_URI

client = PeopleClient()


def test_read_all_has_dock(logger):
    """
    Test on hitting People GET API, we get a user named kent in the list of people
    """
    response = requests.get("http://0.0.0.0:5000/api/people")
    response_text = response.json()
    pretty_print(response_text)

    assert_that(response.status_code).is_equal_to(200)
    logger.info("User successfully read")
    first_names = [people['fname'] for people in response_text]
    assert_that(first_names).contains('Dock')


def test_new_person_can_be_added():
    unique_last_name = f'User {str(uuid4())}'
    payload = dumps({
        'fname': 'Kim',
        'lname': unique_last_name
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(204)

    response_text = requests.get(BASE_URI).json()
    pretty_print(response_text)
    new_users = [person for person in response_text if person['lname'] == unique_last_name]
    assert_that(new_users).is_not_empty()


def test_created_person_can_be_deleted():
    persons_last_name, _ = client.create_person()

    peoples = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(peoples, persons_last_name)['person_id']

    response = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_person_can_be_added_with_a_json_template(create_data):
    client.create_person(create_data)

    response = client.read_all_persons()
    peoples = response.as_dict

    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
