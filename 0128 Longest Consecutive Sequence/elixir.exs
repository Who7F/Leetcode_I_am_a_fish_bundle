defmodule Solution do
  @spec longest_consecutive(nums :: [integer]) :: integer
  def longest_consecutive(nums) do  

    set = MapSet.new(nums)

    nums
    |> Enum.filter(fn n -> not MapSet.member?(set, n - 1) end)
    |> Enum.map(fn n -> length_from(n, set, 1) end)
    |> Enum.max(fn -> 0 end)
  end

  defp length_from(n, set, acc) do
    if MapSet.member?(set, n + 1) do
      length_from(n + 1, set, acc + 1)
    else
      acc
    end
  end
end