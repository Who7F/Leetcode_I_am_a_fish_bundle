defmodule Solution do
  @spec cal_points(operations :: [String.t()]) :: integer
  def cal_points(operations) do
    operations
    |> Enum.reduce([], fn op, stack ->
      case op do
        "+" ->
          [a, b | rest] = stack
          [a + b | stack]

        "D" ->
          [a | _] = stack
          [2 * a | stack]

        "C" ->
          [_ | rest] = stack
          rest

        _ ->
          [String.to_integer(op) | stack]
      end
    end)
    |> Enum.sum()
  end
end