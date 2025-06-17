def validate_account_number(account_number):
    if not isinstance(account_number, str) or len(account_number) != 10 or not account_number.isdigit():
        raise ValueError("Account number must be a 10-digit string.")

def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")

def load_json_file(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)