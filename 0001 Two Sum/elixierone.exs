defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    findMyButt(nums, target, 0, %{})
  end

  def findMyButt([head|tail], target, position, seen)do
    if Map.has_key?(seen, target - head) do
        [Map.get(seen, target - head), position]
    else
        findMyButt(tail, target, position + 1, Map.put_new(seen, head, position))
    end
  end
end