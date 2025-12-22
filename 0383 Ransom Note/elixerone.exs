defmodule Solution do
  @spec can_construct(ransom_note :: String.t, magazine :: String.t) :: boolean
  def can_construct(ransom_note, magazine) do
    magazine = magazine |> String.to_charlist() |> Enum.frequencies()

    ransom_note
    |> String.to_charlist()
    |> Enum.frequencies()
    |> Enum.all?(fn {char, num} ->
        Map.get(magazine, char, 0) >= num
    end)
  end
end