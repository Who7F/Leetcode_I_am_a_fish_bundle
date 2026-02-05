defmodule Solution do
  @spec sorted_squares(nums :: [integer]) :: [integer]
  def sorted_squares(nums) do
    nums
    |> Enum.map(&(&1 * &1))
    |> Enum.sort()
  end
end