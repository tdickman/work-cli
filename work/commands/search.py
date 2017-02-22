import click

from work.managers import settings, jira as jira_manager


@click.command()
@click.argument('query')
def cli(query):
    jira = jira_manager.load()
    jira_default_project = settings.get_or_create('jira_default_project')

    issues = jira.search_issues('project={} and (summary~"{}" or description~"{}")'.format(jira_default_project, query, query))

    for issue in issues:
        if str(issue.fields.status) != 'Done':
            print('{} ({}): {}'.format(issue, issue.fields.status, issue.fields.summary))
