# __manifest__.py

{
    'name': 'Sales Sequence',
    'summary': 'Add sequence numbers to sales order lines',
    'version': '1.0',
    'author': 'Your Name',
    'depends': ['sale'],
    'data': [
        'views/sale_order_line.xml',
    ],
}
