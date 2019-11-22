#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import os


@click.group()
def cli():
    click.echo('\n\033[1;32mWelcome to emmm-cli!\033[0m\n')


@click.command()
def vue():
    """vue init
    """
    try:
        os.system('cp ~/GitHub/emmmLibrary/vue/vue-requests . -rf')
        os.system('cp ~/GitHub/emmmLibrary/vue/vue-iconfont ./assets -rf')
        click.echo('\033[1;34mDone\033[0m')
    except Exception as e:
        click.echo('\n\033[1;31m[Error]\033[0m')
        click.echo(e)
        click.echo('\n\033[1;31m[Error End]\033[0m')


@click.command()
@click.argument('name')
def flask():
    """flask init
    需要获取用户输入项目名称，然后通过名称区替换示例文件。
    """
    try:
        ...
        click.echo('\033[1;34mDone\033[0m')
    except Exception as e:
        click.echo('\n\033[1;31m[Error]\033[0m')
        click.echo(e)
        click.echo('\n\033[1;31m[Error End]\033[0m')


if __name__ == '__main__':
    cli.add_command(vue)
    cli.add_command(flask)

    cli()
