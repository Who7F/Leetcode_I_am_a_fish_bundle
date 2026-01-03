defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do
    String.bag_distance(s, t) == 1.0
  end
end