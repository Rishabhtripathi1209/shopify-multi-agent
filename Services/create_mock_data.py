def generate_mock_orders():
    return [
        {
            "id": 101,
            "created_at": "2024-05-01T10:00:00Z",
            "processed_at": "2024-05-01T14:00:00Z",
            "fulfillment_status": None,
            "cancelled_at": None,
            "line_items": [
                {"name": "Wireless Mouse", "quantity": 1},
                {"name": "Keyboard", "quantity": 1}
            ],
        },
        {
            "id": 102,
            "created_at": "2024-05-02T12:00:00Z",
            "processed_at": None,
            "fulfillment_status": None,
            "cancelled_at": "2024-05-03T08:00:00Z",
            "line_items": [
                {"name": "Laptop Stand", "quantity": 1}
            ],
        },
        {
            "id": 103,
            "created_at": "2024-05-04T09:00:00Z",
            "processed_at": "2024-05-05T10:00:00Z",
            "fulfillment_status": "fulfilled",
            "cancelled_at": None,
            "line_items": [
                {"name": "USB-C Hub", "quantity": 1},
                {"name": "Wireless Mouse", "quantity": 1}
            ],
        }
    ]
