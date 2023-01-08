//https://leetcode.com/problems/linked-list-cycle-ii/description/?envType=study-plan&id=level-1

// Unoptimized, using Map to track all nodes. If node revisited, this is start of cycle
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        map<ListNode*, int> nodes;
        int index = 0;

        while (head) {
            if (nodes.count(head) == 0) {
                nodes[head] = index;
                index++;
            } else {
                return head;
            }
            head = head->next;
        }
        return NULL;
    }
};

// Optimized, using slow & fast nodes until intersection. This intersect node is same distance from cycle start
// as is head. Iterate both intersection & head until same node, this is cycle's start.
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;

        // intersection point between slow & fast pointers
        // this node will be same distance away from cycle's start as head
        do {
            if (!fast or !fast->next) {
                return NULL;
            } else {
                slow = slow->next;
                fast = fast->next->next;
            }
        } while (slow != fast);
        
        // revert 'slow' to head and iterate both pointers
        // once pointers intersect, this will be cycle's start
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return slow;
    }
};
