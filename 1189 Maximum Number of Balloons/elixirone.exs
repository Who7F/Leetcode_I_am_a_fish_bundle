defmodule Solution do
  @spec max_number_of_balloons(text :: String.t) :: integer
  def max_number_of_balloons(text) do
    freq = text |> String.to_charlist() |> Enum.frequencies()

    "balloon"|> String.to_charlist() |> Enum.frequencies()
        |> Enum.map(fn {c, n} -> div(Map.get(freq, c, 0), n) end)
        |> Enum.min()
  end
end