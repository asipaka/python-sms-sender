import os
import phonenumbers
from phonenumbers import NumberParseException
from twilio.rest import Client

def load_phone_numbers(file_path, default_country):
    """
    Load phone numbers from a .txt file and validate them with country-specific formats.
    
    Args:
        file_path (str): Path to the .txt file containing phone numbers.
        default_country (str): Default country code for parsing phone numbers (e.g., 'US', 'NG').

    Returns:
        list: Valid phone numbers in E.164 format.
    """
    if not file_path.endswith('.txt'):
        raise ValueError("Only .txt files are allowed.")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    valid_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            phone = line.strip()
            try:
                # Parse and validate phone number
                parsed_number = phonenumbers.parse(phone, default_country)
                if phonenumbers.is_valid_number(parsed_number):
                    # Convert to E.164 format
                    valid_numbers.append(phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))
                else:
                    print(f"Invalid phone number format: {phone}")
            except NumberParseException as e:
                print(f"Error parsing phone number '{phone}': {e}")

    if not valid_numbers:
        raise ValueError("No valid phone numbers found in the file.")

    return valid_numbers

def send_sms(account_sid, auth_token, sender_number, recipient_numbers, message):
    """
    Sends SMS to a list of recipient numbers using Twilio.

    Args:
        account_sid (str): Twilio Account SID.
        auth_token (str): Twilio Auth Token.
        sender_number (str): Twilio-verified sender number.
        recipient_numbers (list): List of recipient phone numbers in E.164 format.
        message (str): The SMS message to send.
    """
    client = Client(account_sid, auth_token)

    for number in recipient_numbers:
        try:
            message_response = client.messages.create(
                body=message,
                from_=sender_number,
                to=number
            )
            print(f"Message sent to {number}. SID: {message_response.sid}")
        except Exception as e:
            print(f"Failed to send message to {number}. Error: {e}")

def main():
    print("\n-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!\n")
    correct_password = "Tec"
    user_password = input("Enter the access password: ")
    print("\n!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-!!-\n")
    if user_password != correct_password:
        print("Incorrect password. Access denied.")
        print("--------------------------------------------")
    else:
        print("Welcome to E-SMS v1.0.0")

        # Get user inputs for Twilio credentials
        print("\n*********************************************************")
        account_sid = input("Enter your Twilio Account SID: ").strip()
        auth_token = input("Enter your Twilio Auth Token: ").strip()
        sender_number = input("Enter your Twilio-verified phone number or Sender ID: ").strip()
        print("*********************************************************\n")

        # Default country for phone number validation
        default_country = input("Enter your default country code (e.g., 'US', 'NG'): ").strip()

        print("\n-----------------------------------------------------------------------\n")

        # Get the phone numbers file
        file_path = input("Enter the path to your phone number list (.txt only): ").strip()
        try:
            recipient_numbers = load_phone_numbers(file_path, default_country)
            print(f"Loaded {len(recipient_numbers)} valid phone numbers.")
        except Exception as e:
            print(f"Error loading phone numbers: {e}")
            return
        
        print("\n-----------------------------------------------------------------------\n")

        # Get the message to send
        message = input("Enter the message you want to send: ").strip()

        print("\n-----------------------------------------------------------------------\n")

        # Confirm and send messages
        confirm = input(f"Are you sure you want to send this message to {len(recipient_numbers)} recipients? (y/n): ").strip().lower()
        print("-----------------------------------------------------------------------\n")
        if confirm == 'y':
            try:
                send_sms(account_sid, auth_token, sender_number, recipient_numbers, message)
            except Exception as e:
                print(f"Error sending SMS: {e}")
        else:
            print("Operation cancelled.")

if __name__ == "__main__":
            main()
