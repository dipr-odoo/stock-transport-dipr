{
    'name' : 'Dispatch management System',
    # 'version' : '1.2',
    'summary': 'Stock_transport',
    # 'sequence': 10,
    'description': """
        Stock Transport App
    """,
    # 'category': 'Real Estate/Brokerage',
    'application': True,
    'depends': ['base','stock_picking_batch','fleet'],
    'data' :[
        'security/ir.model.access.csv',
        'views/fleet_vehicle_model_category_views.xml'
    ],
    'demo': [
       
    ],

}