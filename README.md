## About the project
In this project, we are making it so that all of the actions done by PostgreSQL will be logged by the blockchain, which is shared between all of the nodes in the network. When something is done in PostgreSQL, it will be logged, which will be tracked by our program, and that query is going to be synced between all nodes. This allows for logging, recovery, and distributive qualities.

## Development
After a lot of testing, when run on different computers, whenever there is a transaction on one computer, it is shown on every other computer. We have added functionality for making it easy to join a network using the p2pnetwork module. The way we made p2p connections for testing was RadminVPN, this allowed us to make the computer think we were in the same network, so we could use our VPN IPs to refer to each other's computers, and all ports would be open by default.

## Use case
The way this can be used is:-
* In banks, it can be used as a ledger system where every node in the network is known and all the transactions must have a recovery in case of a catastrophic failure resulting in the shutdown of the entire network, or even if a single computer is shut down, the rest will work without any issues.
* Supply Chain Management Systems could also make very good use of our system to keep track of their goods to assure quality and authenticity.
* Healthcare systems, where a ledger system can help maintain patient records, prescriptions, and other health-related data.
* Government agencies and departments, where a ledger system can help track budgets, contracts, and other financial transactions.
* E-commerce platforms, where a ledger system can help manage transactions between buyers and sellers and ensure the accuracy of inventory and shipping information.
* Cryptocurrency and blockchain systems, where a ledger system is used to record all transactions on the network and ensure the accuracy and security of the system.

# Instructions
## Do these in order in root directory to install

## For Windows:
Execute this in the base folder
<pre><code>psql -U postgres -f pgscript.sql
</code></pre>

After installing PostgreSQL
Make sure to change log_collector to "on", log_statement to "all", log_destination to "jsonlog" in PostgreSQL's config

## For UNIX based OS:
Run `./install.sh` to install it in one command

# Functionalities
The functionalities are listed as:-
* Recording transactions: The system should be able to record all types of transactions, including sales, purchases, transfers, and other financial events.
* Immutable records: The records should be immutable, meaning that once a transaction is recorded, it cannot be altered or deleted. This ensures that the data is accurate and cannot be tampered with.
* Data integrity: The system should have measures in place to ensure the integrity of the data, including authentication, authorization, and encryption.
Reporting and analysis: The system should be able to generate reports and provide analytical insights into the data.
* User management: The system should have user management functionalities, including user authentication and authorization, role-based access controls, and audit logs.
* Auditing and compliance: The system should have auditing and compliance functionalities, including the ability to track changes, generate audit trails, and maintain compliance with regulatory requirements.
* Backup and recovery: The system should have backup and recovery functionalities to ensure that data is recoverable in the event of a disaster or data loss. (Potentially to be added)