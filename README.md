django-simple-ledger
====================

Application that allow to keep track of financial transactions between different object of the system.
Basically if you have model class the instance of that model can pay money to the instance of the different model.

Transactions are based on 4 types:

* Deposit transation - Sets a deposit from one object to another
* Withdrawal transation - One object takes money back from deposit that is was given to other object
* Credit transaction - States that one objects owes some amount of money to another object
* Debit transaction - Make the actual payment from one object to another based on credit transation. Payment can be made from the previous deposit.


### Adding transaction

```python
import ledger.common as ledger
from ledger import trasaction

transaction = transaction.DepositTransaction()
trasaction.agent_from = client_object
trasaction.agent_to = service_provider_object # or merchant
transaction.amount = 1000

ledger.ledger.addTransaction(transaction, transaction_id="payment_type") # transaction_id is optional
```
