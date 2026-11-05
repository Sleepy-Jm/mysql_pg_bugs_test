CREATE TABLE parent (
		parent_field INTEGER CONSTRAINT pk_parent PRIMARY KEY
	);
	CREATE TABLE child (
		child_field INTEGER,
		CONSTRAINT fk_child FOREIGN KEY (child_field) REFERENCES parent
(parent_field)
	);
	CLUSTER parent USING pk_parent;
