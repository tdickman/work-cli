import os
import json


def set(key, value):
    settings_folder = os.path.expanduser('~/.global_work/')
    if not os.path.exists(settings_folder):
        os.makedirs(settings_folder)

    settings_file = os.path.join(settings_folder, 'settings.json')
    if not os.path.exists(settings_file):
        with open(settings_file, 'w') as f:
            f.write(json.dumps({}))

    with open(settings_file, 'r+') as f:
        settings = json.load(f)
        settings[key] = value
        f.seek(0)
        f.write(json.dumps(settings))


def get(key):
    settings_folder = os.path.expanduser('~/.global_work/')
    settings_file = os.path.join(settings_folder, 'settings.json')
    if not os.path.exists(settings_file):
        return None

    with open(settings_file) as f:
        settings = json.load(f)
        return settings.get(key)


def get_or_create(key, prompt=None):
    value = get(key)
    if value is not None:
        return value

    # Prompt user to craete a new value
    if prompt is None:
        prompt = 'Enter a value for {}: '.format(key)
    value = input(prompt)
    set(key, value)
    return value
