from configparser import ConfigParser

def config(filename='conf.ini', section='model'):
    parser = ConfigParser()
    parser.read(filename)
   
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        db['path']=""
        ##raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def confcreate(lokasi, filename='conf.ini', section='model'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        params = parser['model']
        params['path']= lokasi
        with open(filename,'w') as f:
            parser.write(f)
    else:
        config_obj = ConfigParser()
        config_obj[section] = {
            "path":lokasi
        }
        with open(filename,'w') as t:
            config_obj.write(t)
