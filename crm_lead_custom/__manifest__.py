{
    'name': 'CRM Lead Custom Field',
    'version': '19.0.1.0.0',
    'category': 'CRM',
    'summary': 'Adds a custom field to CRM Leads',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
