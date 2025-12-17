defmodule Solution do
  @spec num_jewels_in_stones(jewels :: String.t, stones :: String.t) :: integer
  def num_jewels_in_stones(jewels, stones) do
    jewels = jewels |> String.graphemes() |> MapSet.new()

    stones |> String.graphemes() |> Enum.count(&MapSet.member?(jewels, &1))
  end
end