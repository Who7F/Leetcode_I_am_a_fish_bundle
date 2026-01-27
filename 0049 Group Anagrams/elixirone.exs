defmodule Solution do
  @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
  def group_anagrams(strs) do
  strs
  |> Enum.group_by(fn s ->
    s
    |> String.graphemes()
    |> Enum.sort()
    |> Enum.join()
  end)
  |> Map.values()
  end
end