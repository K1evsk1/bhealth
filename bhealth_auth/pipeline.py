from social.backends.google import GoogleOAuth2
from social.backends.vk import VKOAuth2
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from client.models import Client


def create_user(**kwargs):
    unique_id = kwargs.get('unique_id', None)
    email = kwargs.get('email', None)
    name = kwargs.get('name', None)
    password = kwargs.get('password', None)
    gender = kwargs.get('gender', None)
    height = kwargs.get('height', None)
    age = kwargs.get('age', None)
    weight = kwargs.get('weight', None)
    date_of_birth = kwargs.get('date_of_birth', None)
    activity = kwargs.get('activity', None)
    count_training_to_week = kwargs.get('count_training_to_week', None)
    count_minute_to_training = kwargs.get('count_minute_to_training', None)
    goal = kwargs.get('goal', None)
    have_a_coach=2,
    avatar = kwargs.get('avatar', None)

    new_user = User.objects.create_user(unique_id, email=email)
    new_user.save()
    new_client = Client(user=new_user, unique_id=unique_id, name=name, gender=gender, height=height, age=age,
                        weight=weight, date_of_birth=date_of_birth, activity=activity,
                        count_training_to_week=count_training_to_week, count_minute_to_training=count_minute_to_training,
                        goal=goal, have_a_coach=2, avatar=avatar
                        )
    new_client.save()

    return new_user

def create_social_user(backend, response, user=None, *args, **kwargs):
    '''
    Overriding social.create_user function, with adding
    new client into Client model
    '''
    social_id = None
    social_username = None
    social_email = None
    social_avatar = None

    if isinstance(backend, GoogleOAuth2):
        social_id = response['id']
        social_username = '%s %s' % (response['name']['givenName'], response['name']['familyName'])
        social_email = response['emails'][0]['value']
        social_avatar = response['image']['url']
    if isinstance(backend, VKOAuth2):
        social_id = str(response['user_id'])
        social_username = '%s %s' % (response['first_name'], response['last_name'])
        social_avatar = response['user_photo']

    try:
        social_user = Client.objects.get(unique_id=social_id)
        return {'is_new': False}
    except ObjectDoesNotExist:
        new_user = create_user(**{'unique_id': social_id, 'email': social_email,
                                  'name': social_username, 'avatar': social_avatar})
    return {'is_new': True,
            'user': new_user}
