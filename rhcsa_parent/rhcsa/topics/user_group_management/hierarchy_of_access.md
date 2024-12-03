* System immediately stops at any step when finds a match and uses those permissions


1. Is user owner? uses the user owner chmod permissions
1. Any user ACLs? Unions those permissions
1. Is group owner? uses the group ownder chmod permissions
1. Any group ACL's?  Unions those group permissions
1. Get permissions of others entity