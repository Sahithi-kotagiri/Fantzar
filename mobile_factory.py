class MobileFactory:
    PRICES = {
        'A': 10.28, 'B': 24.07, 'C': 33.30,
        'D': 25.94, 'E': 32.39, 'F': 18.77,
        'G': 15.13, 'H': 20.00, 'I': 42.31,
        'J': 45.00, 'K': 45.00, 'L': 30.00
    }
    
    PARTS = {
        'A': 'LED Screen', 'B': 'OLED Screen', 'C': 'AMOLED Screen',
        'D': 'Wide-Angle Camera', 'E': 'Ultra-Wide-Angle Camera',
        'F': 'USB-C Port', 'G': 'Micro-USB Port', 'H': 'Lightning Port',
        'I': 'Android OS', 'J': 'iOS OS', 'K': 'Metallic Body', 'L': 'Plastic Body'
    }

    @staticmethod
    def validate_order(components):
        required_parts = {'Screen', 'Camera', 'Port', 'OS', 'Body'}
        component_parts = {MobileFactory.get_part_type(component) for component in components}
        if required_parts != component_parts:
            return False
        return True

    @staticmethod
    def calculate_total(components):
        total = sum(MobileFactory.PRICES[component] for component in components)
        return round(total, 2)

    @staticmethod
    
    def create_order(components):
        if not MobileFactory.validate_order(components):
            return None

        total_price = MobileFactory.calculate_total(components)
        parts = [MobileFactory.PARTS[component] for component in components]
        order_id = 'some-id'  # Generate or retrieve order ID dynamically
        
        # Construct the response JSON string with "total" before "parts"
        response_json = f'{{"order_id": "{order_id}", "total": {total_price}, "parts": {parts}}}'
        
        return response_json

    
    @staticmethod
    def get_part_type(component):
        if component in ['A', 'B', 'C']:
            return 'Screen'
        elif component in ['D', 'E']:
            return 'Camera'
        elif component in ['F', 'G', 'H']:
            return 'Port'
        elif component in ['I', 'J']:
            return 'OS'
        elif component in ['K', 'L']:
            return 'Body'
