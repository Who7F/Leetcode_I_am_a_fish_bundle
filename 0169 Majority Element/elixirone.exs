defmodule Solution do
  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    {_, candidate} =
      Enum.reduce(nums, {0, nil}, fn num, {count, cand} ->
        cond do
          count == 0 -> {1, num}
          num == cand -> {count + 1, cand}
          true -> {count - 1, cand}
        end
      end)

    candidate
  end
end