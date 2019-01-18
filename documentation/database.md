# Database

## Database tables

All tables include columns for creation date and latest modification date.

### Account

Each row represents a user account. Passwords are stored in plain text.

```SQL
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
```

### Candidate

Each row represents a candidate, and contains information such as an optional URL and the id of the user account that nominated the candidate. The selected field indicates whether the candidate has already been nominated.

```SQL
CREATE TABLE candidate (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	selected BOOLEAN NOT NULL, 
	url VARCHAR(144) NOT NULL, 
	nominator_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (selected IN (0, 1)), 
	FOREIGN KEY(nominator_id) REFERENCES account (id)
);
```

### Votes

The approval and veto tables are identical in all but name. Each row represents one approval/veto of one candidate by one user.

```SQL
CREATE TABLE approval (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	voter_id INTEGER NOT NULL, 
	candidate_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(voter_id) REFERENCES account (id), 
	FOREIGN KEY(candidate_id) REFERENCES candidate (id)
);
```

```SQL
CREATE TABLE veto (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	voter_id INTEGER NOT NULL, 
	candidate_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(voter_id) REFERENCES account (id), 
	FOREIGN KEY(candidate_id) REFERENCES candidate (id)
);
```

### Tag

The tag table contains only a varchar field as its primary key, because it is intended as a maximally general category identifier. The business logic for adding and utilizing tags hasn't been implemented yet.

```SQL
CREATE TABLE tag (
	name VARCHAR(50) NOT NULL, 
	PRIMARY KEY (name)
);
```

Tags is is a join table that represents a many to many relationship between the candidate and tag tables.

```SQL
CREATE TABLE tags (
	tag_name VARCHAR(50) NOT NULL, 
	candidate_id INTEGER NOT NULL, 
	PRIMARY KEY (tag_name, candidate_id), 
	FOREIGN KEY(tag_name) REFERENCES tag (name), 
	FOREIGN KEY(candidate_id) REFERENCES candidate (id)
);
```

## Normalization

The database is in the second normal form. It falls short of being in the third normal form because of e.g. a transitive dependency between id, username, and name in the candidate table. This was considered an acceptabe choice for the sake of the clarity of the code.

## Database diagram
![database diagram](https://github.com/OAarne/heppa/blob/master/documentation/database_diagram.png "Database diagram")