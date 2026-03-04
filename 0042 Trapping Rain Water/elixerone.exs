defmodule Solution do
  def trap([]), do: 0

  def trap(height) do
    left  = scan_max(height)
    right = height |> Enum.reverse() |> scan_max() |> Enum.reverse()

    Enum.zip([left, right, height])
    |> Enum.reduce(0, fn {l, r, h}, acc ->
      acc + min(l, r) - h
    end)
  end

  defp scan_max(list) do
    list
    |> Enum.reduce({0, []}, fn value, {prev, acc} ->
      curr = max(value, prev)
      {curr, [curr | acc]}
    end)
    |> elem(1)
    |> Enum.reverse()
  end
end