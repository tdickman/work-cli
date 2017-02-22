import click

from work.managers import settings, editor, jira as jira_manager


@click.group()
def cli():
    """Create something."""
    pass


@cli.command('story')
def story():
    """Create a story."""
    create('Story')


@cli.command('bug')
def bug():
    """Create a bug."""
    create('Bug')


def create(issue_type):
    jira_default_project = settings.get_or_create('jira_default_project')
    jira_username = settings.get_or_create('jira_username')
    jira_base_url = settings.get_or_create('jira_base_url')
    jira = jira_manager.load()
    values = editor.prompt([
        {'name': 'summary'},
        {'name': 'description'},
        {'name': 'type', 'default': issue_type, 'valid_values': ['Bug', 'Issue', 'Story']}
    ])

    issue = jira.create_issue(
        project=jira_default_project,
        summary=values['summary'],
        description=values['description'],
        issuetype={'name': values['type']}
    )
    issue.update(assignee={'name': jira_username})
    print('{}: {}/browse/{}'.format(issue, jira_base_url, issue))
