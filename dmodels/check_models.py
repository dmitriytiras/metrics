import os
import xml.etree.ElementTree as ET
from decouple import config


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


def getFolders(export_dae):
    dirs = os.listdir(export_dae)
    print(dirs)


def checkCityModels(started_folder, city_counter, city, objects_xml, result_absent_models):
    missing_count = 0
    dae_counter = 0
    dae_list_from_dir = []
    path_city_model, dirs_city_models, models = next(os.walk(started_folder + '/' + city))
    for model in models:
        if model.endswith('.dae'):
            dae_counter += 1
            dae_list_from_dir.append(model)

    models_list_from_xml, dae_models_id_from_xml = parseObjectsXML(started_folder + '/' + folder + '/' + objects_xml)
    print(f'======================== {city_counter} {str(city).upper()} ========================')
    if len(dae_models_id_from_xml) != len(dae_list_from_dir):
        print(f'======================== {city_counter} {str(city).upper()} ========================', file=result_absent_models)
        print(f'Amount of models in the objects.xml {len(dae_models_id_from_xml)}', file=result_absent_models)
        print(f'Amount of models in the {city} folder {len(dae_list_from_dir)}', file=result_absent_models)

        if len(dae_models_id_from_xml) > len(dae_list_from_dir):
            print(' ------ models from objects.xml which are not in folder ------', file=result_absent_models)
            for model in dae_models_id_from_xml:
                if not (findInList(model[1], dae_list_from_dir)):
                    print(model[1], file=result_absent_models)
        elif len(dae_models_id_from_xml) < len(dae_list_from_dir):
            print(' ------ models from folders which are not in objects.xml ------', file=result_absent_models)
            for model in dae_list_from_dir:
                if not (findInList(model, models_list_from_xml)):
                    print(model, file=result_absent_models)


if __name__ == '__main__':
    path_with_exported_models = config('path_with_exported_models', default='.')
    file_objects_xml = config('file_objects_xml', default='objects.xml')
    absent_models = config('absent_models', default='missing_models.txt')

    file_results = open(absent_models, 'w')
    path, dirs, city = next(os.walk(path_with_exported_models))

    city_counter = 0
    total_missing_count = 0
    for folder in dirs:
        city_counter += 1
        checkCityModels(path_with_exported_models, city_counter, folder, file_objects_xml, file_results)

    file_results.close()
