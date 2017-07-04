XML = False
HATEOAS = False

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'cameo'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'longitude': {
         'type':'string'
    },
    'latitude': {
        type: 'string'
        },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'personality': {
        'type': 'string',
    },
    # An embedded 'strongly-typed' dictionary.
    'age': {
        'type': 'string',
    },
}

users = {
    'item_title': 'user',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {'myGeo': users,
}

