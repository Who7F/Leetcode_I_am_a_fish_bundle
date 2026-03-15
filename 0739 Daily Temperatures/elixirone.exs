defmodule Solution do
  @spec daily_temperatures(temp :: [integer]) :: [integer]
  def daily_temperatures(temp) do
    Enum.reverse(temp)
    |> Enum.with_index()
    |> Enum.map_reduce([], &do_map_reduce/2)
    |> elem(0)
    |> Enum.reverse()
  end

  defp do_map_reduce({x, i}, [{y, j} | tail]) when x >= y do
    do_map_reduce({x, i}, tail)
  end
  defp do_map_reduce({x, i}, [{y, j} | tail]) do
    {i - j, [{x, i}, {y, j} | tail]}
  end
  defp do_map_reduce({x, i}, []) do
    {0, [{x, i}]}
  end
end