import pytest
from sqlalchemy.exc import IntegrityError

from models.user import User as UserEntity
from repositories.user_repository import save_user, get_user_by_username, get_users
from schemas.user import UserCreate
from tests.database.db_fixtures import db_session, db_session_factory, db_tables, db_engine


@pytest.fixture(scope='session')
def user_schema():
    user_data = {
        "username": "user1",
        "password": "Str0ngPa55w0rd"
    }
    return UserCreate(username=user_data['username'], password=user_data['password'])


def test_user_model(user_schema):
    user = UserEntity(username=user_schema.username, password=user_schema.password)
    assert user.username == user_schema.username
    assert user.password == user_schema.password


@pytest.fixture(scope='session')
@pytest.mark.usefixtures('db_session')
def user_entity(db_session, user_schema):
    return save_user(db_session, user_schema)


def test_save_user_model_to_db(user_schema, user_entity):
    assert user_entity.username == user_schema.username
    assert user_entity.password == user_schema.password


@pytest.mark.usefixtures('db_session')
def test_find_existing_user(db_session, user_entity):
    test_user = get_user_by_username(db_session, user_entity.username)
    assert test_user.username == user_entity.username
    assert test_user.password == user_entity.password
    assert test_user.id == user_entity.id


@pytest.mark.usefixtures('db_session')
def test_list_all_users(db_session, user_entity):
    users = get_users(db_session)
    assert type(users) is list
    assert len(users) == 1
    assert type(users[0]) is UserEntity
    test_user = users[0]
    assert test_user.id == user_entity.id


@pytest.mark.usefixtures('db_session')
def test_unique_usernames(db_session, user_entity, user_schema):
    with pytest.raises(IntegrityError) as er:
        new_user = save_user(db_session, user_schema)
    assert 'UNIQUE' in str(er.value.orig)
