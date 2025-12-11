func summaryRanges(nums []int) []string {
    anc := []string{}

    i := 0

    for i < len(nums) {
        start := nums[i]

        for i < len(nums) - 1 && nums[i] + 1 == nums[i + 1] {
            i ++
        }

        if start == nums[i] {
            anc = append(anc, strconv.Itoa(nums[i]))
        } else {
            anc = append(anc, strconv.Itoa(start) + "->" + strconv.Itoa(nums[i]))
        }

        i ++
    }

    return anc
}