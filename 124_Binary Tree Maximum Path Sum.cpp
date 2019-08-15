
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //博客分析   https://blog.csdn.net/Findingxu/article/details/99649130
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        maxPSum(root,maxSum); //递归一定要把参数 maxSum带上
        return maxSum;        
    }
    int maxPSum(TreeNode* root,int &sumMax){ //加上&
        if(root == NULL) //确保递归函数有终止条件
            return 0;
        //左边最大值，右边最大值
        int leftMax = maxPSum(root->left,sumMax); // 调用递归求得子问题
        int rightMax = maxPSum(root->right,sumMax);
        // 下面两种方式都要当前根节点参与进来 
        //方式一：如果路径跨越左右子树
        int passRoot = root->val + max(0,leftMax) + max(0,rightMax); //跟0比，如果小于0就不要带上
        //方式二：如果路径只在一边
        //使用该种方式进行递归，保证从底至当前节点拥有单条路径，不分叉，这样leftMax和rightMax才能获得各自单条不分叉路线，才可以拼接成方式一
        int noRoot = root->val + max(0,max(leftMax,rightMax)); 
        //sumMax里面已经包含了当前root的历史最大值，只有当根节点参与进来的两种方式得到更大值，才会更新sumMax
        sumMax = max(sumMax,max(passRoot,noRoot)); 
        
        //return sumMax; //出错，说明还没有很了解递归
        return noRoot; // 递归只能通过第二种方式
    }
};