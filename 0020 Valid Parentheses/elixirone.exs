defmodule Solution do
  @spec is_valid(s :: String.t()) :: boolean
  def is_valid(s) do
    s
    |> String.graphemes()
    |> check([])
  end

  defp check([], []), do: true
  defp check([], _), do: false

  defp check([c | rest], stack) do
    case c do
      "(" -> check(rest, [")" | stack])
      "[" -> check(rest, ["]" | stack])
      "{" -> check(rest, ["}" | stack])

      _ ->
        case stack do
          [top | tail] when top == c ->
            check(rest, tail)

          _ ->
            false
        end
    end
  end
end