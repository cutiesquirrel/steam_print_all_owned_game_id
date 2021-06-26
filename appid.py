import os
import sys
import urllib.request
import xml.etree.ElementTree as ET


def get_steam_xml(username):
    xml_url = 'http://steamcommunity.com/id/{your_id_here}/games?tab=all&xml=1'.format(
        username)
    return urllib.request.urlopen(xml_url)


def get_ids(username):
    tree = ET.parse(get_steam_xml(username))
    root = tree.getroot()

    return [game.find('appID').text for game in root.iter('game')]

def main():
    username = 'UR_USERNAME_HERE'
    path_to_save = '.'
    id_list = get_ids(username)
    with open(path_to_save + '/ids.txt', 'w', encoding='utf-8') as f:
           f.write(",\n".join(id_list))

if __name__ == '__main__':
    main()
