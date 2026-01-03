defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do
    String.to_charlist(s) |> Enum.frequencies() == String.to_charlist(t) |> Enum.frequencies()
  end
end