from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'suicide',
    'version': '1.0.0',
    'name': 'Suicide',
    'author': 'ANDYzytnb',
    'link': 'https://github.com/your-repo',
    'dependencies': {
        'mcdreforged': '>=1.6.2'
    }
}

def on_info(server, info):
    if info.content == '!kill':
        if not info.is_player:
            server.reply(info, '只有玩家可以使用此命令！')
        else:
            server.execute(f'kill {info.player}')

def on_load(server, old_module):
    server.register_help_message('!kill', '自杀')

def on_unload(server):
    pass