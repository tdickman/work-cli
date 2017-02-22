import click

from work.managers import settings, jira as jira_manager


@click.command()
def cli():
    jira = jira_manager.load()
    jira_default_project = settings.get_or_create('jira_default_project')

    issues = jira.search_issues('project={} and assignee = currentUser()'.format(jira_default_project))

    for issue in issues:
        if str(issue.fields.status) != 'Done':
            print('{} ({}): {}'.format(issue, issue.fields.status, issue.fields.summary))
