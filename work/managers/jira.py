from jira import JIRA

from work.managers import settings


def load():
    jira_base_url = settings.get_or_create('jira_base_url')
    jira_username = settings.get_or_create('jira_username')
    jira_password = settings.get_or_create('jira_password')

    return JIRA(jira_base_url, basic_auth=(jira_username, jira_password))
