from datetime import datetime, timedelta

from database.models import User


def time():
    return datetime.utcnow()+timedelta(hours=10)


def name_maker(model: dict, key: str = "name") -> dict:
    try:

        first_name = model["first_name"]
        second_name = model["second_name"]
        third_name = model["third_name"]

        model.pop("first_name")
        model.pop("second_name")
        model.pop("third_name")

        if first_name == None:
            first_name = ''
        if second_name == None:
            second_name = ''
        if third_name == None:
            third_name = ''

        name = second_name + ' ' + first_name + ' ' + third_name

        model[key] = name.lstrip(' ').rstrip(' ').replace('  ', ' ')

        return model
    except Exception as e:
        print(e)
        raise Exception
