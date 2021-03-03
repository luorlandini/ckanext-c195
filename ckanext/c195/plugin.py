import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckanext.c195.helpers as h


class C195Plugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'c195')

    def get_helpers(self):
        return {
            'c195_get_organizations': h.get_organizations,
            'c195_get_groups': h.get_groups,
        }


