defmodule Solution do
  @spec is_valid_sudoku(board :: [[char()]]) :: boolean
  def is_valid_sudoku(board) do
    board
    |> Enum.with_index()
    |> Enum.flat_map(fn {row, i} ->
      row
      |> Enum.with_index()
      |> Enum.flat_map(fn
        {46, _} -> []
        {v, j} ->
          box = div(i, 3) * 3 + div(j, 3)
          [{:r, i, v}, {:c, j, v}, {:b, box, v}]
      end)
    end)
    |> then(fn keys ->
      length(keys) == MapSet.size(MapSet.new(keys))
    end)
  end
end