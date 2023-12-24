import xml.etree.ElementTree as ET
from xml.dom import minidom
import configparser
import yaml
import os
import json

# глобальный счетчик ID
user_counter = 1

# проверка существования файлов с данными
if os.path.exists('user_counter.txt'):
    with open('user_counter.txt', 'r') as file:
        user_counter = int(file.read())

# Функция для красивого форматирования XML (взята с интернета)
def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

# получение данных от пользователя
def get_user_data():
    global user_counter
    data = {}
    data['user_id'] = str(user_counter)
    user_counter += 1
    data['first_name'] = input("Введите имя пользователя: ")
    data['last_name'] = input("Введите фамилию пользователя: ")
    data['age'] = input("Введите возраст пользователя: ")
    return data

# функция сохранения данных в xml
def save_to_xml(data, filename):
    if os.path.exists(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
    else:
        root = ET.Element("root")
        tree = ET.ElementTree(root)

    new_data = ET.Element("data")
    for key, value in data.items():
        element = ET.SubElement(new_data, key)
        element.text = str(value)

    root.append(new_data)

    for elem in root.iter():
        elem.tail = ""

    xml_str = ET.tostring(root, encoding='utf-8').decode()
    xml_str = xml_str.replace('><', '>\n<')

    with open(filename, 'w') as f:
        f.write(xml_str)


def save_to_ini(data, filename):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
    section_name = f'user_{data["user_id"]}'
    config[section_name] = data
    with open(filename, 'w') as configfile:
        config.write(configfile)


def save_to_yaml(data, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as yamlfile:
            existing_data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        existing_data.append(data)
        with open(filename, 'w') as yamlfile:
            yaml.dump(existing_data, yamlfile)
    else:
        with open(filename, 'w') as yamlfile:
            yaml.dump([data], yamlfile)


def save_to_json(data, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            existing_data = json.load(file)
            existing_data.append(data)
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open(filename, 'w') as file:
            json.dump([data], file, indent=4)

def load_from_xml(filename):
    if os.path.exists(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for element in root:
            for sub_element in element:
                data[sub_element.tag] = sub_element.text
        return data
    else:
        return {}

# функция сохранения данных в ini
def load_from_ini(filename):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
        return dict(config['data'])
    else:
        return {}

# функция сохранения данных в yaml
def load_from_yaml(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return data
    else:
        return []

# функция сохранения данных в json
def load_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    else:
        return None


# получение данных от пользователя
user_data = get_user_data()

# сохранение данных в разных форматах
save_to_xml(user_data, 'data.xml')
save_to_ini(user_data, 'data.ini')
save_to_yaml(user_data, 'data.yaml')
save_to_json(user_data, 'data.json')

# сохранение счетчика пользователей
with open('user_counter.txt', 'w') as file:
    file.write(str(user_counter))

# загрузка данных из файлов
loaded_xml_data = load_from_xml('data.xml')
loaded_ini_data = load_from_ini('data.ini')
loaded_yaml_data = load_from_yaml('data.yaml')
loaded_json_data = load_from_json('data.json')

print(f"Данные сохранены и загружены в XML, INI и YAML форматах.")
print(f"Загруженные данные из XML: {loaded_xml_data}")
print(f"Загруженные данные из INI: {loaded_ini_data}")
print(f"Загруженные данные из YAML: {loaded_yaml_data}")
print(f"Загруженные данные из JSON: {loaded_json_data}")