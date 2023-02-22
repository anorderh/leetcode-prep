## Leetcode Explanation

*provided by @Neetcode*


<img src="youtubeimg.png" title="" alt="youtube" width="191"> [Valid Parentheses - Stack - Leetcode 20 - Python - YouTube](https://www.youtube.com/watch?v=WTzjTskDFMg)

### Drafting & Initial Takeaways

* Can't ever start with a clothing parenthesis, bc nothing is open

* When starting w/ an opening parenthesis, you can start with as many as you want
  
  * So long as they are closed accordingly later

* When parentheses are closed, they can be removed from future consideration

## Implementation

- When removing parentheses, it will occur at front and end's of 1st parentheses considered
  
  - Closing parentheses will be matched to **most recent** opening parentheses. From this, we can reason a **stack** would be most applicable

<img src="file:///Users/anorde/Coding/Leetcode/TopInterviewQuestions/ValidParentheses/1.png" title="" alt="1.png" width="291">

- To ensure a closing parentheses *closes* an open parentheses, a relationship needs to be established
  
  - This can be done so using a **HashMap**

![2.png](/Users/anorde/Coding/Leetcode/TopInterviewQuestions/ValidParentheses/2.png)

## Complexity Analysis

- Time - O(n)
  
  - Will iterate through entire string's characters once

- Space - O(n)
  
  - Stack which can scale up to 'n', string's size if all opening parentheses

## Code

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<>();
        Map<Character, Character> bracketLookup = new HashMap<>();
        
        // Bracket mapping
        bracketLookup.put(')', '(');
        bracketLookup.put('}', '{');
        bracketLookup.put(']', '[');
        
        // Iterate through string, use toCharArray
        for (char c : s.toCharArray()) {
            if (bracketLookup.containsKey(c)) { // Closing paren.
                // If stack not empty && matching char, pop()
                if (brackets.size() != 0 && brackets.peek() == bracketLookup.get(c)) {
                    brackets.pop();
                } else {
                    return false;
                }
            } else { // Opening paren
                brackets.push(c);
            }
        }

        if (brackets.size() == 0) return true;
        return false;
    }
}
```
