defmodule Solution do
  @spec max_area([integer]) :: integer
  def max_area(heights) do
    heights
    |> List.to_tuple()
    |> then(fn tuple ->
      max(tuple, 0, tuple_size(tuple) - 1, 0)
    end)
  end

  defp max(_, l, r, max_vol) when l >= r,
    do: max_vol

  defp max(heights, l, r, max_vol) do
    h_l = elem(heights, l)
    h_r = elem(heights, r)

    area = (r - l) * min(h_l, h_r)
    new_max = max(max_vol, area)

    if h_l < h_r do
      max(heights, l + 1, r, new_max)
    else
      max(heights, l, r - 1, new_max)
    end
  end
end