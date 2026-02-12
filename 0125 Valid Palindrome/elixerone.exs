defmodule Solution do
  @spec is_palindrome(s :: String.t) :: boolean
  def is_palindrome(s) do
    cleaned =
      s
      |> String.downcase()
      |> String.replace(~r/[^[:alnum:]]/u, "")

    cleaned == String.reverse(cleaned)
  end
end