# Accounts Merge

```javascript
var accountsMerge = function(accounts) {  
    let emailToNameMap = {};
    
    var createGraph = function() {
        let graph = {};
        for (let emails of accounts) {
            for (let i = 1; i < emails.length; i++) {    
                
                emailToNameMap[emails[i]] = emails[0];

                if (!(emails[i] in graph)) {
                    graph[emails[i]] = [];
                }
                if (i > 1) {
                    graph[emails[1]].push(emails[i]);
                    graph[emails[i]].push(emails[1]);
                }
            }
        }
        return graph;
    }   
    
    let emailGraph = createGraph();
    let ans = [];
    let visited = {};    
        
    for (let emailKey in emailGraph) {
        
        if (emailKey in visited) continue;
        
        let q = [emailKey];
        visited[emailKey] = true;
        let emailsPerPerson = [];
                
        while (q.length > 0) {
            const email = q.shift();
            emailsPerPerson.push(email);
            
            for (let emailEdge of emailGraph[email]) {
                if (!(emailEdge in visited)) {
                    visited[emailEdge] = true;
                    q.push(emailEdge);
                }
            }        
        }
        emailsPerPerson.sort();
        emailsPerPerson.unshift(emailToNameMap[emailKey]);
        ans.push(emailsPerPerson);
    }
    return ans;
};
```

# Complexity
### Time: O(Sum(accounts))
### Space: O(Sum(emailGraph)) where emailGraph is the size of our graph
