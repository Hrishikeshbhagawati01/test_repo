import python

/**
 * This query detects possible exposure of PII in Python code.
 */

from Variable v
where v.getName().matches("(?i).*?(customerid|account|balance|phone|email|ssn).*")
select v, "This variable may expose PII."
