# python-sms-sender

# SMS Sender

This project is a Python-based SMS Sender that allows users to send SMS messages to a list of phone numbers. The application provides features such as phone number validation, country-specific formatting using the `phonenumbers` library, and error handling. The script uses Twilio as the SMS sending service. Use a paid twilio account for full access to other features such as, sending to unverified numbers, custom sender ID etc

## Features

1. **Load Phone Numbers from a .txt File**
   - Only `.txt` files are allowed.
   - The script validates phone numbers against country-specific formats.

2. **Phone Number Validation**
   - Ensures that all phone numbers are valid and formatted using the `phonenumbers` library.
   - Supports default country codes for parsing.

3. **Send SMS Messages**
   - Users can send SMS messages to validated numbers.
   - Allows customization of the sender ID (requires configuration in Twilio).

4. **Error Handling**
   - Includes robust error handling for invalid phone numbers, file-related issues, and API errors.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.7 or later installed.
- Required Python libraries:
  - `twilio`
  - `phonenumbers`
- A Twilio account with:
  - Account SID
  - Auth Token
  - Verified phone number (or configured sender ID for custom names).

## Installation

1. Clone the repository or download the script file.
2. Install the required Python libraries:
   ```bash
   pip install twilio phonenumbers or pip install requirements.txt
   ```
3. Ensure your `.txt` file containing phone numbers is properly formatted, with one phone number per line.

## Usage

1. Run the script:
   ```bash
   python tecsms.py
   Password : "Tec" or change in source code
   ```

2. Follow the prompts:
   - Enter your Twilio credentials (Account SID and Auth Token).
   - Provide your Twilio-verified phone number or sender name (if configured).
   - Specify the path to your `.txt` file with phone numbers.
   - Enter the message you want to send.

3. Confirm the operation to send SMS messages.

## Example

### Sample Phone Numbers File (`numbers.txt`):
```
+1234567890
+1987654321
+441234567890
```

### Running the Script:
```
Enter your Twilio Account SID: <Your_SID>
Enter your Twilio Auth Token: <Your_Auth_Token>
Enter your Twilio-verified phone number or sender name: MyBusiness
Enter your default country code (e.g., 'US', 'NG'): US
Enter the path to your phone number list (.txt only): numbers.txt
Enter the message you want to send: Hello! This is a test message.
Are you sure you want to send this message to 3 recipients? (y/n): y
```

### Output:
```
Loaded 3 valid phone numbers.
Message sent to +1234567890. SID: SMXXXXXXXXXXXXXXXXXXX
Message sent to +1987654321. SID: SMXXXXXXXXXXXXXXXXXXX
Message sent to +441234567890. SID: SMXXXXXXXXXXXXXXXXXXX
```

## Notes

- **Twilio Phone Number Requirements**: You must use a verified Twilio phone number or a configured sender ID.
- **Rate Limits**: Be aware of rate limits and costs associated with Twilio SMS.
- **Error Logs**: Any invalid phone numbers or failed message deliveries will be logged to the console.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

## Acknowledgments

- [Twilio Python Library Documentation](https://www.twilio.com/docs/libraries/python)
- [Python `phonenumbers` Library Documentation](https://pypi.org/project/phonenumbers/)

---
For any issues or feature requests, feel free to reach out.
