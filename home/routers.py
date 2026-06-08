class CapturaRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'home' and model.__name__ == 'LeadCaptura':
            return 'captura'
        return None

    def db_for_write(self, model, **hints):
        return None  # no escribir en captura

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
