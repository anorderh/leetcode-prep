// https://leetcode.com/problems/binary-tree-level-order-traversal/description/

// Incorrect solution, 15/34 test cases solved
// Outputting each node levels' values in seperated vectors within a vector
// My solution seperated nodes with different parents into different vectors
// However, Leetcode desired nodes with different parents (but on the same level) to be in the
// same vector.
// EX:
// Tree Structure -> [1,2,3,4,null,null,5]
// Output -> [ [1], [2,3], [4], [5]]
// Expected -> [ [1], [2,3], [4, 5]]

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<TreeNode*> rootCopy;
        vector<vector<TreeNode*>> nodes;
        vector<vector<int>> result;

        if (root == nullptr) {
            return result;
        }
        rootCopy.push_back(root);
        nodes.push_back(rootCopy);

        while (nodes.size() != 0) {
            vector<int> pair;

            for (TreeNode* node: nodes[0]) {
                pair.push_back(node->val);
            }
            result.push_back(pair);

            vector<TreeNode*> nodePair;
            for (TreeNode* node: nodes[0]) {
                if (node->left != nullptr) {
                    nodePair.push_back(node->left);
                }
                if (node->right != nullptr) {
                    nodePair.push_back(node->right);
                }
                if(nodePair.size() != 0) {
                    nodes.push_back(nodePair);
                    nodePair.clear();
                }
            }

            nodes.erase(nodes.begin());
        }

        return result;
    }
};

// Correct solution, utilizing a queue to store children and output into desired lists if req met

 class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        if(root == nullptr) return {};
        vector<vector<int>> res;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty())
        {
            int count = q.size();
            vector<int> temp;
            while(count--)
            {
                TreeNode* curr = q.front();
                q.pop();
                temp.push_back(curr->val);
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
            
            res.push_back(temp);
        }
        return res;
    }
};
