import click

# You may run program with following commands
# python pass_arguments_to_script_click_example.py --name Adrian -n 2
# or
# python pass_arguments_to_script_click_example.py --name
# More information at https://click.palletsprojects.com/en/7.x/


@click.command()
@click.option('--name', type=str, required=True, help='The person to greet.')
@click.option('-n', type=int, default=1)
def my_function(name, n):
    i = 0
    while i < n:
        print('Hello {}'.format(name))
        i += 1


if __name__ == '__main__':
    my_function()
