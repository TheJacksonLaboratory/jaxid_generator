from suit import apps
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

APP_NAME = 'jaxid_generator'

class SuitConfig(DjangoSuitConfig):
    name = 'suit'
    verbose_name = 'Mbiome Core JAXid Generator'
    site_title = 'Mbiome Core JAXid Tracking'
    site_header = site_title
    index_title = verbose_name


    layout = 'vertical'
    list_per_page = 35

    # header_date_format = 'l, d-M-o'
    # header_time_format = 'H:i e'

    menu = (
            ParentItem(
                label='JAXid Record List',
                url='/{}/admin/id_generate/jaxiddetail'.format(APP_NAME),
                icon='fa th-list'),
            ParentItem('Reference Data',
                use_first_child_url=False,
                url='',
                children=[
                    ChildItem(model='id_generate.projectcode'),
                    ChildItem(model='id_generate.nucleicacidtype'),
                    ChildItem(model='id_generate.sampletype'),
                    ChildItem(model='id_generate.sequencingtype'),
                    ],
                icon='fa th-list'),
            ParentItem(
                label='Generate new JAXid''s',
                url='/{}/admin/id_generate/jaxiddetail/import/'.format(APP_NAME),
                icon='fa open-file'),
            ParentItem(
                label='Authorization',
                children=[
                    ChildItem('Staff', model='auth.user'),
                    ChildItem(model='auth.group'),
                    ],
                icon='fa th-list'),
           )
    # menu_handler = None
    menu_show_home = False


    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = False


#    # Enables two column layout for change forms with submit row on the right
    form_submit_on_right = False

    # Hide name/"original" column for all tabular inlines.
    # May be overridden in Inline class by suit_form_inlines_hide_original = False
    #form_inlines_hide_original = False

    form_size = {
        'default': apps.SUIT_FORM_SIZE_LARGE,
        'widgets': {
            'AutosizedTextarea': apps.SUIT_FORM_SIZE_X_LARGE,
            'Textarea': apps.SUIT_FORM_SIZE_X_LARGE,
        },
    }

#     # form_size setting can be overridden in ModelAdmin using suit_form_size parameter
#     #
#     # Example:
#     # ----------------------------------------------
#     # suit_form_size = {
#     #     'default': 'col-xs-12 col-sm-2', 'col-xs-12 col-sm-10',
#     #     'fields': {
#     #          'field_name': SUIT_FORM_SIZE_LARGE,
#     #          'field_name2': SUIT_FORM_SIZE_X_LARGE,
#     #      },
#     #      'widgets': {
#     #          'widget_class_name': SUIT_FORM_SIZE_FULL,
#     #          'AdminTextareaWidget': SUIT_FORM_SIZE_FULL,
#     #      },
#     #      'fieldsets': {
#     #          'fieldset_name': SUIT_FORM_SIZE_FULL,
#     #          'fieldset_name2': SUIT_FORM_SIZE_FULL,
#     #      }
#     # }
