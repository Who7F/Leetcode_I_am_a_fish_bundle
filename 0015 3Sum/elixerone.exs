defmodule Solution do
  def three_sum(nums) do
    nums
    |> Enum.sort()
    |> combinations(3)
    |> Enum.filter(fn [a, b, c] -> a + b + c == 0 end)
    |> Enum.uniq()
  end

  defp combinations(_, 0), do: [[]]
  defp combinations([], _), do: []

  defp combinations([h | t], k) do
    for(l <- combinations(t, k - 1), do: [h | l]) ++
      combinations(t, k)
  end
end