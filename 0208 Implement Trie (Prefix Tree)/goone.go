type Trie struct {
    children map[rune]*Trie
    isEnd bool
}


func Constructor() Trie {
    return Trie{children: make(map[rune]*Trie)}
}


func (tits *Trie) Insert(word string) {
    node := tits
    for _, ch := range word {
        if _, exists := node.children[ch]; !exists {
            node.children[ch] = &Trie{children: make(map[rune]*Trie)}
        }
        node = node.children[ch]
    }
    node.isEnd = true
}


func (tits *Trie) Search(word string) bool {
    node := tits
    for _, ch := range word {
        if node.children[ch] == nil {
            return false
        }
        node = node.children[ch]
    }
    return node.isEnd
}


func (tits *Trie) StartsWith(prefix string) bool {
    node := tits
    for _, ch := range prefix {
        if node.children[ch] == nil {
            return false
        }
        node = node.children[ch]
    }
    return true
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */