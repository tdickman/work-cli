import click
import webbrowser

from work.managers import settings, jira as jira_manager


@click.command()
@click.argument('ticket', required=False)
def cli(ticket):
    jira = jira_manager.load()
    jira_default_project = settings.get_or_create('jira_default_project')
    jira_base_url = settings.get_or_create('jira_base_url')

    # Default to ticket for current branch
    if not ticket:
        raise Exception('todo')

    if ticket.isdigit():
        ticket = '{}-{}'.format(jira_default_project, ticket)

    issue = jira.issue(ticket)
    webbrowser.open_new_tab('{}/browse/{}'.format(jira_base_url, issue))
