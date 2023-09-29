# ATM-Management-System
This application is an ATM management system which performs the operations such as Cash Withdraw, Balance Enquiry, Deposit, Transfer using Python and sqlite3

### Overview
The ATM Management System is a Python application designed to simulate the operations of an Automated Teller Machine (ATM). This system allows users to perform various banking transactions including withdrawing funds, depositing funds, checking account balances, and transferring the money. The system uses the SQLite database to store and manage user account information securely.

### Features
**1.User Registration:** New users can be added into the database by including their details into it like account number, pin, initial deposit.  
**2.Login:** Registered users can log in to their accounts using their account number and PIN.  
**3.Account Balance Enquiry:** Users can check their account balances to view their available funds.  
**4.Cash Withdrawal:** Users can withdraw cash from their accounts by specifying the desired amount. The system will dispense cash if the account has sufficient funds.  
**5.Cash Deposit:** Users can deposit cash into any account which is already stored in the database by specifying the account number and amount they want to deposit. It deposits the amount into specified account.  
**6.Cash Transfer:** Users can transfer cash to any account in the database from their account by specifying the account number and amount they want to transfer. It not only deposits the amount into specified account but also reduce the amount from the user account.  
**7.Logout:** Users can securely log out of their accounts to prevent unauthorized access by clicking quit button.  

### Technologies Used
**- Python:** The core programming language used to develop the ATM system.
**- SQLite3:** The database management system used to store and retrieve user account information.

### Usage
To use the atm management system after adding details to the database login to perform acyions by using account number and respective pin. Next, you will find options which are deposit, cash withdrawl, transfer, balance enquiry. To deposit the money to any account use deposit. To withdrawl the cash, use cash withdrawl. To transfer the money to any account from your account, use transfer. To check the available balance, use balance enquiry.

### Database Schema
###### Data table:
**- account_number:** The unique account number for each user.
**- pin:** The encrypted PIN of the user.
**- balance:** The current account balance.

### Contributions
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or create a pull request on the project's GitHub repository.

### License
This ATM Management System is licensed under the MIT License.

### Contact
If you have any questions or need assistance, you can reach out to the project maintainer:  
PANDETI LAKSHMI PRASANNA  
lakshmiprasanna.lp07@gmail.com
