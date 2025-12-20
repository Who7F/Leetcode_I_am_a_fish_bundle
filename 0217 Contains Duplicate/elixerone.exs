defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums) do
    MapSet.size(MapSet.new(nums)) != length(nums)
  end
end