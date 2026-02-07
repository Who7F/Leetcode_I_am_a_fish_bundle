defmodule Solution do
  def two_sum(numbers, target) do
    nums = List.to_tuple(numbers)
    do_two_sum(nums, target, 0, tuple_size(nums) - 1)
  end

  defp do_two_sum(_nums, _target, left, right) when left >= right do
    [-1, -1]
  end

  defp do_two_sum(nums, target, left, right) do
    sum = elem(nums, left) + elem(nums, right)

    cond do
      sum < target ->
        do_two_sum(nums, target, left + 1, right)

      sum > target ->
        do_two_sum(nums, target, left, right - 1)

      true ->
        [left + 1, right + 1]
    end
  end
end