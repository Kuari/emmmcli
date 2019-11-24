#!/usr/bin/python
# -*- coding: utf-8 -*-
import click
import os

import replaceFlask


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.group()
def cli():
    # click.echo('\n\033[1;32mWelcome to emmm-cli!\033[0m\n')
    click.echo('\n')


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def vue():
    """在vue-cli创建文件的基础上，将自定义的拦截器、模板组件、字体文件放置到项目文件中。
    """
    try:
        # 放置预设文件
        os.system('cp ~/GitHub/emmmLibrary/vue/vue-requests/* . -rf && \
                  cp ~/GitHub/emmmLibrary/vue/vue-iconfont ./assets -rf && \
                  cp ~/GitHub/emmmLibrary/vue/vue-components/example.vue \
                  ./src/components && \
                  rm ./src/components/HelloWorld.vue && \
                  cp ~/GitHub/emmmLibrary/vue/App.vue ./src && \
                  cp ~/GitHub/emmmLibrary/vue/main.js ./src')
        # 初始化库
        os.system('yarn add vue-router vuex element-ui axios -D')
        click.echo('\033[1;34mDone\033[0m')
    except Exception as e:
        click.echo('\n\033[1;31m[Error]\033[0m')
        click.echo(e)
        click.echo('\n\033[1;31m[Error End]\033[0m')


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--name', prompt='New Project Name',
              help='The new project name.')
def flask(name):
    """需要获取用户输入项目名称，然后通过名称区替换示例文件。
    """
    try:
        # 将模板文件夹移动到当前文件夹并且改名为新的项目名称
        flaskPath = os.path.join('~/GitHub/emmmLibrary', 'flask')
        os.system('cp ' + flaskPath + ' ./' + name + ' -rf')
        # 首先更换文件内容，将server改为新的项目名称
        emmmPath = os.path.join('.', name)
        replaceFlask.replaceFileContent(emmmPath, 'server', name)
        # 然后更换文件名，将server改为新的项目名称
        replaceFlask.replaceDirName(emmmPath, 'server', name)
        click.echo('\033[1;34mDone\033[0m')
    except Exception as e:
        click.echo('\n\033[1;31m[Error]\033[0m')
        click.echo(e)
        click.echo('\n\033[1;31m[Error End]\033[0m')


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def version():
    click.echo('heihei')


if __name__ == '__main__':
    cli.add_command(vue)
    cli.add_command(flask)
    cli.add_command(version)

    cli()
