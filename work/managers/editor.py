import tempfile
import os
import sys
from subprocess import call


EDITOR = os.environ.get('EDITOR', 'vim')


def prompt(prompts):
    """Open a vim editor with the specified variables specified and allow the user to enter values."""
    message = ''
    for item in prompts:
        message += '#! {}\n{}\n'.format(item['name'].title(), item.get('default', ''))
    response = start(message).decode()

    # Parse response
    output = {}
    for response in response.split('#!'):
        try:
            key, value = response.split('\n', 1)
        except ValueError:
            continue
        key = key.strip().lower()
        output[key] = value.strip()

    # Make sure all values were found
    for item in prompts:
        if item['name'] not in output:
            print('Missing {} in edited file'.format(item['name']))
            print(output)
            sys.exit(1)
        if item.get('valid_values') and output[item['name']] not in item['valid_values']:
            print('{} set to invalid value'.format(item['name']))
            print(output)
            sys.exit(1)
    return output


def start(initial_message):
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_message.encode())
        tf.flush()
        call([EDITOR, tf.name])

        # do the parsing with `tf` using regular File operations.
        # for instance:
        tf.seek(0)
        edited_message = tf.read()
        return edited_message
