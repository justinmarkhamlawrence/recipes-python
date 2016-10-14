class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://justinlawrence@localhost:5432/recipes_list"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://justinlawrence@localhost:5432/recipes_list_test"
    DEBUG = True
