import python

/**
 * This query detects possible exposure of PII in Python code.
 */

// Look for variable declarations or assignments with PII-like patterns
from Variable v
where v.getName().matches("(?i).*?(customerid|account|phone|email|ssn).*")
select v, "This variable may expose PII."
