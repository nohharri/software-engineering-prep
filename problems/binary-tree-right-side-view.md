# Binary Tree right side view

https://leetcode.com/problems/binary-tree-right-side-view/

```javascript
var rightSideView = function(root) {
    let ans = [];
    let heightCheckedMap = {};
    let currHeight = 0;
    
    var traverse = function(r, currHeight) {
        if (r === null) {
            return;
        }
        if (!(currHeight in heightCheckedMap)) {
            heightCheckedMap[currHeight] = true;
            ans.push(r.val);
        }
        traverse(r.right, currHeight + 1);
        traverse(r.left, currHeight + 1);
    }
    
    traverse(root, 0);
    
    return ans;
};
```
# Complexity

### Time: O(N)
* We are traversing through the whole tree.

### Space: O(logN)
* The recursion stack will only be the size of the tree. We are also storing heightCheckedMap but we are only storing logN nodes.
