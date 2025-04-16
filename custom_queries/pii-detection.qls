import python

/**
 * This query detects potential Personally Identifiable Information (PII) in your code.
 * It looks for identifiers like "CustomerID" or other fields that suggest sensitive information.
 */

// Find variables with names commonly associated with PII
from VariableDeclaration v
where v.getName().matches("(?i).*?(customerid|account|phone|email|ssn).*")
select v, "This variable may contain PII data."
