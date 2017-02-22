import click

from work.managers import settings, jira as jira_manager


@click.command()
@click.argument('ticket', required=False)
def cli(ticket):
    jira = jira_manager.load()
    jira_default_project = settings.get_or_create('jira_default_project')

    # Default to ticket for current branch
    if not ticket:
        raise Exception('todo')

    if ticket.isdigit():
        ticket = '{}-{}'.format(jira_default_project, ticket)

    issue = jira.issue(ticket)
    output = '-- Summary: {}\n\n-- Description:\n{}\n\n'.format(issue.fields.summary, issue.fields.description)
    for index, comment in enumerate(issue.fields.comment.comments):
        output += '-- Comment {} ({}):\n{}\n\n'.format(index, comment.author, comment.body)

    print(output.strip())
