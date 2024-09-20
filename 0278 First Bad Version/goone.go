/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersion(n int) int {
    lit := 0
    anc := -1
    for lit < n{
        anc = lit + (n - lit) / 2
        if isBadVersion(anc){
            n = anc
        }else{
            lit = anc + 1
        }
    }
    return n
}