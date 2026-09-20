-- SQL Environment Test Script (Compatible with SQLite / MySQL / PostgreSQL)
CREATE TABLE IF NOT EXISTS test_env (
    id INTEGER PRIMARY KEY,
    module_name TEXT NOT NULL,
    status TEXT NOT NULL
);

INSERT INTO test_env (id, module_name, status) VALUES (1, 'Database Environment', 'SUCCESS');
INSERT INTO test_env (id, module_name, status) VALUES (2, 'Termux SQL Execution', 'READY');

SELECT * FROM test_env;
