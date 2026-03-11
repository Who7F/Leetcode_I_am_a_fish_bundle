defmodule Solution do
  @spec eval_rpn(tokens :: [String.t]) :: integer
  def eval_rpn(tokens) do
    tokens
    |> Enum.reduce([], fn token, stack ->
      case token do
        "+" ->
          [y, x | rest] = stack
          [x + y | rest]

        "-" ->
          [y, x | rest] = stack
          [x - y | rest]

        "*" ->
          [y, x | rest] = stack
          [x * y | rest]

        "/" ->
          [y, x | rest] = stack
          [div(x, y) | rest]

        num ->
          [String.to_integer(num) | stack]
      end
    end)
    |> hd()
  end
end