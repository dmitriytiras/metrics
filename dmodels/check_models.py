import os
import xml.etree.ElementTree as ET


def findInList(model_name, dae_models):
    if model_name in dae_models:
        return True
    else:
        return False


def parseObjectsXML(file):
    if os.path.exists(file):
        tree = ET.parse(file)
        root = tree.getroot()
        dae_models_id = []
        models_list = []
        for building in root.findall('building'):
            # print(building.tag, building.attrib)
            part = building.findall('part')
            for id in part:
                id_part = id.get('id')
                model = id.get('model')
                dae_models_id.append([id_part, model])
                models_list.append(model)
    else:
        print(f'file {file} does not exist')
    return models_list, dae_models_id


if __name__ == '__main__':
    path, dirs, files = next(os.walk("data/spb/"))
    file_objects_xml = 'data/spb/objects.xml'
    dae_counter = 0
    dae_list_from_dir = []
    for file in files:
        if file.endswith('.dae'):
            dae_counter += 1
            dae_list_from_dir.append(file)

    models_list_from_xml, dae_models_id_from_xml = parseObjectsXML(file_objects_xml)
    print(len(dae_models_id_from_xml))
    print(len(dae_list_from_dir))
    # for model in dae_models_from_xml:
    #      if not(findInList(model[1], dae_list)):
    #          print(model[1])

    # print(dae_models_from_xml[1])
    for model in dae_list_from_dir:
        if not(findInList(model, models_list_from_xml)):
            print(model)